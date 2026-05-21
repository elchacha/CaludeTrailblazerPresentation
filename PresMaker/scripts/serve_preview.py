#!/usr/bin/env python3
"""
serve_preview.py — Prévisualisation interactive des slides avec ouverture
des fichiers .md via l'application système par défaut (os.startfile).

Usage:
    python scripts/serve_preview.py work/<slug>/slides/
    python scripts/serve_preview.py work/<slug>/slides/ --port 8765

Ouvre automatiquement http://localhost:<port> dans le navigateur.
Ctrl+C pour arrêter.
"""

import argparse
import json
import os
import re
import sys
import webbrowser
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import parse_qs, urlparse, unquote


# ---------------------------------------------------------------------------
# Lecture des slides
# ---------------------------------------------------------------------------

def parse_frontmatter(content):
    match = re.match(r'^---\n(.*?)\n---\n?(.*)', content, re.DOTALL)
    if not match:
        return {}, content
    fm_text, body = match.groups()
    fm = {}
    for line in fm_text.strip().splitlines():
        if ':' in line:
            key, _, value = line.partition(':')
            fm[key.strip()] = value.strip()
    return fm, body.strip()


def read_slides(slides_dir: Path):
    slide_files = sorted(slides_dir.glob('slide-*.md'))
    if not slide_files:
        print(f"Aucun fichier slide-XX.md trouve dans {slides_dir}", file=sys.stderr)
        sys.exit(1)
    slides = []
    for path in slide_files:
        content = path.read_text(encoding='utf-8')
        fm, body = parse_frontmatter(content)
        slides.append({
            'numero':   int(fm.get('numero', 0)),
            'titre':    fm.get('titre', path.stem),
            'type':     fm.get('type', 'contenu'),
            'content':  body,
            'filename': path.name,
        })
    return slides


# ---------------------------------------------------------------------------
# Template HTML (mode serveur — bouton .md via fetch /open)
# ---------------------------------------------------------------------------

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Preview — {title}</title>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ display: flex; height: 100vh; font-family: 'Segoe UI', sans-serif; background: #0f0f17; color: #e0e0f0; overflow: hidden; }}
  #sidebar {{
    width: 300px; min-width: 220px;
    background: #16161f; border-right: 1px solid #2a2a3a;
    overflow-y: auto; display: flex; flex-direction: column; flex-shrink: 0;
  }}
  #sidebar h2 {{
    padding: 14px 16px; font-size: 0.78em; text-transform: uppercase;
    letter-spacing: 0.1em; color: #7070a0; border-bottom: 1px solid #2a2a3a; line-height: 1.4;
  }}
  .slide-item {{
    padding: 10px 16px; cursor: pointer;
    border-bottom: 1px solid #1e1e2a; transition: background 0.12s;
  }}
  .slide-item:hover {{ background: #1e1e2e; }}
  .slide-item.active {{ background: #252540; border-left: 3px solid #7c6af7; padding-left: 13px; }}
  .slide-num {{ font-size: 0.70em; color: #5555aa; margin-bottom: 2px; }}
  .slide-title {{ font-size: 0.85em; line-height: 1.3; color: #d0d0e8; }}
  .slide-type {{ font-size: 0.65em; color: #444466; margin-top: 3px; text-transform: uppercase; letter-spacing: 0.05em; }}
  .slide-type.intro      {{ color: #6655aa; }}
  .slide-type.agenda     {{ color: #446688; }}
  .slide-type.contenu    {{ color: #448866; }}
  .slide-type.transition {{ color: #886644; }}
  .slide-type.conclusion {{ color: #aa6655; }}
  .slide-type.final      {{ color: #667788; }}
  #main {{ flex: 1; display: flex; flex-direction: column; overflow: hidden; }}
  #content {{ flex: 1; padding: 40px 60px 20px; overflow-y: auto; }}
  #content h1 {{ font-size: 2em; margin-bottom: 0.6em; color: #c0b0ff; line-height: 1.2; }}
  #content h2 {{ font-size: 1.4em; margin: 1.2em 0 0.5em; color: #a0a0d0; }}
  #content h3 {{ font-size: 1.1em; margin: 1em 0 0.4em; color: #8888bb; }}
  #content p  {{ line-height: 1.7; margin-bottom: 0.8em; color: #c8c8e0; }}
  #content ul, #content ol {{ margin: 0.5em 0 1em 1.5em; line-height: 1.8; color: #c8c8e0; }}
  #content li {{ margin-bottom: 0.3em; }}
  #content blockquote {{
    border-left: 3px solid #7c6af7; padding: 8px 16px;
    background: #1a1a2e; color: #aaaacc; margin: 1em 0; border-radius: 0 4px 4px 0;
  }}
  #content table {{ border-collapse: collapse; width: 100%; margin: 1em 0; }}
  #content th {{ background: #1e1e30; padding: 8px 12px; text-align: left; color: #9090cc; font-weight: 600; }}
  #content td {{ padding: 8px 12px; border-bottom: 1px solid #2a2a3a; color: #c0c0d8; }}
  #content tr:nth-child(even) td {{ background: #13131e; }}
  #content code {{ background: #1a1a2e; padding: 2px 6px; border-radius: 3px; font-family: 'Consolas', monospace; color: #a0d0ff; font-size: 0.92em; }}
  #content pre {{ background: #1a1a2e; padding: 16px; border-radius: 6px; overflow-x: auto; margin: 1em 0; border: 1px solid #2a2a3a; }}
  #content pre code {{ background: none; padding: 0; color: #c8e0c8; }}
  #content hr {{ border: none; border-top: 1px solid #2a2a3a; margin: 1.5em 0; }}
  #content .notes-block {{
    margin-top: 2em; padding: 12px 16px; background: #131310;
    border-left: 3px solid #665530; border-radius: 0 4px 4px 0;
    font-size: 0.84em; color: #888870; font-style: italic;
  }}
  #content .notes-block::before {{
    content: 'Notes presentateur';
    display: block; font-weight: 600; font-style: normal;
    margin-bottom: 6px; color: #aaaa80; font-size: 0.9em;
  }}
  #nav-bar {{
    border-top: 1px solid #2a2a3a; padding: 8px 24px;
    display: flex; justify-content: space-between; align-items: center;
    font-size: 0.82em; color: #555577; background: #0f0f17; flex-shrink: 0; gap: 12px;
  }}
  #nav-bar button, #btn-open-md {{
    background: #1e1e30; border: 1px solid #3a3a5a; color: #9090cc;
    padding: 5px 16px; border-radius: 4px; cursor: pointer; font-size: 0.88em;
    text-decoration: none; display: inline-block; transition: background 0.1s;
  }}
  #nav-bar button:hover:not(:disabled), #btn-open-md:hover {{ background: #252540; color: #c0c0ff; }}
  #nav-bar button:disabled {{ opacity: 0.25; cursor: default; }}
  #nav-label {{ color: #6060aa; font-size: 0.9em; flex: 1; text-align: center; }}
  #btn-open-md {{ color: #7070aa; font-size: 0.80em; padding: 5px 10px; }}
  #btn-open-md.ok  {{ color: #44aa66; border-color: #336644; }}
  #btn-open-md.err {{ color: #aa4444; border-color: #663333; }}
</style>
</head>
<body>

<div id="sidebar">
  <h2>{sidebar_title}</h2>
  <div id="slide-list"></div>
</div>

<div id="main">
  <div id="content"></div>
  <div id="nav-bar">
    <button id="btn-prev" onclick="navigate(-1)">&#8592; Precedent</button>
    <span id="nav-label"></span>
    <button id="btn-open-md" title="Ouvrir le fichier .md avec l'application par defaut">&#128196; .md</button>
    <button id="btn-next" onclick="navigate(1)">Suivant &#8594;</button>
  </div>
</div>

<script>
const slides = {slides_json};
let current = 0;

function extractNotes(text) {{
  const m = text.match(/<!--\\s*notes:\\s*([\\s\\S]*?)\\s*-->/);
  return m ? m[1].trim() : null;
}}

function renderSlide(index) {{
  current = index;
  const slide = slides[index];

  document.querySelectorAll('.slide-item').forEach((el, i) =>
    el.classList.toggle('active', i === index));

  let body = slide.content;
  const notes = extractNotes(body);
  body = body.replace(/<!--\\s*notes:[\\s\\S]*?-->/g, '').trim();

  let html = marked.parse(body);
  if (notes) html += `<div class="notes-block">${{notes}}</div>`;

  const el = document.getElementById('content');
  el.innerHTML = html;
  el.scrollTop = 0;

  document.getElementById('nav-label').textContent =
    `Slide ${{index + 1}} / ${{slides.length}} — ${{slide.filename}}`;
  document.getElementById('btn-prev').disabled = index === 0;
  document.getElementById('btn-next').disabled = index === slides.length - 1;

  const btn = document.getElementById('btn-open-md');
  btn.classList.remove('ok', 'err');

  document.querySelectorAll('.slide-item')[index]
    ?.scrollIntoView({{ block: 'nearest', behavior: 'smooth' }});
}}

function navigate(dir) {{
  const n = current + dir;
  if (n >= 0 && n < slides.length) renderSlide(n);
}}

document.getElementById('btn-open-md').addEventListener('click', () => {{
  const btn = document.getElementById('btn-open-md');
  fetch('/open?file=' + encodeURIComponent(slides[current].filename))
    .then(r => {{
      btn.classList.toggle('ok',  r.ok);
      btn.classList.toggle('err', !r.ok);
      setTimeout(() => btn.classList.remove('ok', 'err'), 1500);
    }})
    .catch(() => {{
      btn.classList.add('err');
      setTimeout(() => btn.classList.remove('err'), 1500);
    }});
}});

document.addEventListener('keydown', e => {{
  if (e.key === 'ArrowRight' || e.key === 'ArrowDown') navigate(1);
  if (e.key === 'ArrowLeft'  || e.key === 'ArrowUp')   navigate(-1);
}});

const list = document.getElementById('slide-list');
slides.forEach((s, i) => {{
  const div = document.createElement('div');
  div.className = 'slide-item';
  div.innerHTML = `
    <div class="slide-num">Slide ${{String(i+1).padStart(2,'0')}}</div>
    <div class="slide-title">${{s.titre}}</div>
    <div class="slide-type ${{s.type}}">${{s.type}}</div>`;
  div.onclick = () => renderSlide(i);
  list.appendChild(div);
}});

renderSlide(0);
</script>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Serveur HTTP
# ---------------------------------------------------------------------------

def make_handler(slides_dir: Path, html_bytes: bytes):
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed = urlparse(self.path)

            if parsed.path in ('/', '/index.html'):
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(html_bytes)

            elif parsed.path == '/open':
                qs = parse_qs(parsed.query)
                filename = unquote(qs.get('file', [''])[0])
                filepath = (slides_dir / filename).resolve()
                # Securite : rester dans le dossier slides
                if filepath.parent == slides_dir.resolve() and filepath.suffix == '.md' and filepath.exists():
                    os.startfile(str(filepath))
                    self._ok('Ouvert')
                else:
                    self.send_response(400)
                    self.end_headers()

            else:
                self.send_response(404)
                self.end_headers()

        def _ok(self, msg='OK'):
            body = msg.encode()
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *_):
            pass  # Silence les logs HTTP

    return Handler


# ---------------------------------------------------------------------------
# Point d'entrée
# ---------------------------------------------------------------------------

def find_free_port(preferred=8765):
    import socket
    for port in range(preferred, preferred + 20):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('localhost', port)) != 0:
                return port
    return preferred


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('slides_dir')
    parser.add_argument('--port', type=int, default=8765)
    args = parser.parse_args()

    slides_dir = Path(args.slides_dir).resolve()
    if not slides_dir.is_dir():
        print(f"Repertoire introuvable : {slides_dir}", file=sys.stderr)
        sys.exit(1)

    slides = read_slides(slides_dir)
    slug = slides_dir.parent.name
    sidebar_title = slug.replace('-', ' ').title()
    title = slides[0]['titre'] if slides else 'Preview'

    html = HTML_TEMPLATE.format(
        title=title,
        sidebar_title=sidebar_title,
        slides_json=json.dumps(slides, ensure_ascii=False, indent=2),
    )
    html_bytes = html.encode('utf-8')

    port = find_free_port(args.port)
    url  = f'http://localhost:{port}'

    server = HTTPServer(('localhost', port), make_handler(slides_dir, html_bytes))

    print(f"[serve_preview] {len(slides)} slides - {url}")
    print(f"[serve_preview] Ctrl+C pour arreter")

    threading.Timer(0.4, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[serve_preview] Arrete.")

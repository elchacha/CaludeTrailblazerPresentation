#!/usr/bin/env python3
"""
gen_presentation.py — Génère index.html Reveal.js à partir des slides enrichis
et du fichier theme.json produit par Claude.

Usage:
    python scripts/gen_presentation.py work/<slug>/
"""

import json
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Lecture
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
            fm[key.strip()] = value.strip().strip('"\'')  # retire les guillemets YAML optionnels
    return fm, body.strip()


def read_slides(slides_dir: Path):
    files = sorted(slides_dir.glob('slide-*.md'))
    if not files:
        print(f"Aucun slide-XX.md dans {slides_dir}", file=sys.stderr)
        sys.exit(1)
    slides = []
    for path in files:
        content = path.read_text(encoding='utf-8')
        fm, body = parse_frontmatter(content)
        match = re.search(r'slide-(\d+)\.md', path.name)
        default_num = match.group(1) if match else '00'
        slides.append({
            'numero':  fm.get('numero', default_num).zfill(2),
            'titre':   fm.get('titre', ''),
            'type':    fm.get('type', 'contenu'),
            'content': body,
        })
    return slides


def read_theme(project_dir: Path) -> dict:
    path = project_dir / 'theme.json'
    if not path.exists():
        print(f"[WARN] theme.json absent — theme par defaut utilise")
        return {}
    return json.loads(path.read_text(encoding='utf-8'))


# ---------------------------------------------------------------------------
# Conversion slide → section Reveal.js
# ---------------------------------------------------------------------------

def notes_from_content(body: str):
    """Extrait et supprime le commentaire <!-- notes: ... --> du corps."""
    match = re.search(r'<!--\s*notes:\s*([\s\S]*?)\s*-->', body)
    if match:
        notes = match.group(1).strip()
        body = re.sub(r'<!--\s*notes:[\s\S]*?-->', '', body).strip()
        return body, notes
    return body, None


def slide_to_section(slide: dict, theme: dict) -> str:
    """Convertit un slide en <section> Reveal.js avec data-markdown."""
    numero  = slide['numero']
    stype   = slide['type']
    body, notes = notes_from_content(slide['content'])

    # Attributs de section
    attrs = [f'<!-- SLIDE {numero} -->']
    section_attrs = []

    # Couleur de fond par type ou override dans theme.json
    bg_overrides = theme.get('slide_backgrounds', {})
    if numero in bg_overrides:
        section_attrs.append(f'data-background-color="{bg_overrides[numero]}"')
    elif stype == 'transition':
        bg = theme.get('transition_bg', theme.get('accent', '#7c6af7'))
        section_attrs.append(f'data-background-color="{bg}"')

    # Auto-animate sur intro et transition
    if stype in ('intro', 'transition'):
        section_attrs.append('data-auto-animate')

    attr_str = ' '.join(section_attrs)
    open_tag = f'<section data-markdown {attr_str}>'.replace('  ', ' ').strip() \
               if attr_str else '<section data-markdown>'

    # Le contenu Markdown dans <textarea data-template>
    # On convertit <!-- notes --> en syntaxe Reveal.js (Note:)
    md_content = body
    if notes:
        md_content += f'\n\nNote:\n{notes}'

    # Indentation propre pour le textarea
    lines = md_content.splitlines()
    indented = '\n'.join('          ' + l for l in lines)

    return f"""        {attrs[0]}
        {open_tag}
          <textarea data-template>
{indented}
          </textarea>
        </section>"""


# ---------------------------------------------------------------------------
# Template HTML Reveal.js
# ---------------------------------------------------------------------------

REVEAL_HTML = """\
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reset.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/theme/{reveal_theme}.css">
<style>
{custom_css}
</style>
</head>
<body>
<div class="reveal">
  <div class="slides">

{sections}

  </div>
</div>
<!-- Reveal.js depuis CDN — pas d'assets locaux -->
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.js"></script>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/markdown/markdown.js"></script>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/highlight/highlight.js"></script>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/notes/notes.js"></script>
<script>
Reveal.initialize({{
  hash: true,
  slideNumber: true,
  progress: true,
  controls: true,
  transition: '{transition}',
{extra_options}  plugins: [ RevealMarkdown, RevealHighlight, RevealNotes ]
}});
</script>
</body>
</html>
"""


DEFAULT_CSS = """\
  .reveal h1 { font-size: 2.2em; }
  .reveal h2 { font-size: 1.5em; }
  .reveal ul  { text-align: left; }
  .reveal blockquote { font-style: italic; opacity: 0.85; }
  .reveal table { margin: 0 auto; }
  .reveal pre  { width: 100%; }
"""


def format_reveal_options(options: dict) -> str:
    """Formate les options Reveal.js extra depuis theme.json en propriétés JS."""
    if not options:
        return ''
    lines = []
    for key, value in options.items():
        if isinstance(value, str):
            lines.append(f'  {key}: "{value}",')
        elif isinstance(value, bool):
            lines.append(f'  {key}: {"true" if value else "false"},')
        else:
            lines.append(f'  {key}: {value},')
    return '\n'.join(lines) + '\n'


def build_html(slides: list, theme: dict, title: str) -> str:
    reveal_theme  = theme.get('reveal_theme', 'black')
    transition    = theme.get('transition', 'slide')
    custom_css    = theme.get('custom_css', DEFAULT_CSS)
    extra_options = format_reveal_options(theme.get('reveal_options', {}))

    sections = '\n\n'.join(slide_to_section(s, theme) for s in slides)

    return REVEAL_HTML.format(
        title=title,
        reveal_theme=reveal_theme,
        transition=transition,
        custom_css=custom_css,
        extra_options=extra_options,
        sections=sections,
    )


# ---------------------------------------------------------------------------
# slides-final.md
# ---------------------------------------------------------------------------

def build_slides_final(slides: list) -> str:
    parts = []
    for s in slides:
        body, _ = notes_from_content(s['content'])
        parts.append(f"## Slide {s['numero']} — {s['titre']}\n\n{body}")
    return '\n\n---\n\n'.join(parts)


# ---------------------------------------------------------------------------
# Point d'entrée
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python scripts/gen_presentation.py work/<slug>/", file=sys.stderr)
        sys.exit(1)

    project_dir = Path(sys.argv[1]).resolve()
    slides_dir  = project_dir / 'slides'
    output_dir  = project_dir / 'presentation'
    output_dir.mkdir(exist_ok=True)

    slides = read_slides(slides_dir)
    theme  = read_theme(project_dir)

    # Titre depuis theme.json ou premier slide
    title = theme.get('title', slides[0]['titre'] if slides else 'Présentation')

    html = build_html(slides, theme, title)
    (output_dir / 'index.html').write_text(html, encoding='utf-8')
    print(f"[OK] index.html genere : {output_dir / 'index.html'}")

    md = build_slides_final(slides)
    (output_dir / 'slides-final.md').write_text(md, encoding='utf-8')
    print(f"[OK] slides-final.md genere")
    print(f"     {len(slides)} slides, theme: {theme.get('reveal_theme', 'black')}")

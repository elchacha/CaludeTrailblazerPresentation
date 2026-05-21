#!/usr/bin/env python3
"""
update-slide.py — PostToolUse hook : met à jour une <section> dans index.html
quand Claude édite un fichier slide-XX.md.

Pour un rendu complet et stylé, utiliser /present --slide=XX.
Ce script fait une conversion MD→HTML basique mais immédiate.
"""
import sys, json, re, os

# ── Couleurs de fond par partie (transitions) ──────────────────────────
TRANSITION_BG = {
    1: '#00A1E0', 2: '#032D60', 3: '#c94b00', 4: '#6a1e7a', 5: '#007a6e'
}

def main():
    try:
        raw = sys.stdin.read()
        event = json.loads(raw) if raw.strip() else {}
    except Exception:
        sys.exit(0)

    file_path = (event.get('tool_input') or {}).get('file_path', '')
    if not file_path:
        sys.exit(0)

    file_path = file_path.replace('\\', '/')

    m = re.search(r'work/([^/]+)/slides/slide-(\d+)\.md$', file_path)
    if not m:
        sys.exit(0)

    try:
        _process(event, file_path, m)
    except Exception as e:
        print(f"[update-slide] erreur ignorée : {e}", file=sys.stderr)
        sys.exit(0)


def _process(event, file_path, m):

    slug = m.group(1)
    slide_num = int(m.group(2))

    base_dir = file_path.split('/work/')[0]
    html_path = f"{base_dir}/work/{slug}/presentation/index.html"

    if not os.path.exists(html_path.replace('/', os.sep)):
        sys.exit(0)  # Pas encore de présentation générée

    with open(file_path.replace('/', os.sep), 'r', encoding='utf-8') as f:
        source = f.read()

    fm, body = parse_frontmatter(source)

    # Supprimer les directives @xxx@
    body = re.sub(r'@[^@\n]+@', '', body).strip()

    new_section = generate_section(body, fm, slide_num)

    with open(html_path.replace('/', os.sep), 'r', encoding='utf-8') as f:
        html = f.read()

    updated = replace_section(html, slide_num, new_section)

    if updated != html:
        with open(html_path.replace('/', os.sep), 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"[update-slide] slide-{slide_num:02d} mis à jour dans index.html", file=sys.stderr)
    else:
        print(f"[update-slide] aucun changement détecté pour slide-{slide_num:02d}", file=sys.stderr)


def parse_frontmatter(source):
    fm = {}
    m = re.match(r'^---\n(.*?)\n---\n', source, re.DOTALL)
    if m:
        for line in m.group(1).split('\n'):
            if ':' in line:
                k, v = line.split(':', 1)
                fm[k.strip()] = v.strip()
        return fm, source[m.end():]
    return fm, source


def replace_section(html, slide_num, new_section):
    """Remplace la <section> du slide N dans le HTML.
    Cherche le bloc de commentaires <!-- SLIDE XX puis la section qui suit.
    """
    pattern = (
        r'(    <!-- ═+[^\n]* -->\n'
        r'    <!-- SLIDE {:02d}[^\n]*\n'
        r'    <!-- ═+[^\n]* -->\n)'
        r'    <section[\s\S]*?</section>'.format(slide_num)
    )
    replacement = r'\g<1>    ' + new_section
    result = re.sub(pattern, replacement, html, count=1, flags=re.DOTALL)
    return result


def generate_section(body, fm, slide_num):
    slide_type = fm.get('type', 'contenu')
    partie = int(fm.get('partie', 0))

    notes_html = ''
    notes_m = re.search(r'<!-- notes: (.*?) -->', body, re.DOTALL)
    if notes_m:
        notes_html = f'\n      <aside class="notes">{notes_m.group(1).strip()}</aside>'
        body = (body[:notes_m.start()] + body[notes_m.end():]).strip()

    if slide_type == 'transition':
        bg = TRANSITION_BG.get(partie, '#00A1E0')
        content = md_to_html(body, fragment=False)
        return (
            f'<section data-background-color="{bg}" class="transition-slide">\n'
            f'{content}{notes_html}\n'
            f'    </section>'
        )
    else:
        content = md_to_html(body, fragment=True)
        return (
            f'<section data-background-color="#0a0f1e">\n'
            f'{content}{notes_html}\n'
            f'    </section>'
        )


def md_to_html(md, fragment=True):
    frag = ' class="fragment"' if fragment else ''
    lines = md.split('\n')
    out = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Heading
        if line.startswith('### '):
            out.append(f'      <h3>{inline(line[4:])}</h3>')
        elif line.startswith('## '):
            out.append(f'      <h2>{inline(line[3:])}</h2>')
        elif line.startswith('# '):
            out.append(f'      <h1>{inline(line[2:])}</h1>')

        # Blockquote
        elif line.startswith('> '):
            out.append(f'      <blockquote{frag}>{inline(line[2:])}</blockquote>')

        # Code block
        elif line.startswith('```'):
            lang = line[3:].strip() or 'plaintext'
            code = []
            i += 1
            while i < len(lines) and not lines[i].startswith('```'):
                code.append(lines[i])
                i += 1
            out.append(f'      <pre><code class="{lang}">' + '\n'.join(code) + '</code></pre>')

        # Table
        elif '|' in line and i + 1 < len(lines) and re.match(r'^\|[-| :]+\|$', lines[i + 1]):
            headers = [h.strip() for h in line.strip('|').split('|')]
            i += 2
            out.append('      <table>')
            out.append('        <thead><tr>' + ''.join(f'<th>{inline(h)}</th>' for h in headers) + '</tr></thead>')
            out.append('        <tbody>')
            while i < len(lines) and '|' in lines[i] and lines[i].strip():
                cells = [c.strip() for c in lines[i].strip('|').split('|')]
                out.append(f'          <tr{frag}>' + ''.join(f'<td>{inline(c)}</td>' for c in cells) + '</tr>')
                i += 1
            out.append('        </tbody>')
            out.append('      </table>')
            continue

        # Unordered list
        elif re.match(r'^[-*] ', line):
            out.append('      <ul>')
            while i < len(lines) and re.match(r'^[-*] ', lines[i]):
                out.append(f'        <li{frag}>{inline(lines[i][2:])}</li>')
                i += 1
            out.append('      </ul>')
            continue

        # Ordered list
        elif re.match(r'^\d+\. ', line):
            out.append('      <ol>')
            while i < len(lines) and re.match(r'^\d+\. ', lines[i]):
                out.append(f'        <li>{inline(re.sub(r"^\d+\. ", "", lines[i]))}</li>')
                i += 1
            out.append('      </ol>')
            continue

        # HR
        elif line.strip() in ('---', '***', '___'):
            out.append('      <hr>')

        # Empty line
        elif not line.strip():
            out.append('')

        # Paragraph (accumule les lignes consécutives)
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not re.match(
                r'^(#{1,3} |[-*] |\d+\. |> |```|[|])', lines[i]
            ) and lines[i].strip() not in ('---', '***', '___'):
                para.append(inline(lines[i]))
                i += 1
            if para:
                out.append(f'      <p{frag}>{" ".join(para)}</p>')
            continue

        i += 1

    return '\n'.join(out)


def inline(text):
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
    return text


if __name__ == '__main__':
    main()

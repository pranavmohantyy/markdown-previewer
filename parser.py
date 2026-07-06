def parse_headers(markdown):
    lines = markdown.split('\n')
    html = ''
    for line in lines:
        if line.startswith('# '):
            html += f'<h1>{line[2:].strip()}</h1>\n'
        elif line.startswith('## '):
            html += f'<h2>{line[3:].strip()}</h2>\n'
        elif line.startswith('### '):
            html += f'<h3>{line[4:].strip()}</h3>\n'
    return html

def parse_bold(markdown):
    return markdown.replace('**', '<strong>', 1).replace('**', '</strong>', 1)

def parse_italic(markdown):
    return markdown.replace('*', '<em>', 1).replace('*', '</em>', 1)

def parse_links(markdown):
    import re
    return re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown)

def parse_images(markdown):
    import re
    return re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', markdown)


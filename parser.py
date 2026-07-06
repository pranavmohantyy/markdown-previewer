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

def parse_lists(markdown):
    lines = markdown.split('\n')
    html = ''
    ordered = False
    for line in lines:
        if line.startswith('- '):
            if '<ul>' not in html:
                html += '<ul>\n'
            html += f'    <li>{line[2:].strip()}</li>\n'
        elif line.startswith('1. '):
            if '<ol>' not in html:
                html += '<ol>\n'
                ordered = True
            html += f'    <li>{line[3:].strip()}</li>\n'
        else:
            if ordered:
                html += '</ol>\n'
                ordered = False
            if '<ul>' in html:
                html += '</ul>\n'
    if ordered:
        html += '</ol>\n'
    if '<ul>' in html:
        html += '</ul>\n'
    return html

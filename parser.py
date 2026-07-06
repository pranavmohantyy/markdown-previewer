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

def parse_code(markdown):
    return markdown.replace('`', '<code>', 1).replace('`', '</code>', 1)

def parse_blockquotes(markdown):
    lines = markdown.split('\n')
    html = ''
    for line in lines:
        if line.startswith('> '):
            html += f'<blockquote>{line[2:].strip()}</blockquote>\n'
        else:
            html += line + '\n'
    return html

def parse_code_block(markdown):
    lines = markdown.split('\n')
    in_code_block = False
    html = ''
    code_buffer = ''
    for line in lines:
        if line.startswith('```'):
            if in_code_block:
                html += f'<pre><code>{code_buffer}</code></pre>\n'
                code_buffer = ''
                in_code_block = False
            else:
                in_code_block = True
        elif in_code_block:
            code_buffer += line + '\n'
        else:
            html += line + '\n'
    return html

def parse_markdown(markdown):
    parsed = parse_headers(markdown)
    parsed += parse_bold(markdown)
    parsed += parse_italic(markdown)
    parsed += parse_code(markdown)
    parsed += parse_blockquotes(markdown)
    parsed += parse_code_block(markdown)
    return parsed
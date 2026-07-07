import argparse
import webbrowser

from parser import parse_headers, parse_bold, parse_italic


def wrap_html(content):
    return f'<!DOCTYPE html><html><head><title>Markdown Preview</title></head><body>{content}</body></html>'


def main():
    parser = argparse.ArgumentParser(description='Markdown Previewer')
    parser.add_argument('input', help='input markdown file')
    parser.add_argument('--output', help='output html file', default='output.html')
    parser.add_argument('--open', action='store_true', help='open in browser')
    args = parser.parse_args()

    with open(args.input, 'r') as f:
        markdown_content = f.read()

    html_content = parse_headers(markdown_content)
    html_content += parse_bold(markdown_content)
    html_content += parse_italic(markdown_content)
    final_html = wrap_html(html_content)

    with open(args.output, 'w') as f:
        f.write(final_html)

    if args.open:
        webbrowser.open(f'file://{args.output}')


if __name__ == '__main__':
    main()
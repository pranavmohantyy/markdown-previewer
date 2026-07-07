import argparse
import webbrowser
import os
import time

from parser import parse_headers, parse_bold, parse_italic


def wrap_html(content):
    return f'<!DOCTYPE html><html><head><title>Markdown Preview</title></head><body>{content}</body></html>'


def main():
    parser = argparse.ArgumentParser(description='Markdown Previewer')
    parser.add_argument('input', help='input markdown file')
    parser.add_argument('--output', help='output html file', default='output.html')
    parser.add_argument('--open', action='store_true', help='open in browser')
    parser.add_argument('--watch', action='store_true', help='watch for changes')
    args = parser.parse_args()

    last_mtime = 0
    while True:
        if os.path.exists(args.input):
            mtime = os.path.getmtime(args.input)
            if mtime != last_mtime:
                last_mtime = mtime
                with open(args.input, 'r') as f:
                    markdown_content = f.read()
                html_content = parse_headers(markdown_content) + parse_bold(markdown_content) + parse_italic(markdown_content)
                with open(args.output, 'w') as f:
                    f.write(wrap_html(html_content))
                if args.open:
                    webbrowser.open(args.output)
            if not args.watch:
                break
        time.sleep(1)

if __name__ == '__main__':
    main()
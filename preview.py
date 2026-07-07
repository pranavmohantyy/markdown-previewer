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

    while True:
        with open(args.input, 'r') as file:
            markdown = file.read()

        html_content = parse_headers(markdown)
        html_content += parse_bold(markdown)
        html_content += parse_italic(markdown)

        html = wrap_html(html_content)

        with open(args.output, 'w') as output_file:
            output_file.write(html)

        if args.open:
            webbrowser.open('file://' + os.path.realpath(args.output))

        if not args.watch:
            break

        time.sleep(2)


if __name__ == '__main__':
    main()
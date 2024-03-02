import sys,os,markdown

if len(sys.argv) < 2:
    print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

with open(input_file, 'r') as f:
    md_content = f.read()
    html_content = markdown.markdown(md_content)

with open(output_file, 'w') as f:
    f.write(html_content)

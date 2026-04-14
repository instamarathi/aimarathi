#!/usr/bin/env python3
"""Build script: replaces {{NAV}} and {{FOOTER}} in src/ files, outputs to root."""

import os
import shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'src')
INCLUDES = os.path.join(ROOT, '_includes')

# Read partials
with open(os.path.join(INCLUDES, 'nav.html'), 'r') as f:
    nav_html = f.read()

with open(os.path.join(INCLUDES, 'footer.html'), 'r') as f:
    footer_html = f.read()

count = 0
for dirpath, dirs, files in os.walk(SRC):
    for filename in files:
        if not filename.endswith('.html'):
            continue

        src_path = os.path.join(dirpath, filename)
        rel_path = os.path.relpath(src_path, SRC)
        out_path = os.path.join(ROOT, rel_path)

        with open(src_path, 'r') as f:
            content = f.read()

        content = content.replace('{{NAV}}', nav_html)
        content = content.replace('{{FOOTER}}', footer_html)

        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, 'w') as f:
            f.write(content)

        count += 1

print(f'Built {count} pages.')

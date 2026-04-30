import os
import re
from pathlib import Path

WEB_DIR = Path("web")

def fix_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Unescape the table HTML
    # We target specifically the string that was likely escaped
    content = content.replace("&lt;div style=&quot;overflow-x:auto;&quot;&gt;", '<div style="overflow-x:auto;">')
    content = content.replace("&lt;table style=&quot;width:100%; border-collapse: collapse; text-align: left;&quot;&gt;", '<table style="width:100%; border-collapse: collapse; text-align: left;">')
    content = content.replace("&lt;tr style=&quot;border-bottom: 1px solid var(--border);&quot;&gt;", '<tr style="border-bottom: 1px solid var(--border);">')
    content = content.replace("&lt;th style=&quot;padding: 8px;&quot;&gt;", '<th style="padding: 8px;">')
    content = content.replace("&lt;/th&gt;", "</th>")
    content = content.replace("&lt;/tr&gt;", "</tr>")
    content = content.replace("&lt;td style=&quot;padding: 8px;&quot;&gt;", '<td style="padding: 8px;">')
    content = content.replace("&lt;/td&gt;", "</td>")
    content = content.replace("&lt;/table&gt;", "</table>")
    content = content.replace("&lt;/div&gt;", "</div>")
    content = content.replace("&lt;tr&gt;", "<tr>")

    # 2. Remove the second (duplicate) Format Comparison Table section
    # Search for the second occurrence of the table section
    sections = content.split('<section class="section">')
    new_sections = []
    table_count = 0
    
    # This is a bit risky, let's use a more specific regex to find the duplicate section
    # The duplicate section usually looks like: <section class="section"> ... <h2>Format Comparison Table</h2> ... </section>
    
    # Pattern to find the section containing the table
    pattern = r'<section class="section[^"]*">\s*<div class="container">\s*<h2>Format Comparison Table</h2>.*?</div>\s*</section>'
    
    matches = list(re.finditer(pattern, content, re.DOTALL))
    if len(matches) > 1:
        # Keep only the first match
        first_match = matches[0]
        # Remove subsequent matches
        for m in reversed(matches[1:]):
            content = content[:m.start()] + content[m.end():]
            print(f"Removed duplicate table section from {file_path}")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    # Find all index.html files in subdirectories
    for root, dirs, files in os.walk(WEB_DIR):
        if "index.html" in files:
            file_path = Path(root) / "index.html"
            # Skip the root index.html if it doesn't have the issue
            fix_file(file_path)

if __name__ == "__main__":
    main()

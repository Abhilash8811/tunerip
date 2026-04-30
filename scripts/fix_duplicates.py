import os
import re
from pathlib import Path

WEB_DIR = Path("web")

def clean_duplicates(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Pattern for FAQ sections
    # We want to find cases where we have multiple <h2>Frequently asked questions</h2> or similar
    
    # 1. Check for duplicate <h2>Frequently asked questions</h2>
    faq_headers = ["Frequently asked questions", "YouTube to MP3 Converter FAQ", "FAQ"]
    for header in faq_headers:
        pattern = r'<section class="section[^"]*">\s*<div class="container">\s*<h[23][^>]*>' + re.escape(header) + r'.*?</div>\s*</section>'
        matches = list(re.finditer(pattern, content, re.DOTALL | re.IGNORECASE))
        if len(matches) > 1:
            # Keep only the LAST one (usually the most updated one I added) or the FIRST one if the last is empty
            # Actually, let's keep the one that has the most <details> or <li> tags inside
            best_match = max(matches, key=lambda m: len(re.findall(r'<details|<li>', m.group(0))))
            
            # Remove all matches except the best one
            for m in reversed(matches):
                if m != best_match:
                    content = content[:m.start()] + content[m.end():]
                    print(f"Removed duplicate FAQ section from {file_path}")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    for root, dirs, files in os.walk(WEB_DIR):
        if "index.html" in files:
            file_path = Path(root) / "index.html"
            clean_duplicates(file_path)

if __name__ == "__main__":
    main()

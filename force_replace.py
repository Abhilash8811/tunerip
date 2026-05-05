import re

with open('web/download-lagu-youtube/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# I will use the exact good content from replace_script_final.py but with word count trimmed by me manually.
# First let's load that script's content variable.
from replace_script_final import content

# Replace the content. The target is everything inside <div class="main-content"> ... </div> before <!-- Ad: Sidebar (Desktop Only) -->
new_html = re.sub(
    r'(<div class="main-content">\n\n).*?(  </div>\n\n  <!-- Ad: Sidebar \(Desktop Only\) -->)',
    r'\1' + content.replace('\\', '\\\\') + r'\n\2',
    html,
    flags=re.DOTALL
)

with open('web/download-lagu-youtube/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Done replacing.")

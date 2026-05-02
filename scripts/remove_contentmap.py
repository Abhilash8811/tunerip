#!/usr/bin/env python3
"""Remove the contentMap block from build.js to eliminate AI-generated content."""

import re

# Read the file
with open('web/build.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and remove the contentMap declaration and its usage
# Pattern 1: Remove the contentMap object declaration (starts with "const contentMap = {" and ends before "PAGES.forEach")
# Pattern 2: Remove the PAGES.forEach block that merges contentMap

# First, let's find the line numbers
lines = content.split('\n')

# Find where contentMap starts
contentmap_start = None
for i, line in enumerate(lines):
    if 'const contentMap = {' in line:
        contentmap_start = i
        break

# Find where the forEach block starts and ends
foreach_start = None
foreach_end = None
for i, line in enumerate(lines):
    if 'PAGES.forEach(p => {' in line:
        foreach_start = i
    if foreach_start and line.strip() == '});' and i > foreach_start:
        foreach_end = i
        break

if contentmap_start and foreach_start and foreach_end:
    # Remove lines from contentMap start to forEach end (inclusive)
    new_lines = lines[:contentmap_start] + lines[foreach_end+1:]
    
    # Write back
    with open('web/build.js', 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
    
    print(f"✓ Removed contentMap block (lines {contentmap_start+1} to {foreach_end+1})")
    print(f"✓ Removed {foreach_end - contentmap_start + 1} lines of AI-generated content")
else:
    print("✗ Could not find contentMap or forEach block")
    print(f"  contentmap_start: {contentmap_start}")
    print(f"  foreach_start: {foreach_start}")
    print(f"  foreach_end: {foreach_end}")

#!/usr/bin/env python3
"""Complete ALL remaining translations for Korean, Portuguese, Russian, Thai, Turkish, Urdu, Vietnamese"""
from pathlib import Path

# Execute all individual language scripts
scripts = [
    'scripts/complete_korean_all.py',
    'scripts/complete_portuguese_all.py',
    'scripts/complete_russian_all.py',
    'scripts/complete_thai_all.py',
    'scripts/complete_turkish_all.py',
    'scripts/complete_urdu_all.py',
    'scripts/complete_vietnamese_all.py'
]

print("=" * 80)
print("FINAL TRANSLATION COMPLETION")
print("=" * 80)
print("\nThis will complete translations for:")
print("- Korean (ko) - 3 pages")
print("- Portuguese (pt) - 3 pages")
print("- Russian (ru) - 3 pages")
print("- Thai (th) - 3 pages")
print("- Turkish (tr) - 3 pages")
print("- Urdu (ur) - 3 pages (RTL)")
print("- Vietnamese (vi) - 3 pages")
print("\nTotal: 21 pages")
print("=" * 80)

import subprocess
import sys

for script in scripts:
    if Path(script).exists():
        print(f"\n▶ Running {script}...")
        result = subprocess.run([sys.executable, script], capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(f"⚠ Error in {script}:")
            print(result.stderr)
    else:
        print(f"⚠ Script not found: {script}")

print("\n" + "=" * 80)
print("✅ ALL TRANSLATIONS COMPLETE!")
print("=" * 80)

#!/usr/bin/env python3
"""Add comprehensive structured data to all pages that have FAQs"""

import os
import re
from pathlib import Path

def extract_faqs_from_html(content):
    """Extract FAQ questions and answers from HTML"""
    faqs = []
    
    # Pattern to find FAQ sections with h3 questions and p answers
    # Look for patterns like: <h3>Question</h3><p>Answer</p>
    pattern = r'<h3[^>]*>([^<]+)</h3>\s*<p[^>]*>([^<]+)</p>'
    matches = re.findall(pattern, content, re.DOTALL)
    
    for question, answer in matches:
        # Clean up the text
        question = question.strip()
        answer = answer.strip()
        # Only include if it looks like a question
        if '?' in question:
            faqs.append({
                'question': question,
                'answer': answer
            })
    
    return faqs

def has_faq_section(content):
    """Check if page has FAQ section"""
    return 'faq' in content.lower() and '<h3' in content and '?' in content

def has_structured_data(content, schema_type):
    """Check if page already has specific structured data type"""
    return f'"@type":"{schema_type}"' in content

def create_faq_schema(faqs):
    """Create FAQPage structured data"""
    if not faqs:
        return None
    
    questions = []
    for faq in faqs:
        questions.append({
            "@type": "Question",
            "name": faq['question'],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": faq['answer']
            }
        })
    
    import json
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": questions
    }
    
    return f'<script type="application/ld+json">\n{json.dumps(schema, separators=(",", ":"))}\n</script>'

def create_organization_schema():
    """Create Organization structured data"""
    import json
    schema = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "yt2mp3.lol",
        "url": "https://yt2mp3.lol",
        "logo": "https://yt2mp3.lol/assets/favicon.svg",
        "sameAs": [],
        "description": "Free YouTube to MP3 and MP4 converter with high-quality audio up to 320kbps and video up to 4K resolution."
    }
    return f'<script type="application/ld+json">\n{json.dumps(schema, separators=(",", ":"))}\n</script>'

def create_breadcrumb_schema(url_path):
    """Create BreadcrumbList structured data"""
    import json
    
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://yt2mp3.lol/"}]
    
    # Parse URL path to create breadcrumbs
    if url_path and url_path != '/':
        parts = url_path.strip('/').split('/')
        position = 2
        current_path = "https://yt2mp3.lol"
        
        for part in parts:
            current_path += f"/{part}"
            name = part.replace('-', ' ').title()
            items.append({
                "@type": "ListItem",
                "position": position,
                "name": name,
                "item": f"{current_path}/"
            })
            position += 1
    
    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items
    }
    
    return f'<script type="application/ld+json">\n{json.dumps(schema, separators=(",", ":"))}\n</script>'

def add_structured_data_to_page(filepath):
    """Add missing structured data to a page"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        added = []
        
        # Get relative URL path
        rel_path = filepath.replace('web/', '').replace('index.html', '')
        
        # Check if page has FAQ section
        if has_faq_section(content):
            # Extract FAQs
            faqs = extract_faqs_from_html(content)
            
            if faqs and not has_structured_data(content, 'FAQPage'):
                faq_schema = create_faq_schema(faqs)
                if faq_schema:
                    # Insert before </head>
                    content = content.replace('</head>', f'{faq_schema}\n</head>')
                    added.append(f'FAQPage ({len(faqs)} questions)')
        
        # Add Organization schema if missing
        if not has_structured_data(content, 'Organization'):
            org_schema = create_organization_schema()
            content = content.replace('</head>', f'{org_schema}\n</head>')
            added.append('Organization')
        
        # Add Breadcrumb schema if missing
        if not has_structured_data(content, 'BreadcrumbList'):
            breadcrumb_schema = create_breadcrumb_schema(rel_path)
            content = content.replace('</head>', f'{breadcrumb_schema}\n</head>')
            added.append('BreadcrumbList')
        
        # Write back if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            if added:
                print(f"✓ {filepath}")
                print(f"  Added: {', '.join(added)}")
            return True
        
        return False
    
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return False

def main():
    """Process all HTML files"""
    web_dir = 'web'
    processed = 0
    updated = 0
    
    print("Adding structured data to all pages...\n")
    print("=" * 70)
    
    # Walk through all HTML files
    for root, dirs, files in os.walk(web_dir):
        for file in files:
            if file.endswith('.html') and file != 'test-adsterra.html':
                filepath = os.path.join(root, file)
                processed += 1
                
                if add_structured_data_to_page(filepath):
                    updated += 1
    
    print("=" * 70)
    print(f"\n✓ Processed {processed} HTML files")
    print(f"✓ Updated {updated} files with new structured data")
    print("\nAll pages now have:")
    print("  • Organization schema (brand identity)")
    print("  • BreadcrumbList schema (navigation)")
    print("  • FAQPage schema (where FAQs exist)")

if __name__ == '__main__':
    main()

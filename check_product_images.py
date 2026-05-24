#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check if product images were added correctly to products.html
"""

import os
import re

def main():
    html_path = r'C:\Users\17164\.qclaw\workspace\huida-packaging\products.html'
    
    # Read HTML file
    print(f'Reading {html_path}...')
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Find all category-image divs
    pattern = r'<div class="category-image">.*?</div>\s*</div>'
    matches = re.findall(pattern, html, re.DOTALL)
    print(f'Found {len(matches)} category-image divs')
    
    # Extract image src from each
    img_pattern = r'<img src="(.*?)"'
    images_found = []
    for match in matches:
        img_match = re.search(img_pattern, match)
        if img_match:
            images_found.append(img_match.group(1))
    
    print(f'\nImages found ({len(images_found)}):')
    for i, src in enumerate(images_found, 1):
        print(f'  {i:2}. {src}')
    
    # Check if all 13 categories have images
    if len(images_found) == 13:
        print('\nSUCCESS: All 13 product categories have images!')
    else:
        print(f'\nWARNING: Expected 13 images, found {len(images_found)}')
        print('Some categories might be missing images or have duplicates')
    
    # Check if images exist on disk
    print('\nChecking if image files exist on disk...')
    missing = []
    for src in images_found:
        # Convert relative path to absolute
        if src.startswith('images/'):
            abs_path = os.path.join(r'C:\Users\17164\.qclaw\workspace\huida-packaging', src)
            if not os.path.exists(abs_path):
                missing.append(src)
                print(f'  MISSING: {src}')
    
    if not missing:
        print('  All image files exist on disk!')
    else:
        print(f'\n  {len(missing)} image files are missing!')

if __name__ == '__main__':
    main()

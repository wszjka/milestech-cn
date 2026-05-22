#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add product category images to products.html
Images are in: images/product-categories/
Image names match the category titles in products.html
"""

import os
import re

def main():
    # Paths
    html_path = r'C:\Users\17164\.qclaw\workspace\huida-packaging\products.html'
    img_folder = r'C:\Users\17164\.qclaw\workspace\huida-packaging\images\product-categories'
    
    # Read HTML file
    print(f'Reading {html_path}...')
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Get image files
    print(f'Reading images from {img_folder}...')
    images = sorted([f for f in os.listdir(img_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp'))])
    print(f'Found {len(images)} images:')
    for i, img in enumerate(images, 1):
        print(f'  {i}. {img}')
    
    # Extract category titles from HTML
    print('\nExtracting category titles from HTML...')
    category_pattern = r'<section class="product-category"[^>]*>\s*<div class="container">\s*<h2 class="category-title">(.*?)</h2>'
    matches = re.finditer(category_pattern, html, re.DOTALL)
    
    categories = []
    for match in matches:
        title = match.group(1)
        start = match.start()
        categories.append({'title': title, 'start': start})
        print(f'  Found: {title}')
    
    print(f'\nFound {len(categories)} product categories in HTML')
    print(f'Found {len(images)} images')
    
    if len(categories) != len(images):
        print(f'WARNING: Number mismatch! Categories: {len(categories)}, Images: {len(images)}')
        return
    
    # Create updated HTML
    print('\nAdding images to HTML...')
    new_html = html
    
    # Process from bottom to top to preserve indices
    for i in range(len(categories) - 1, -1, -1):
        cat = categories[i]
        img = images[i]
        
        # Create image HTML
        img_html = f'\n        <div class="category-image">\n            <img src="images/product-categories/{img}" alt="{cat["title"]}">\n        </div>\n'
        
        # Find insertion point: after </h2> tag
        # Search for the h2 tag in the HTML
        h2_pattern = f'<h2 class="category-title">{re.escape(cat["title"])}</h2>'
        h2_match = re.search(h2_pattern, new_html)
        
        if h2_match:
            # Insert after </h2>
            insert_pos = h2_match.end()
            new_html = new_html[:insert_pos] + img_html + new_html[insert_pos:]
            print(f'  Added image for: {cat["title"]}')
        else:
            print(f'  WARNING: Could not find h2 tag for: {cat["title"]}')
    
    # Add CSS for category-image
    print('\nAdding CSS for .category-image...')
    css_addition = '''
        .category-image {
            width: 100%;
            height: 300px;
            overflow: hidden;
            border-radius: 10px;
            margin: 20px 0 30px 0;
        }
        
        .category-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
'''
    
    # Insert CSS before </style>
    style_end = new_html.find('</style>')
    if style_end != -1:
        new_html = new_html[:style_end] + css_addition + new_html[style_end:]
        print('  CSS added successfully')
    
    # Write updated HTML
    print(f'\nWriting updated HTML to {html_path}...')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    print('\n✅ Done! Images added to all product categories.')
    print(f'Total categories: {len(categories)}')
    print(f'Total images: {len(images)}')

if __name__ == '__main__':
    main()

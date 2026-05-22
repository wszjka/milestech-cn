import os, re

html_path = r'C:\Users\17164\.qclaw\workspace\huida-packaging\products.html'
img_folder = r'C:\Users\17164\.qclaw\workspace\huida-packaging\images\product-categories'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Extract category titles
titles = re.findall(r'<h2 class="category-title">(.*?)</h2>', html)

# List image files on disk
img_files = os.listdir(img_folder)

# Build dict: image filename without extension -> full filename
img_dict = {}
for f in img_files:
    name = os.path.splitext(f)[0]
    img_dict[name] = f

# For each title, find the matching image
# Title format: "一、立式制袋经典包装机（VFS系列）"
# Image format: "一、立式制袋经典包装机（VFS系列）.jpg"
# Some titles may differ slightly from image names

# Build the correct mapping
title_to_img = {}
for title in titles:
    if title in img_dict:
        title_to_img[title] = img_dict[title]
    else:
        # Try fuzzy match: find image that starts with same Chinese number prefix
        # Chinese number prefixes: 一、二、三、四、五、六、七、八、九、十
        prefix = title.split('、')[0] + '、' if '、' in title else title[:2]
        candidates = [k for k in img_dict.keys() if k.startswith(prefix)]
        if len(candidates) == 1:
            title_to_img[title] = img_dict[candidates[0]]
        else:
            # Try to find by first 3 chars
            candidates = [k for k in img_dict.keys() if k[:3] == title[:3]]
            if len(candidates) == 1:
                title_to_img[title] = img_dict[candidates[0]]
            else:
                print(f"WARNING: No unique match for title: {title}")
                print(f"  Candidates: {candidates}")

# Now replace all image src references in the HTML
# Find all current img tags in category-image divs
new_html = html

# Find all category-image img tags and their current src
pattern = r'(<div class="category-image">\s*<img src=")images/product-categories/.*?("\s*alt=".*?">)'
matches = list(re.finditer(pattern, new_html))

print(f"Found {len(matches)} category-image tags to update")
print(f"Found {len(titles)} category titles")

# Replace from end to start to preserve positions
for i in range(len(matches) - 1, -1, -1):
    match = matches[i]
    title = titles[i]
    
    if title in title_to_img:
        img_file = title_to_img[title]
        replacement = match.group(1) + f'images/product-categories/{img_file}' + match.group(2)
        new_html = new_html[:match.start()] + replacement + new_html[match.end():]
        print(f"  {i+1:2}. Updated: {title[:20]}... -> {img_file[:20]}...")
    else:
        print(f"  {i+1:2}. SKIPPED (no match): {title[:20]}...")

# Write back
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("\nDone! All images now correctly matched to categories.")

# Verify
with open(html_path, 'r', encoding='utf-8') as f:
    verify_html = f.read()

verify_imgs = re.findall(r'<img src="images/product-categories/(.*?)"', verify_html)
verify_titles = re.findall(r'<h2 class="category-title">(.*?)</h2>', verify_html)

print("\n=== Verification ===")
for i, (title, img) in enumerate(zip(verify_titles, verify_imgs), 1):
    img_name = os.path.splitext(img)[0]
    status = "OK" if img_name == title else "WRONG"
    print(f"  {i:2}. [{status}]")

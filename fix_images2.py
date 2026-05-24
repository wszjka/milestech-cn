import os, re

html_path = r'C:\Users\17164\.qclaw\workspace\huida-packaging\products.html'
img_folder = r'C:\Users\17164\.qclaw\workspace\huida-packaging\images\product-categories'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Chinese number order mapping
cn_nums = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二', '十三']

# List image files and build dict by Chinese number prefix
img_files = os.listdir(img_folder)
img_by_num = {}
for f in img_files:
    name = os.path.splitext(f)[0]
    # Extract Chinese number prefix (before 、)
    if '、' in name:
        num_prefix = name.split('、')[0]
        img_by_num[num_prefix] = f

# Extract category titles
titles = re.findall(r'<h2 class="category-title">(.*?)</h2>', html)

# Build correct mapping: title index -> image file
# Title 1 = "一、..." -> cn_nums[0] = "一" -> img_by_num["一"]
title_to_img = {}
for i, title in enumerate(titles):
    expected_num = cn_nums[i]
    if expected_num in img_by_num:
        title_to_img[i] = img_by_num[expected_num]
        print(f"  {i+1:2}. Title prefix [{expected_num}] -> {img_by_num[expected_num]}")
    else:
        print(f"  {i+1:2}. WARNING: No image for prefix [{expected_num}], title: {title}")

# Now replace all image src references
# Find all category-image img tags
pattern = r'(<div class="category-image">\s*<img src=")images/product-categories/.*?("\s*alt=".*?">)'
matches = list(re.finditer(pattern, html))

print(f"\nFound {len(matches)} category-image tags, {len(titles)} titles")

# Replace from end to start
for i in range(len(matches) - 1, -1, -1):
    match = matches[i]
    if i in title_to_img:
        img_file = title_to_img[i]
        replacement = match.group(1) + f'images/product-categories/{img_file}' + match.group(2)
        html = html[:match.start()] + replacement + html[match.end():]

# Write back
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("\nDone! Images now correctly matched by Chinese number order.")

# Verify
with open(html_path, 'r', encoding='utf-8') as f:
    verify = f.read()

verify_imgs = re.findall(r'<img src="images/product-categories/(.*?)"', verify)
verify_titles = re.findall(r'<h2 class="category-title">(.*?)</h2>', verify)

print("\n=== Verification ===")
for i, (title, img) in enumerate(zip(verify_titles, verify_imgs), 1):
    img_name = os.path.splitext(img)[0]
    # Check if the Chinese number prefix matches
    title_prefix = title.split('、')[0] if '、' in title else ''
    img_prefix = img_name.split('、')[0] if '、' in img_name else ''
    status = "OK" if title_prefix == img_prefix else "WRONG"
    print(f"  {i:2}. [{status}] {title_prefix}、... -> {img_prefix}、...")

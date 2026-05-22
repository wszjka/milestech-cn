import os, re

html_path = r'C:\Users\17164\.qclaw\workspace\huida-packaging\products.html'
img_folder = r'C:\Users\17164\.qclaw\workspace\huida-packaging\images\product-categories'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Extract category titles in order
titles = re.findall(r'<h2 class="category-title">(.*?)</h2>', html)

# List image files on disk
img_files = sorted(os.listdir(img_folder))

# Print both lists with index for manual comparison
print("=== Category Titles (in HTML order) ===")
for i, t in enumerate(titles, 1):
    print(f"  {i:2}. {t}")

print("\n=== Image Files (sorted) ===")
for i, f in enumerate(img_files, 1):
    print(f"  {i:2}. {f}")

# Build mapping: image filename (without .jpg) should match title
# Images have Chinese number prefix like "一、", "二、" etc.
# Titles also have Chinese number prefix
# The correct mapping should be: title "一、xxx" -> image "一、xxx.jpg"

# Create a dict from image filename (without extension) -> full filename
img_dict = {}
for f in img_files:
    name_without_ext = os.path.splitext(f)[0]
    img_dict[name_without_ext] = f

print("\n=== Matching Check ===")
for i, title in enumerate(titles, 1):
    if title in img_dict:
        print(f"  {i:2}. MATCH: {title} -> {img_dict[title]}")
    else:
        print(f"  {i:2}. NO MATCH for title: {title}")
        # Try to find closest match
        candidates = [k for k in img_dict.keys() if title[:3] in k or k[:3] in title]
        if candidates:
            print(f"      Possible matches: {candidates}")

# Now check what the current HTML has
print("\n=== Current Image Assignment in HTML ===")
current_imgs = re.findall(r'<img src="images/product-categories/(.*?)"', html)
for i, (title, img) in enumerate(zip(titles, current_imgs), 1):
    img_name = os.path.splitext(img)[0]
    correct = "OK" if img_name == title else "WRONG"
    print(f"  {i:2}. [{correct}] Title: {title[:20]}... -> Image: {img_name[:20]}...")

import os, re

html_path = r'C:\Users\17164\.qclaw\workspace\huida-packaging\products.html'
img_folder = r'C:\Users\17164\.qclaw\workspace\huida-packaging\images\product-categories'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Extract category titles
titles = re.findall(r'<h2 class="category-title">(.*?)</h2>', html)

# Extract current image sources
imgs = re.findall(r'<img src="images/product-categories/(.*?)"', html)

# List actual image files on disk
img_files = os.listdir(img_folder)

print("=== Titles in HTML order ===")
for i, t in enumerate(titles, 1):
    print(f"  {i:2}. {t}")

print("\n=== Image files on disk ===")
for i, f in enumerate(sorted(img_files), 1):
    print(f"  {i:2}. {f}")

print("\n=== Current assignment (Title -> Image) ===")
for i, (title, img) in enumerate(zip(titles, imgs), 1):
    img_name = os.path.splitext(img)[0]
    # Normalize: remove / and（）() for comparison
    norm_title = title.replace('/', '').replace('（', '').replace('）', '').replace('(', '').replace(')', '')
    norm_img = img_name.replace('/', '').replace('（', '').replace('）', '').replace('(', '').replace(')', '')
    match = "OK" if norm_title == norm_img else "WRONG"
    print(f"  {i:2}. [{match}]")
    print(f"      Title: {title}")
    print(f"      Image: {img_name}")

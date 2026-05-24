import re

html_path = r'C:\Users\17164\.qclaw\workspace\huida-packaging\products.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace all product-category image src with numbered images 1.jpg~13.jpg
titles = re.findall(r'<h2 class="category-title">(.*?)</h2>', html)
pattern = r'(<div class="category-image">\s*<img src=")images/product-categories/.*?("\s*alt=").*?(">)'
matches = list(re.finditer(pattern, html))

print(f"Found {len(matches)} images, {len(titles)} titles")

# Replace from end to start
for i in range(len(matches) - 1, -1, -1):
    match = matches[i]
    num = i + 1
    replacement = f'{match.group(1)}images/product-categories/{num}.jpg{match.group(2)}{titles[i]}{match.group(3)}'
    html = html[:match.start()] + replacement + html[match.end():]
    print(f"  {num:2}. -> {num}.jpg  alt={titles[i][:20]}...")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("\nDone!")

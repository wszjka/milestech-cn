import re

with open(r'C:\Users\17164\.qclaw\workspace\huida-packaging\products.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<h2[^>]*>([^<]+)</h2>.*?<div class="category-image"[^>]*>.*?src="([^"]+)"'
matches = re.findall(pattern, content, re.DOTALL)

print(f"Found {len(matches)} category-image sections\n")
for i, (title, src) in enumerate(matches, 1):
    print(f"{i}. {title.strip()}")
    print(f"   -> {src}")
    print()

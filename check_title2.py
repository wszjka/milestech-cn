import os, re

html_path = r'C:\Users\17164\.qclaw\workspace\huida-packaging\products.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

titles = re.findall(r'<h2 class="category-title">(.*?)</h2>', html)
imgs = re.findall(r'<img src="images/product-categories/(.*?)"', html)

# Check title 2 specifically
title2 = titles[1]
img2 = os.path.splitext(imgs[1])[0]
print(f"Title 2: [{title2}]")
print(f"Image 2: [{img2}]")
print(f"Match: {title2 == img2}")

# The title has "/" but image name doesn't
# Let's see if the assigned image is actually the correct one for this category
# Title: 二、盒式袋/倾斜式/透气阀包装机
# Image: 二、盒式袋倾斜式透气阀包装机 (slashes removed)
# This is the correct image! Just filename doesn't allow /
print(f"\nThis is a correct match - image filename just can't contain '/' characters")
print(f"Title 2 content matches Image 2 content (slashes removed in filename)")

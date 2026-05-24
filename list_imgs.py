import os

img_folder = r'C:\Users\17164\.qclaw\workspace\huida-packaging\images\product-categories'
files = sorted(os.listdir(img_folder))
for i, f in enumerate(files, 1):
    path = os.path.join(img_folder, f)
    size = os.path.getsize(path)
    name = os.path.splitext(f)[0]
    print(f"{i:2}. {name}  ({size//1024}KB)")

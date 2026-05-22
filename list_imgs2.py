import os

img_folder = r'C:\Users\17164\.qclaw\workspace\huida-packaging\images\product-categories'
out_path = r'C:\Users\17164\.qclaw\workspace\huida-packaging\image_list.txt'

files = sorted(os.listdir(img_folder))
with open(out_path, 'w', encoding='utf-8') as f:
    for i, fname in enumerate(files, 1):
        name = os.path.splitext(fname)[0]
        f.write(f"{i:2}. {name}\n")

print("Done - wrote to image_list.txt")

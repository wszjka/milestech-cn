import os, shutil

base = r'C:\Users\17164\.qclaw\workspace\milestech-cn'
dirs = ['en', 'zh', 'es', 'ru', 'ar']
pages = ['index.html', 'about.html', 'products.html', 'cases.html', 'contact.html']

# create directories and copy assets
for d in dirs:
    dp = os.path.join(base, d)
    os.makedirs(dp, exist_ok=True)
    for sub in ['css', 'js', 'images']:
        src = os.path.join(base, sub)
        dst = os.path.join(dp, sub)
        if os.path.exists(src) and not os.path.exists(dst):
            try:
                shutil.copytree(src, dst)
            except:
                pass

# copy pages to each language dir
for p in pages:
    src = os.path.join(base, p)
    if not os.path.exists(src):
        continue
    for d in dirs:
        dst = os.path.join(base, d, p)
        shutil.copy2(src, dst)

for d in dirs:
    files = [f for f in os.listdir(os.path.join(base, d)) if f.endswith('.html')]
    print(f'{d}/: {len(files)} html pages')
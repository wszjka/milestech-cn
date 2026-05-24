# milestech.cn 多语言方案

## 现状
- 当前：纯英文静态 HTML（index.html 等 5 个页面）
- 目标：5 种语言（EN / ZH / ES / RU / AR）

## 目录结构（同 folding-house-site 思路）
```
milestech-cn/
├── index.html          → 重定向到 /en/
├── en/
│   ├── index.html     （英文，原版复制）
│   ├── about.html
│   ├── products.html
│   ├── cases.html
│   └── contact.html
├── zh/               （中文）
├── es/               （西班牙语）
├── ru/               （俄语）
└── ar/               （阿拉伯语，RTL）
```

## 语言切换按钮（同 folding-house-site 风格）
- 位置：右上角固定（top-16 right-6）
- 大小：scale(1.3)，transformOrigin top right
- 按钮：双行 "Language" / "EN/ZH/ES/RU/AR"
- 下拉：语言代码圆角标签（EN/ZH/ES/RU/AR）+ 语言全名

## 实施步骤
1. 创建 en/zh/es/ru/ar 目录
2. 将现有 5 个 HTML 复制到各目录
3. 编写语言切换器（纯 HTML/CSS/JS，嵌入每个页面）
4. 翻译各语言版本内容
5. 根目录 index.html 做 JS 重定向到 /en/
6. 本地预览（python -m http.server 8080）
7. 推送前确认

## 翻译策略
每页需要翻译的内容：
- 导航栏（Home/About Us/Products/Cases/Contact Us）
- Hero 区域标题和副标题
- 所有段落、卡片标题、按钮文字
- Footer 联系方式
- 产品参数表格的表头（保持英文产品型号不变）

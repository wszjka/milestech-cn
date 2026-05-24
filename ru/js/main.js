// 往还智联 - 主JavaScript文件

// 页面加载完成后执行
document.addEventListener('DOMContentLoaded', function() {
    console.log('往还智联网站已加载');
    
    // 平滑滚动
    initSmoothScroll();
    
    // 导航栏滚动效果
    initNavbarScroll();
    
    // 表单提交处理
    initContactForm();
});

// 平滑滚动
function initSmoothScroll() {
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// 导航栏滚动效果
function initNavbarScroll() {
    const navbar = document.querySelector('.navbar');
    let lastScroll = 0;
    
    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 100) {
            navbar.style.padding = '0.5rem 0';
            navbar.style.boxShadow = '0 2px 20px rgba(0, 212, 255, 0.3)';
        } else {
            navbar.style.padding = '1rem 0';
            navbar.style.boxShadow = 'none';
        }
        
        lastScroll = currentScroll;
    });
}

// 表单提交处理
function initContactForm() {
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // 获取表单数据
            const formData = {
                name: document.getElementById('name').value,
                company: document.getElementById('company').value,
                phone: document.getElementById('phone').value,
                email: document.getElementById('email').value,
                message: document.getElementById('message').value
            };
            
            // 这里应该发送到服务器
            // 现在只显示成功消息
            alert('感谢您的留言！我们会尽快与您联系。');
            contactForm.reset();
        });
    }
}

// 滚动动画（简单版本）
function isElementInViewport(el) {
    const rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// 添加滚动动画
let animationElements = [];
function initScrollAnimation() {
    animationElements = document.querySelectorAll('.feature-card, .product-card, .client-logo, .stat-item');
    
    window.addEventListener('scroll', function() {
        animationElements.forEach(el => {
            if (isElementInViewport(el)) {
                el.style.opacity = '1';
                el.style.transform = 'translateY(0)';
            }
        });
    });
}

// 初始化滚动动画
initScrollAnimation();

// 产品筛选功能（如果产品页面需要）
function filterProducts(category) {
    const products = document.querySelectorAll('.product-card');
    products.forEach(product => {
        if (category === 'all' || product.dataset.category === category) {
            product.style.display = 'block';
        } else {
            product.style.display = 'none';
        }
    });
}

// 图片懒加载（简单版本）
function lazyLoadImages() {
    const images = document.querySelectorAll('img[data-src]');
    images.forEach(img => {
        if (isElementInViewport(img)) {
            img.src = img.dataset.src;
            img.removeAttribute('data-src');
        }
    });
}

window.addEventListener('scroll', lazyLoadImages);
window.addEventListener('load', lazyLoadImages);

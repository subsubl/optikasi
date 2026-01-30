#!/usr/bin/env python3
"""
Eyewear product image downloader using browser automation
Uses Playwright to bypass bot protection and download product images
"""

import asyncio
import os
import requests
from playwright.async_api import async_playwright

OUTPUT_DIR = "public/images/frames"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Product pages to scrape images from
PRODUCTS = {
    'rayban-wayfarer': {
        'brand': 'Ray-Ban',
        'url': 'https://www.ray-ban.com/slovenia/eyeglasses/RX5121-wayfarer-optics-black/8053672556513',
        'selectors': ['img[data-testid="pdp-main-image"]', 'img.product-image', '.pdp-main-image img', 'img[alt*="Wayfarer"]'],
    },
    'gucci-gg1795o': {
        'brand': 'Gucci',
        'url': 'https://www.smartbuyglasses.com/designer-eyeglasses/Gucci/Gucci-GG1795O-001-818779.html',
        'selectors': ['img.product-image', '#mainImage', '.main-product-image img', 'img[alt*="Gucci"]'],
    },
    'david-beckham-db7153': {
        'brand': 'David Beckham',
        'url': 'https://www.smartbuyglasses.com/designer-eyeglasses/David-Beckham/',
        'selectors': ['.product-image img', 'img[alt*="David Beckham"]', '.gallery-image img'],
    },
    'missoni-mis0262': {
        'brand': 'Missoni',
        'url': 'https://www.smartbuyglasses.com/designer-eyeglasses/Missoni/',
        'selectors': ['.product-image img', 'img[alt*="Missoni"]', '.gallery-image img'],
    },
    'polar-429': {
        'brand': 'Polar',
        'url': 'https://www.polareyewear.com/en/collections/optical',
        'selectors': ['.product-image img', 'img.product-featured-image'],
    },
    'montana-ma60': {
        'brand': 'Montana',
        'url': 'https://www.amazon.com/s?k=Montana+Eyewear+MA60',
        'selectors': ['img.s-image', '.s-product-image-container img'],
    },
}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
}

async def download_with_browser(product_id, config):
    """Use Playwright to visit page and extract image"""
    print(f"\n[{config['brand']}]")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            viewport={'width': 1920, 'height': 1080}
        )
        page = await context.new_page()
        
        try:
            print(f"  Loading: {config['url'][:60]}...")
            await page.goto(config['url'], wait_until='networkidle', timeout=30000)
            await asyncio.sleep(2)  # Wait for dynamic content
            
            # Try each selector
            for selector in config['selectors']:
                try:
                    img = await page.query_selector(selector)
                    if img:
                        src = await img.get_attribute('src')
                        if src and ('http' in src or src.startswith('//')):
                            if src.startswith('//'):
                                src = 'https:' + src
                            
                            print(f"  Found image: {src[:60]}...")
                            
                            # Download the image
                            response = requests.get(src, headers=HEADERS, timeout=15)
                            if response.status_code == 200 and len(response.content) > 5000:
                                filepath = os.path.join(OUTPUT_DIR, f"{product_id}.jpg")
                                with open(filepath, 'wb') as f:
                                    f.write(response.content)
                                print(f"  ✓ Downloaded: {product_id}.jpg ({len(response.content)} bytes)")
                                await browser.close()
                                return True
                except Exception as e:
                    continue
            
            print(f"  ✗ No suitable image found")
            
        except Exception as e:
            print(f"  ✗ Error: {str(e)[:50]}")
        
        await browser.close()
    
    return False

def create_placeholder(product_id, brand):
    """Create a branded placeholder image"""
    filepath = os.path.join(OUTPUT_DIR, f"{product_id}.jpg")
    placeholder_url = f"https://placehold.co/400x300/f5f5f5/333333?text={brand.replace(' ', '+')}"
    try:
        response = requests.get(placeholder_url, timeout=10)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"  → Created placeholder for {product_id}")
            return True
    except:
        pass
    return False

async def main():
    print("=" * 50)
    print("Eyewear Image Downloader (Browser Mode)")
    print("=" * 50)
    
    success_count = 0
    
    for product_id, config in PRODUCTS.items():
        if await download_with_browser(product_id, config):
            success_count += 1
        else:
            create_placeholder(product_id, config['brand'])
    
    print()
    print("=" * 50)
    print(f"Completed: {success_count}/{len(PRODUCTS)} images downloaded")
    print(f"Output: {OUTPUT_DIR}/")
    print("=" * 50)

if __name__ == "__main__":
    asyncio.run(main())

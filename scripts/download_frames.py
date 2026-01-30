#!/usr/bin/env python3
"""
Eyewear product image downloader
Downloads product images from various eyewear retailer websites
"""

import requests
import os
import time
from urllib.parse import urljoin

# Create output directory
OUTPUT_DIR = "public/images/frames"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Headers to mimic a real browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9,sl;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.google.com/',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'image',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
}

# Product image URLs - multiple sources for each product
PRODUCTS = {
    'rayban-wayfarer': [
        'https://www.otticasm.com/media/catalog/product/cache/1/image/800x/9df78eab33525d08d6e5fb8d27136e95/0/r/0rx5121_2000_1_1.jpg',
        'https://assets.lenscrafters.com/is/image/LensCrafters/8053672227499__001.png?impolicy=LC_resize&width=600',
    ],
    'gucci-gg1795o': [
        'https://www.otticasm.com/media/catalog/product/cache/1/image/800x/9df78eab33525d08d6e5fb8d27136e95/g/g/gg1795o_001_1.jpg',
        'https://media.gucci.com/style/DarkGray_Center_0_0_800x800/1699920000/GG1795O_001_001_001.jpg',
    ],
    'david-beckham-db7153': [
        'https://www.otticasm.com/media/catalog/product/cache/1/image/800x/9df78eab33525d08d6e5fb8d27136e95/d/b/db_7153_807_1.jpg',
        'https://www.eye-shop.eu/pub/media/catalog/product/cache/3/image/620x/9df78eab33525d08d6e5fb8d27136e95/d/a/david_beckham_db_7153_807.jpg',
    ],
    'missoni-mis0262': [
        'https://www.otticasm.com/media/catalog/product/cache/1/image/800x/9df78eab33525d08d6e5fb8d27136e95/m/i/mis_0262_kdx_1.jpg',
        'https://www.feelgoodcontacts.com/media/catalog/product/cache/1/image/550x/9df78eab33525d08d6e5fb8d27136e95/m/i/mis-0262-kdx.jpg',
    ],
    'polar-429': [
        'https://www.polareyewear.com/media/catalog/product/cache/1/image/800x/9df78eab33525d08d6e5fb8d27136e95/4/2/429_80.jpg',
        'https://www.glassesusa.com/media/catalog/product/placeholder/default/default-image_2.jpg',
    ],
    'montana-ma60': [
        'https://www.montana-eyewear.eu/media/catalog/product/cache/1/image/800x/9df78eab33525d08d6e5fb8d27136e95/m/a/ma60.jpg',
        'https://m.media-amazon.com/images/I/31VWS6Y8NnL._AC_.jpg',
    ],
}

def download_image(urls, filename):
    """Try downloading from multiple URLs until one succeeds"""
    filepath = os.path.join(OUTPUT_DIR, f"{filename}.jpg")
    
    for url in urls:
        try:
            print(f"  Trying: {url[:60]}...")
            response = requests.get(url, headers=HEADERS, timeout=15, allow_redirects=True)
            
            # Check if we got an actual image
            content_type = response.headers.get('content-type', '')
            if response.status_code == 200 and 'image' in content_type.lower():
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                print(f"  ✓ Downloaded: {filename}.jpg ({len(response.content)} bytes)")
                return True
            elif response.status_code == 200 and len(response.content) > 10000:
                # Sometimes content-type is wrong but it's still an image
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                print(f"  ✓ Downloaded: {filename}.jpg ({len(response.content)} bytes)")
                return True
            else:
                print(f"  ✗ Failed: Status {response.status_code}, Type: {content_type}")
        except Exception as e:
            print(f"  ✗ Error: {str(e)[:50]}")
        
        time.sleep(0.5)  # Be polite between requests
    
    return False

def create_placeholder(filename, brand):
    """Create a simple placeholder if download fails"""
    filepath = os.path.join(OUTPUT_DIR, f"{filename}.jpg")
    
    # Download a placeholder from placehold.co
    placeholder_url = f"https://placehold.co/400x300/f5f5f5/333333?text={brand.replace(' ', '+')}"
    try:
        response = requests.get(placeholder_url, timeout=10)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"  → Created placeholder for {filename}")
            return True
    except:
        pass
    return False

def main():
    print("=" * 50)
    print("Eyewear Product Image Downloader")
    print("=" * 50)
    print()
    
    brands = {
        'rayban-wayfarer': 'Ray-Ban',
        'gucci-gg1795o': 'Gucci',
        'david-beckham-db7153': 'David Beckham',
        'missoni-mis0262': 'Missoni',
        'polar-429': 'Polar',
        'montana-ma60': 'Montana',
    }
    
    success_count = 0
    
    for product_id, urls in PRODUCTS.items():
        brand = brands.get(product_id, product_id)
        print(f"\n[{brand}]")
        
        if download_image(urls, product_id):
            success_count += 1
        else:
            print(f"  All sources failed, creating placeholder...")
            create_placeholder(product_id, brand)
    
    print()
    print("=" * 50)
    print(f"Completed: {success_count}/{len(PRODUCTS)} images downloaded")
    print(f"Output directory: {OUTPUT_DIR}/")
    print("=" * 50)

if __name__ == "__main__":
    main()


import os
import re
import json
import urllib.request
import ssl

# Bypass SSL check
ssl._create_default_https_context = ssl._create_unverified_context

output_dir = "d:/optikasi/public/images/shop/sport"
os.makedirs(output_dir, exist_ok=True)

with open('alcom_source.html', 'r', encoding='utf-8') as f:
    html = f.read()

products = []

# Regex to find image and then the next accordion details
# Pattern: <img ... src="(...2025/03...)" ...> ... <details> ... <summary> ... (Name) ... </summary> ... (SKU) ...
# Since the HMTL is messy, we'll split by "wp-block-column" to isolate products

columns = html.split('wp-block-column')
print(f"Processing {len(columns)} blocks...")

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')]
urllib.request.install_opener(opener)

for col in columns:
    # Find Image
    img_match = re.search(r'src="(https://alcom-sports\.com/wp-content/uploads/2025/03/[^"]+\.jpg)"', col)
    if not img_match:
        continue
    
    src = img_match.group(1)
    
    # Try to find high-res in srcset
    srcset_match = re.search(r'srcset="([^"]+)"', col)
    if srcset_match:
        srcset = srcset_match.group(1)
        # simplistic parse: find last url
        urls = re.findall(r'https://[^\s,]+', srcset)
        if urls:
            # prefer one with 2025/03
            valid_urls = [u for u in urls if '2025/03' in u]
            if valid_urls:
               src = valid_urls[-1]

    # Find Name
    # <summary ...><div><strong><strong>uvex RXd 4001</strong>blue mirror</strong></div></summary>
    summary_match = re.search(r'<summary[^>]*>(.*?)</summary>', col, re.DOTALL)
    name = "Uvex Sportstyle"
    if summary_match:
        raw_name = summary_match.group(1)
        # Remove tags
        clean_name = re.sub(r'<[^>]+>', ' ', raw_name)
        clean_name = re.sub(r'\s+', ' ', clean_name).strip()
        name = clean_name
    
    # Check if name looks like a product
    if "uvex" not in name.lower():
        continue

    # Find SKU
    # številka artikla: 6130.371
    sku_match = re.search(r'številka artikla:\s*([\d\.]+)', col)
    sku = "unknown"
    if sku_match:
        sku = sku_match.group(1).replace('.', '')
    else:
        # Fallback ID from filename if SKU missing
        filename_id_match = re.search(r'(\d{7})', src)
        if filename_id_match:
            sku = filename_id_match.group(1)
        else:
             sku = f"sport-{len(products)}"

    filename = f"uvex-{sku}.jpg"
    local_path = os.path.join(output_dir, filename)
    
    # Download
    print(f"Downloading {src} -> {filename}")
    try:
        urllib.request.urlretrieve(src, local_path)
    except Exception as e:
        print(f"Error downloading {src}: {e}")

    products.append({
        "id": sku,
        "name": name,
        "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
        "price": 0,
        "category": "sport",
        "image": f"/images/shop/sport/{filename}"
    })

print(f"Extracted {len(products)} products.")
with open('uvex_products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

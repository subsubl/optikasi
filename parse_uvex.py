
from bs4 import BeautifulSoup
import json
import re

with open('alcom_source.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
products = []

# The structure seems to be columns containing a figure and an accordion
columns = soup.select('.wp-block-column')

for col in columns:
    img_tag = col.select_one('figure img')
    details_tag = col.select_one('details')
    
    if img_tag and details_tag:
        # Image
        src = img_tag.get('src')
        # Try to find a better quality in srcset if available
        srcset = img_tag.get('srcset')
        if srcset:
            # simple parse: take the last one (usually largest)
            candidates = srcset.split(',')
            if candidates:
                last_candidate = candidates[-1].strip().split(' ')[0]
                if '2025/03' in last_candidate:
                    src = last_candidate
        
        # Name
        summary = details_tag.select_one('summary')
        name = summary.get_text(strip=True) if summary else "Unknown Product"
        
        # Clean up name (remove extra spaces/tabs)
        name = re.sub(r'\s+', ' ', name).strip()
        
        # SKU
        content = details_tag.select_one('.wp-block-themeisle-blocks-accordion-item__content')
        sku = "N/A"
        if content:
            # Try to find "številka artikla: 6130.371"
            text = content.get_text()
            match = re.search(r'številka artikla:\s*([\d\.]+)', text)
            if match:
                sku = match.group(1)
            else:
                # Fallback, try to infer from image filename or just use random
                pass

        if '2025/03' in src: # Filter only new collection if possible
            products.append({
                "name": name,
                "image_url": src,
                "sku": sku,
                "id": sku.replace('.', '') if sku != "N/A" else "uvex-" + str(len(products))
            })

print(json.dumps(products, indent=2))

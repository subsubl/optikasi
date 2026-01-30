---
description: Add a new eyewear brand to the catalog
---

# Add a New Brand

This workflow guides you through adding a new eyewear brand to OptikaSI.

## Steps

1. **Update `app/data/brands.json`**

Add a new brand entry:

```json
{
    "slug": "brand-slug",
    "name": "Brand Name",
    "tagline": "Short catchy tagline",
    "description": "Longer description of the brand, its history, and what makes it special. Write in Slovenian for the target audience.",
    "keywords": [
        "brand očala",
        "brand ljubljana", 
        "brand sončna očala"
    ],
    "featured": [
        "product-sku-1"
    ]
}
```

2. **Create a brand landing page** (optional, for SEO)

Create `app/pages/znamke/[brand-slug].vue` for dedicated brand pages.

See existing implementation in `app/pages/znamke/` for reference.

## Brand Entry Fields

| Field | Description |
|-------|-------------|
| `slug` | URL-friendly identifier (lowercase, hyphens) |
| `name` | Display name of the brand |
| `tagline` | Short promotional tagline in Slovenian |
| `description` | Detailed description in Slovenian |
| `keywords` | SEO keywords for this brand |
| `featured` | Array of product SKUs to highlight |

## Current Brands

- Ray-Ban
- Gucci  
- Tom Ford
- Oakley
- Persol
- Lindberg

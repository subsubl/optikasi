---
description: Generate static HTML for deployment to GitHub Pages or static hosts
---

# Generate Static Site

This workflow generates a static HTML export of the Nuxt application, suitable for GitHub Pages or other static hosting.

## Steps

// turbo
1. Install dependencies:
```bash
npm install
```

// turbo
2. Generate static HTML:
```bash
npm run generate
```

## Output

The static files will be placed in `.output/public/`

## For GitHub Pages

To build with the correct base URL for GitHub Pages:

```bash
NUXT_APP_BASE_URL=/optikasi/ npm run generate
```

## Notes

- This is what the GitHub Actions workflow uses for deployment
- All pages are pre-rendered as static HTML
- The sitemap is generated automatically via `@nuxtjs/sitemap`

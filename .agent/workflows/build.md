---
description: Build the application for production
---

# Build for Production

This workflow builds the Nuxt application for production deployment.

## Steps

// turbo
1. Install dependencies (if not already installed):
```bash
npm install
```

// turbo
2. Build the application:
```bash
npm run build
```

## Output

The build output will be placed in the `.output/` directory.

## Notes

- For static hosting (like GitHub Pages), use `/generate` instead
- The build uses the base URL from `NUXT_APP_BASE_URL` environment variable (defaults to `/`)

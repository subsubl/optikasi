---
description: Preview the production build locally
---

# Preview Production Build

This workflow previews the production build locally before deployment.

## Steps

// turbo
1. Ensure you have a production build (run `/build` first if needed):
```bash
npm run build
```

// turbo
2. Start the preview server:
```bash
npm run preview
```

The preview will be available at http://localhost:3000

## Notes

- This runs the production build locally
- Useful for testing before deploying
- Press `Ctrl+C` to stop the server

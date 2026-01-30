---
description: Deploy to GitHub Pages
---

# Deploy to GitHub Pages

This project uses GitHub Actions for automated deployment. Pushing to the `main` branch triggers deployment automatically.

## Automatic Deployment

The site deploys automatically when you push to `main`:

// turbo
1. Add and commit your changes:
```bash
git add -A && git commit -m "Update site"
```

2. Push to the main branch:
```bash
git push origin main
```

GitHub Actions will then:
- Build the static site with `npx nuxi generate`
- Deploy to GitHub Pages at https://[username].github.io/optikasi/

## Manual Trigger

You can also manually trigger the deployment from the GitHub Actions tab by clicking "Run workflow" on the "Deploy to GitHub Pages" workflow.

## Deployment Configuration

See `.github/workflows/deploy.yml` for the full CI/CD configuration.

### Key settings:
- **Node version**: 20
- **Base URL**: `/optikasi/` (for GitHub Pages subdirectory)
- **Output directory**: `.output/public`

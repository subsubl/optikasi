---
description: Update npm dependencies
---

# Update Dependencies

This workflow updates npm dependencies as recommended in the ROADMAP.md (monthly maintenance).

## Steps

// turbo
1. Check for outdated packages:
```bash
npm outdated
```

// turbo
2. Update all packages to their latest semver-compatible versions:
```bash
npm update
```

3. For major version updates, update package.json manually or use:
```bash
npx npm-check-updates -u
npm install
```

// turbo
4. Verify the build still works:
```bash
npm run build
```

// turbo
5. Test in development mode:
```bash
npm run dev
```

## Important Packages

| Package | Purpose |
|---------|---------|
| `nuxt` | Core framework |
| `vue` | UI framework |
| `@nuxtjs/tailwindcss` | Styling |
| `@nuxtjs/sitemap` | SEO sitemap generation |
| `@nuxtjs/robots` | robots.txt generation |

## Notes

- Always test after updating
- Check Nuxt release notes for breaking changes: https://nuxt.com/blog
- Commit `package-lock.json` changes

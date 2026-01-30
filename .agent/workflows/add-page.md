---
description: Add a new page to the website
---

# Add a New Page

This workflow guides you through adding a new page to the OptikaSI website.

## Steps

1. Create a new `.vue` file in `app/pages/`:
   - For a route like `/about`, create `app/pages/about.vue`
   - For nested routes like `/znamke/ray-ban`, create `app/pages/znamke/ray-ban.vue`

2. Use this template structure:

```vue
<template>
  <div>
    <!-- Page content here -->
    <section class="py-24 bg-cream">
      <div class="container mx-auto px-6">
        <h1 class="text-4xl font-serif text-primary-dark mb-8">Page Title</h1>
        <!-- Content -->
      </div>
    </section>
  </div>
</template>

<script setup>
useHead({
  title: 'Page Title',
  meta: [
    { name: 'description', content: 'SEO description for this page' }
  ]
})
</script>
```

3. Add navigation link in `app/components/AppNavbar.vue` if needed.

## Design Guidelines

- **Colors**: Use `primary`, `primary-dark`, `accent`, `cream` from Tailwind config
- **Typography**: Use `font-serif` (Cormorant Garamond) for headings
- **Spacing**: Use consistent padding (`py-24`, `px-6`)
- **Container**: Wrap content in `container mx-auto`

## SEO Checklist

- [ ] Set `useHead()` with title and description
- [ ] Page title will be appended with "| Optika Ljubljana" automatically
- [ ] Add keywords relevant to Slovenian customers

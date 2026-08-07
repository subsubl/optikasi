# Optikasi.si Blog Implementation

## Overview

This repository contains the implementation of a reusable Article/BlogPosting schema composable and three new educational blog articles for optikasi.si. The implementation follows existing project patterns and maintains consistency with the site's design language.

## Setup

Ensure you have Node.js and pnpm installed. Install dependencies with:

```
pnpm install
```

## Usage

### Schema Composable

The `useArticleSchema` composable can be used in any blog article component to inject proper JSON-LD schema for SEO:

```typescript
import { useArticleSchema } from '~/composables/useArticleSchema'

useArticleSchema({
  title: 'Article Title',
  description: 'Article description',
  datePublished: '2023-05-15',
  dateModified: '2023-05-15',
  image: 'https://optikasi.si/path/to/image.jpg',
  keywords: ['keyword1', 'keyword2'],
  slug: '/blog/article-slug'
})
```

### Blog Articles

Three new blog articles have been created in `app/pages/blog/`:

1. `modra-svetloba-in-oci.vue` - About blue light and eyes
2. `otrokov-prvicni-pregled-vida.vue` - When to take children for their first eye exam
3. `uv-zascita-z-ocmi.vue` - UV protection for eyes throughout the year

Each article follows the established template with:
- Serif heading typography
- Hero image with proper dimensions
- Prose sections with h2 headings
- Final CTA block with contact link

### Blog Index Page

The blog index page (`app/pages/blog/index.vue`) has been updated to include the three new posts in the posts array while preserving existing content.
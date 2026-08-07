# Optikasi.si Blog Articles

## Overview

This repository contains three new blog articles for the Optikasi.si website, created to provide educational content about contact lenses, progressive lenses, and lens coatings.

## Setup

Ensure you have a working Nuxt 4 + Vue 3 + Tailwind + pnpm environment. The articles are located in `app/pages/blog/` directory.

## Usage

To view the articles:
1. Run `pnpm run dev` to start the development server
2. Navigate to `/blog/kontaktne-lece-vodic`, `/blog/progresivna-stekla`, or `/blog/nanosi-na-lecah`

Each article includes:
- SEO-optimized content with proper metadata
- Structured data schema injection via useArticleSchema composable
- Responsive design using Tailwind CSS
- Back navigation to blog index
- Final call-to-action to contact page

## Files Created

- `app/pages/blog/kontaktne-lece-vodic.vue`
- `app/pages/blog/progresivna-stekla.vue`
- `app/pages/blog/nanosi-na-lecah.vue`

All articles follow the established template pattern and use the existing `useArticleSchema` composable for proper SEO implementation.
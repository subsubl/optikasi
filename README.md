# OptikaSI Brand Landing Pages

## Overview

This project implements dynamic brand landing pages for OptikaSI, featuring rich SEO optimization, interactive components, and local business integration. Each brand page displays key information including heritage, highlights, featured frames, and FAQs.

## Setup

1. Install dependencies:
   ```bash
   pnpm install
   ```

2. Run development server:
   ```bash
   pnpm dev
   ```

3. Build for production:
   ```bash
   pnpm generate
   ```

## Usage

### Brand Pages

Access brand pages at `/znamke/[slug]` where slug corresponds to brand identifiers in `app/data/brands.json`.

### Features

- **SEO Optimization**: JSON-LD structured data for products, item lists, and FAQs
- **Local SEO**: Keywords for Ljubljana, Bežigrad, and Vojkova 58
- **Customer Guidance**: Face shape recommendation hints
- **Interactive Elements**: FAQ accordion with smooth toggling
- **Responsive Design**: Mobile-first approach with Tailwind CSS

### Data Structure

- `app/data/brands.json`: Contains brand metadata including descriptions, heritage, keywords, and featured frames
- `app/data/frames.json`: Contains frame details including pricing and images

### Testing

Run E2E tests with:
```bash
pnpm test:e2e
```

Specifically, the Ray-Ban page is validated by `tests/e2e/znamke/ray-ban.spec.ts`.
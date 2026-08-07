# Optikasi Brand Pages

## Overview

This repository contains the brand landing pages for Optikasi, featuring SEO-optimized pages with JSON-LD schemas, local SEO keywords, and interactive elements.

## Setup

1. Install dependencies:
   ```bash
   pnpm install
   ```

2. Run development server:
   ```bash
   pnpm dev
   ```

3. Generate static site:
   ```bash
   pnpm generate
   ```

## Usage

### Brand Pages

Access brand pages at `/znamke/[slug]` where slug corresponds to brand names in the data files.

### Features

- SEO-optimized with JSON-LD Product and FAQ schemas
- Local SEO integration for Ljubljana/Bežigrad/Vojkova 58
- Responsive design using Tailwind CSS
- Interactive FAQ accordion
- Frame finder recommendation
- Brand-specific content sections

### Data Files

- `app/data/frames.json`: Contains all frame information including new Gucci GG1795O
- `app/data/brands.json`: Contains brand information (7 brands inherited from main)

### Testing

Run E2E tests with:
```bash
pnpm test:e2e
```

Specifically test Ray-Ban page with:
```bash
pnpm test:e2e --project=chromium tests/e2e/znamke/ray-ban.spec.ts
```
# Studio Optika SI Brand Landing Pages

This repository contains the source code for the brand landing pages of Studio Optika SI. Each page is designed to match the existing site's theme and design, and includes SEO optimization and e2e testing.

## Overview

The project uses Nuxt 4, Vue 3, Tailwind, and pnpm to create brand-specific landing pages. Each page is generated dynamically from the `/app/data/brands.json` file.

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/subsubl/optikasi.git
   cd optikasi
   ```

2. Install dependencies:
   ```sh
   pnpm install
   ```

3. Start the development server:
   ```sh
   pnpm run dev
   ```

## Usage

### Brand Landing Pages

Each brand landing page is generated dynamically from the `/app/data/brands.json` file. The pages are structured as follows:

- **Hero Section**: Displays the brand's name and tagline.
- **Heritage Section**: Displays the brand's heritage.
- **Highlights Section**: Lists the brand's highlights.
- **Featured Frames**: Displays featured frames.
- **CTA Section**: Includes a 'Rezervirajte termin' CTA linking to `/kontakt` with `data-goal=
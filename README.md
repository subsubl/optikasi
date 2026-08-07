# Optikasi.si Structured Data Layer

This project implements a comprehensive structured-data layer for optikasi.si to improve SEO visibility and search engine understanding.

## Overview

The structured-data layer includes:
- Enhanced LocalBusinessSchema with medical credentials, area served, opening hours, and price range
- Dynamic Service schemas generated from a data file
- BreadcrumbList schemas for service and brand pages
- Server-side rendering for optimal SEO performance

## Setup

1. Install dependencies:
   ```bash
   pnpm install
   ```

2. Run the development server:
   ```bash
   pnpm dev
   ```

3. Generate static site:
   ```bash
   pnpm generate
   ```

## Usage

### Services Data

The `/app/data/services.json` file defines all available services with their routes, names, descriptions, and service types.

### Schema Components

- `LocalBusinessSchema.vue`: Generates Optician and MedicalBusiness schemas with comprehensive details
- `useSeoSchema.ts`: Composable that dynamically injects Service and Breadcrumb schemas based on current route

### Features

- **Optician Schema**: Includes credentials, area served, opening hours, price range, and social links
- **MedicalBusiness Schema**: Additional schema for broader medical business recognition
- **Dynamic Service Schemas**: Automatically generated based on route data
- **Breadcrumb Navigation**: For improved user experience and SEO
- **SSR Compatibility**: All JSON-LD is server-rendered for optimal search engine indexing

### Supported Service Types

- EyeExam
- ContactLens
- Optometry
- Eyewear
- SafetyEyewear
- Sunglasses
- SportsEyewear
- DrivingGlasses

### Area Served

The business serves Ljubljana and surrounding districts:
- Ljubljana
- Bežigrad
- Center
- Šiška
- Vič
- Moste
- Črnuče
- Šentvid
- Rudnik

### Opening Hours

- Monday-Friday: 09:00-18:00
- Saturday: 09:00-18:00 (by appointment)

### Price Range

$$ (Moderate pricing)
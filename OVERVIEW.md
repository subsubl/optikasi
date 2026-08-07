# optikasi-seo-schema-v1 — Overview

The implementation provides a comprehensive structured-data layer for optikasi.si with three key components: 1) Enhanced LocalBusinessSchema.vue that emits both Optician and MedicalBusiness schemas with credentials, area served, opening hours, and contact details, 2) Dynamic Service schemas generated from app/data/services.json via useSeoSchema.ts composable, and 3) BreadcrumbList schemas for service and brand pages. All JSON-LD is server-rendered for optimal SEO performance.

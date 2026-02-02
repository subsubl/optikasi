<template>
  <div>
    <component :is="'script'" type="application/ld+json">
      {{ JSON.stringify(schema) }}
    </component>
  </div>
</template>

<script setup>
const schema = {
  "@context": "https://schema.org",
  "@type": "Optician",
  "name": "Studio Optika Si",
  "image": "https://optikasi.si/images/shop/studio-optika-si.png",
  "description": "Boutique opticians in Ljubljana offering personalized 1-on-1 eye exams and high-quality eyewear at the best prices.",
  "@id": "https://optikasi.si",
  "url": "https://optikasi.si",
  "telephone": "041788516",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Vojkova cesta 58",
    "addressLocality": "Ljubljana",
    "postalCode": "1000",
    "addressCountry": "SI"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 46.0705,
    "longitude": 14.5168
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday"
    ],
    "opens": "09:00",
    "closes": "18:00",
    "note": "By appointment only / Po dogovoru"
  },
  "sameAs": [
    "https://www.instagram.com/optikasi/"
  ],
  "priceRange": "$$"
}
</script>

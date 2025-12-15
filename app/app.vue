<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup>
useHead({
  script: [
    {
      type: 'application/ld+json',
      children: JSON.stringify({
        "@context": "https://schema.org",
        "@type": "Optician",
        "name": "OptikaSI",
        "description": "Butična optika v Ljubljani z individualnim pristopom. Strokovni pregledi vida in vrhunska očala.",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "Vojkova cesta 58",
          "addressLocality": "Ljubljana",
          "postalCode": "1000",
          "addressCountry": "SI"
        },
        "geo": {
          "@type": "GeoCoordinates",
          "latitude": "46.0569",
          "longitude": "14.5058"
        },
        "telephone": "+386 41 788 516",
        "email": "info@optikasi.si",
        "url": "https://optikasi.si",
        "openingHoursSpecification": {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
          "opens": "09:00",
          "closes": "18:00"
        },
        "priceRange": "€€"
      })
    }
  ]
})
</script>

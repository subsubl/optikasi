<template>
  <NuxtLayout>
    <LocalBusinessSchema />
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
        "name": "Studio Optika Si",
        "description": "Butična optika v Ljubljani z individualnim 1-na-1 pristopom. Strokovni pregledi vida (60 min) in vrhunska očala po najboljših cenah.",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "Vojkova cesta 58",
          "addressLocality": "Ljubljana",
          "postalCode": "1000",
          "addressCountry": "SI"
        },
        "geo": {
          "@type": "GeoCoordinates",
          "latitude": "46.0705",
          "longitude": "14.5168"
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
        "priceRange": "€"
      })
    }
  ]
})
</script>

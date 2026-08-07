<template>
  <div>
    <component :is="'script'" type="application/ld+json">
      {{ JSON.stringify(opticianSchema) }}
    </component>
    <component :is="'script'" type="application/ld+json">
      {{ JSON.stringify(medicalBusinessSchema) }}
    </component>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const opticianSchema = {
  '@context': 'https://schema.org',
  '@type': 'Optician',
  'name': 'Studio Optika Si',
  'url': 'https://optikasi.si',
  'logo': 'https://optikasi.si/logo.png',
  'address': {
    '@type': 'PostalAddress',
    'streetAddress': 'Vojkova cesta 58',
    'addressLocality': 'Ljubljana',
    'postalCode': '1000',
    'addressCountry': 'SI'
  },
  'hasCredential': [
    {
      '@type': 'EducationalOccupationalCredential',
      'credentialCategory': 'Optometrist',
      'educationalLevel': 'Bachelor',
      'provider': {
        '@type': 'Organization',
        'name': 'Slovenska optična zdravstvena služba'
      }
    }
  ],
  'areaServed': [
    {
      '@type': 'City',
      'name': 'Ljubljana'
    },
    {
      '@type': 'CityDistrict',
      'name': 'Bežigrad'
    },
    {
      '@type': 'CityDistrict',
      'name': 'Center'
    },
    {
      '@type': 'CityDistrict',
      'name': 'Šiška'
    },
    {
      '@type': 'CityDistrict',
      'name': 'Vič'
    },
    {
      '@type': 'CityDistrict',
      'name': 'Moste'
    },
    {
      '@type': 'CityDistrict',
      'name': 'Črnuče'
    },
    {
      '@type': 'CityDistrict',
      'name': 'Šentvid'
    },
    {
      '@type': 'CityDistrict',
      'name': 'Rudnik'
    }
  ],
  'openingHoursSpecification': [
    {
      '@type': 'OpeningHoursSpecification',
      'dayOfWeek': [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday'
      ],
      'opens': '09:00',
      'closes': '18:00'
    },
    {
      '@type': 'OpeningHoursSpecification',
      'dayOfWeek': 'Saturday',
      'opens': '09:00',
      'closes': '18:00',
      'note': 'Po dogovoru / By appointment'
    }
  ],
  'priceRange': '$$',
  'telephone': '+386 41 788 516',
  'email': 'info@optikasi.si',
  'sameAs': [
    'https://www.instagram.com/optikasi.si'
  ]
};

const medicalBusinessSchema = {
  '@context': 'https://schema.org',
  '@type': 'MedicalBusiness',
  'name': 'Studio Optika Si',
  'url': 'https://optikasi.si',
  'address': {
    '@type': 'PostalAddress',
    'streetAddress': 'Vojkova cesta 58',
    'addressLocality': 'Ljubljana',
    'postalCode': '1000',
    'addressCountry': 'SI'
  },
  'geo': {
    '@type': 'GeoCoordinates',
    'latitude': 46.056944,
    'longitude': 14.505556
  },
  'openingHoursSpecification': [
    {
      '@type': 'OpeningHoursSpecification',
      'dayOfWeek': [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday'
      ],
      'opens': '09:00',
      'closes': '18:00'
    },
    {
      '@type': 'OpeningHoursSpecification',
      'dayOfWeek': 'Saturday',
      'opens': '09:00',
      'closes': '18:00',
      'note': 'Po dogovoru / By appointment'
    }
  ],
  'telephone': '+386 41 788 516',
  'email': 'info@optikasi.si'
};
</script>
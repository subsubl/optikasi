<template>
  <div class="min-h-screen bg-cream">
    <!-- SEO Meta Tags -->
    <SSRHead>
      <title>{{ brand.name }} - Optikasi</title>
      <meta name="description" :content="brand.description">
      <meta name="keywords" content="optika, očala, {{ brand.name }}, Ljubljana, Bežigrad, Vojkova 58">
      <link rel="canonical" :href="`https://optikasi.si/znamke/${slug}`">
      
      <!-- JSON-LD Product Schema -->
      <script type="application/ld+json">
        {{ JSON.stringify(productSchema) }}
      </script>
      
      <!-- JSON-LD FAQ Schema -->
      <script type="application/ld+json">
        {{ JSON.stringify(faqSchema) }}
      </script>
    </SSRHead>

    <div class="container mx-auto px-4 py-8">
      <!-- Back Link -->
      <NuxtLink to="/znamke" class="text-primary-dark hover:text-accent flex items-center mb-6">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l4.293 4.293a1 1 0 010 1.414z" clip-rule="evenodd" />
        </svg>
        Nazaj na znamke
      </NuxtLink>

      <!-- Hero Section -->
      <section class="mb-12 relative rounded-xl overflow-hidden h-96 bg-cover bg-center" :style="{ backgroundImage: `url('${brand.image}')` }">
        <div class="absolute inset-0 bg-black bg-opacity-40 flex items-center justify-center">
          <div class="text-center text-white px-4">
            <p class="text-lg font-serif italic">{{ brand.kicker }}</p>
            <h1 class="text-4xl md:text-5xl font-serif font-bold mt-2">{{ brand.tagline }}</h1>
          </div>
        </div>
      </section>

      <!-- Heritage Section -->
      <section v-if="brand.heritage" class="mb-12">
        <h2 class="text-2xl font-serif font-bold mb-4 text-primary-dark">Zgodovina</h2>
        <p class="text-gray-700">{{ brand.heritage }}</p>
      </section>

      <!-- Highlights Grid -->
      <section class="mb-12">
        <h2 class="text-2xl font-serif font-bold mb-4 text-primary-dark">Naše prednosti</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div v-for="highlight in brand.highlights" :key="highlight" class="bg-white p-4 rounded-lg shadow">
            <p class="font-serif">✦ {{ highlight }}</p>
          </div>
        </div>
      </section>

      <!-- Face Shape Hint -->
      <section class="mb-12 bg-primary-dark text-white p-6 rounded-lg">
        <h2 class="text-xl font-serif font-bold mb-2">Kakšna je vaša oblika obraza?</h2>
        <p class="mb-4">Izberite obliko, ki najbolj ustreza vaši obliki obraza, da boste dobili priporočeno okvir.</p>
        <NuxtLink to="/okvir" class="inline-block bg-accent text-primary-dark px-4 py-2 rounded font-medium hover:bg-opacity-90 transition">
          Najdi svoj okvir
        </NuxtLink>
      </section>

      <!-- Featured Frames -->
      <section class="mb-12">
        <h2 class="text-2xl font-serif font-bold mb-4 text-primary-dark">Naše najboljše okvire</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div v-for="frame in featuredFrames" :key="frame.id" class="bg-white rounded-lg shadow overflow-hidden">
            <img :src="frame.image" :alt="frame.name" class="w-full h-48 object-cover">
            <div class="p-4">
              <h3 class="font-serif font-bold text-lg mb-1">{{ frame.name }}</h3>
              <p class="text-gray-600 text-sm mb-2">{{ frame.description }}</p>
              <p class="font-bold text-primary-dark">{{ frame.price.toFixed(2) }} €</p>
            </div>
          </div>
        </div>
      </section>

      <!-- FAQs Accordion -->
      <section class="mb-12">
        <h2 class="text-2xl font-serif font-bold mb-4 text-primary-dark">Pogosto zastavljena vprašanja</h2>
        <div class="space-y-4">
          <div v-for="(faq, index) in brand.faqs" :key="index" class="border border-gray-200 rounded-lg overflow-hidden">
            <button @click="toggleFaq(index)" class="w-full p-4 text-left flex justify-between items-center bg-gray-50 hover:bg-gray-100 transition">
              <span class="font-medium">{{ faq.question }}</span>
              <svg :class="{ 'transform rotate-180': openFaq === index }" class="w-5 h-5 text-gray-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
              </svg>
            </button>
            <div v-show="openFaq === index" class="p-4 bg-white">
              <p class="text-gray-700">{{ faq.answer }}</p>
            </div>
          </div>
        </div>
      </section>

      <!-- CTA Section -->
      <section class="mb-12 text-center">
        <div class="bg-primary-dark text-white p-8 rounded-lg max-w-2xl mx-auto">
          <h2 class="text-2xl font-serif font-bold mb-4">Želite preizkusiti {{ brand.name }}?</h2>
          <p class="mb-6">Pridite na našo trgovino v Ljubljani ali nas kontaktirajte za dodatne informacije.</p>
          <NuxtLink to="/kontakt" data-goal="brand-book" class="inline-block bg-accent text-primary-dark px-6 py-3 rounded font-medium hover:bg-opacity-90 transition">
            Kontaktirajte nas
          </NuxtLink>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useHead } from '@vueuse/head'
import brands from '~/data/brands.json'
import frames from '~/data/frames.json'

const route = useRoute()
const slug = route.params.slug as string

const brand = computed(() => {
  return brands.find(b => b.slug === slug) || brands[0]
})

const featuredFrames = computed(() => {
  return frames.filter(frame => frame.brand === brand.value.name)
})

const openFaq = ref<number | null>(null)

const toggleFaq = (index: number) => {
  openFaq.value = openFaq.value === index ? null : index
}

// JSON-LD Schemas
const productSchema = computed(() => ({
  "@context": "https://schema.org",
  "@type": "Product",
  "name": brand.value.name,
  "description": brand.value.description,
  "image": brand.value.image,
  "offers": {
    "@type": "Offer",
    "priceCurrency": "EUR",
    "itemOffered": featuredFrames.value.map(frame => ({
      "@type": "Product",
      "name": frame.name,
      "description": frame.description,
      "image": frame.image,
      "offers": {
        "@type": "Offer",
        "price": frame.price,
        "priceCurrency": "EUR"
      }
    }))
  }
}))

const faqSchema = computed(() => ({
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": brand.value.faqs.map((faq: any) => ({
    "@type": "Question",
    "name": faq.question,
    "acceptedAnswer": {
      "@type": "Answer",
      "text": faq.answer
    }
  }))
}))

// Local SEO Keywords
useHead({
  title: `${brand.value.name} - Optikasi`,
  meta: [
    { name: 'description', content: brand.value.description },
    { name: 'keywords', content: `optika, očala, ${brand.value.name}, Ljubljana, Bežigrad, Vojkova 58` }
  ],
  link: [
    { rel: 'canonical', href: `https://optikasi.si/znamke/${slug}` }
  ]
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;700&family=Source+Sans+3:wght@400;600&display=swap');

body {
  font-family: 'Source Sans 3', sans-serif;
}
h1, h2, h3 {
  font-family: 'Cormorant Garamond', serif;
}
</style>
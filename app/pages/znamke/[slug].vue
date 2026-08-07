<script setup>
import brandsData from '~/data/brands.json'
import framesData from '~/data/frames.json'

const route = useRoute()
const slug = route.params.slug
const brand = brandsData.find(b => b.slug === slug)

if (!brand) throw createError({ statusCode: 404, statusMessage: 'Znamka ni bila najdena' })

const featuredFrames = framesData.filter(f => brand.featured?.includes(f.id))
const openFaq = ref(null)
const toggleFaq = (i) => {
  openFaq.value = openFaq.value === i ? null : i
}

// Generate JSON-LD for Product/ItemList and FAQPage
const productJsonLd = {
  '@context': 'https://schema.org',
  '@type': 'Product',
  'name': brand.name,
  'description': brand.description,
  'brand': {
    '@type': 'Brand',
    'name': brand.name
  },
  'offers': {
    '@type': 'Offer',
    'priceCurrency': 'EUR',
    'availability': 'https://schema.org/InStock'
  }
}

const itemListJsonLd = {
  '@context': 'https://schema.org',
  '@type': 'ItemList',
  'itemListElement': featuredFrames.map((frame, index) => ({
    '@type': 'ListItem',
    'position': index + 1,
    'item': {
      '@type': 'Product',
      'name': frame.name,
      'image': frame.image,
      'offers': {
        '@type': 'Offer',
        'priceCurrency': 'EUR',
        'price': frame.price
      }
    }
  }))
}

const faqPageJsonLd = {
  '@context': 'https://schema.org',
  '@type': 'FAQPage',
  'mainEntity': brand.faqs?.map(faq => ({
    '@type': 'Question',
    'name': faq.question,
    'acceptedAnswer': {
      '@type': 'Answer',
      'text': faq.answer
    }
  })) || []
}

useHead({
  title: `${brand.name} Očala | OptikaSI Ljubljana`,
  meta: [
    { name: 'description', content: brand.description?.substring(0, 160) },
    { name: 'keywords', content: `${brand.keywords?.join(', ')}, Ljubljana, Bežigrad, Vojkova 58` }
  ],
  script: [
    {
      type: 'application/ld+json',
      innerHTML: JSON.stringify(productJsonLd)
    },
    {
      type: 'application/ld+json',
      innerHTML: JSON.stringify(itemListJsonLd)
    },
    {
      type: 'application/ld+json',
      innerHTML: JSON.stringify(faqPageJsonLd)
    }
  ]
})
</script>

<template>
  <div class="min-h-screen bg-cream">
    <!-- Hero Section -->
    <section class="relative bg-cover bg-center h-[50vh] flex items-center justify-center" :style="{ backgroundImage: `url(${brand.image})` }">
      <div class="absolute inset-0 bg-black bg-opacity-40"></div>
      <div class="relative text-center text-white px-4">
        <h2 class="text-xl md:text-2xl font-serif">{{ brand.name }}</h2>
        <h1 class="text-3xl md:text-5xl font-serif mt-2">{{ brand.tagline }}</h1>
      </div>
    </section>

    <!-- Description Section -->
    <section class="py-12 px-4 max-w-6xl mx-auto">
      <p class="text-lg text-gray-700 mb-8">{{ brand.description }}</p>

      <!-- Heritage Section -->
      <div v-if="brand.heritage" class="mb-12">
        <h2 class="text-2xl font-serif text-primary-dark mb-4">Dediščina znamke</h2>
        <p class="text-gray-700">{{ brand.heritage }}</p>
      </div>

      <!-- Highlights Section -->
      <div v-if="brand.highlights" class="mb-12">
        <h2 class="text-2xl font-serif text-primary-dark mb-4">Ključne lastnosti</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div v-for="highlight in brand.highlights" :key="highlight" class="flex items-start">
            <span class="text-accent mr-2">✦</span>
            <p>{{ highlight }}</p>
          </div>
        </div>
      </div>

      <!-- Face Shape Hint -->
      <div v-if="brand.faceShapeHint" class="mb-12 bg-primary-dark text-white p-6 rounded-lg">
        <h2 class="text-xl font-serif mb-2">Priporočena oblika obraza</h2>
        <p>{{ brand.faceShapeHint }}</p>
      </div>

      <!-- Featured Frames Section -->
      <div v-if="featuredFrames.length > 0" class="mb-12">
        <h2 class="text-2xl font-serif text-primary-dark mb-4">Izbrani Modeli</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div v-for="frame in featuredFrames" :key="frame.id" class="bg-white shadow-md rounded-lg overflow-hidden">
            <img :src="frame.image" :alt="frame.name" class="w-full h-48 object-cover">
            <div class="p-4">
              <h3 class="font-bold text-lg">{{ frame.name }}</h3>
              <p class="text-gray-600 mb-2">{{ frame.description }}</p>
              <p class="text-accent font-bold">{{ frame.price.toFixed(2) }} €</p>
            </div>
          </div>
        </div>
      </div>

      <!-- FAQs Section -->
      <div v-if="brand.faqs && brand.faqs.length > 0" class="mb-12">
        <h2 class="text-2xl font-serif text-primary-dark mb-4">Pogosto zastavljena vprašanja</h2>
        <div class="space-y-4">
          <div v-for="(faq, i) in brand.faqs" :key="i" class="border-b border-gray-200 pb-4">
            <button @click="toggleFaq(i)" class="w-full text-left font-medium text-primary-dark flex justify-between items-center">
              {{ faq.question }}
              <span>{{ openFaq === i ? '-' : '+' }}</span>
            </button>
            <div v-show="openFaq === i" class="mt-2 text-gray-600">
              {{ faq.answer }}
            </div>
          </div>
        </div>
      </div>

      <!-- CTA Section -->
      <div class="bg-primary-dark text-white py-12 px-4 rounded-lg text-center">
        <h2 class="text-2xl font-serif mb-4">Želite preizkusiti {{ brand.name }}?</h2>
        <NuxtLink to="/kontakt" data-goal="brand-book" class="inline-block bg-accent text-primary-dark font-bold py-3 px-6 rounded hover:bg-opacity-90 transition duration-300">
          Kontaktirajte nas
        </NuxtLink>
      </div>

      <!-- Back Link -->
      <div class="mt-8 text-center">
        <NuxtLink to="/znamke" class="text-primary-dark underline">Nazaj na znamke</NuxtLink>
      </div>
    </section>
  </div>
</template>
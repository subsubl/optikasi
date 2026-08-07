<template>
  <div>
    <!-- Hero Section -->
    <section class="relative h-[50vh] min-h-[420px] flex items-center justify-center bg-gray-900 text-white overflow-hidden">
      <div class="absolute inset-0 z-0">
        <img v-if="brand.image" :src="brand.image" :alt="brand.name" class="w-full h-full object-cover opacity-40" />
      </div>
      <div class="absolute inset-0 bg-gradient-to-br from-primary-dark/80 to-black/70 z-0" />
      <div class="relative z-10 text-center px-6 max-w-4xl">
        <span class="text-accent uppercase tracking-widest text-sm font-bold mb-6 block">{{ brand.name }}</span>
        <h1 class="text-5xl md:text-7xl font-serif mb-8 leading-tight">{{ brand.tagline }}</h1>
        <p class="text-xl md:text-2xl font-light text-gray-200 leading-relaxed max-w-2xl mx-auto">
          {{ brand.description }}
        </p>
      </div>
    </section>

    <!-- Heritage Story -->
    <section v-if="brand.heritage" class="py-24 bg-cream">
      <div class="container mx-auto px-6 max-w-4xl text-center">
        <span class="text-accent uppercase tracking-widest text-sm font-bold mb-4 block">Dediščina znamke</span>
        <h2 class="text-4xl font-serif text-primary-dark mb-8">Zgodba {{ brand.name }}</h2>
        <p class="text-gray-600 leading-relaxed text-lg">{{ brand.heritage }}</p>
        <div class="w-16 h-1 bg-accent mx-auto mt-12"></div>
      </div>
    </section>

    <!-- Highlights -->
    <section v-if="brand.highlights?.length" class="py-24 bg-white">
      <div class="container mx-auto px-6 max-w-5xl">
        <div class="text-center mb-16">
          <span class="text-accent uppercase tracking-widest text-sm font-bold mb-4 block">Zakaj {{ brand.name }}</span>
          <h2 class="text-4xl font-serif text-primary-dark">Prednosti znamke</h2>
        </div>
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div v-for="(item, i) in brand.highlights" :key="i" class="flex items-start space-x-4 p-6 border border-gray-100 bg-cream hover:border-accent transition-colors">
            <span class="text-accent text-xl mt-0.5">✦</span>
            <p class="text-gray-700 text-sm leading-relaxed">{{ item }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Face Shape / Frame Finder Hint -->
    <section class="py-16 bg-white">
      <div class="container mx-auto px-6 max-w-4xl text-center">
        <span class="text-accent uppercase tracking-widest text-sm font-bold mb-4 block">Oblika obraza</span>
        <h2 class="text-3xl font-serif text-primary-dark mb-4">Katera oblika vam pristaja?</h2>
        <p class="text-gray-500 leading-relaxed mb-6 max-w-2xl mx-auto">
          {{ brand.name }} okvirji najbolj pristajajo ovalnim, okroglim in podolgovatim oblikam obraza.
          Pridite v Studio Optika SI na Vojkovi 58 in skupaj bova našla popoln okvir za vaš obraz.
        </p>
        <NuxtLink to="/kontakt" data-goal="face-shape" class="inline-block text-accent border-b border-accent pb-1 hover:text-white hover:border-white transition-colors uppercase text-xs tracking-widest">
          Dogovorite se za svetovanje →
        </NuxtLink>
      </div>
    </section>

    <!-- Featured Frames -->
    <section v-if="featuredFrames.length" class="py-24 bg-cream">
      <div class="container mx-auto px-6 max-w-5xl">
        <div class="text-center mb-16">
          <h2 class="text-4xl font-serif text-primary-dark mb-4">Izbrani Modeli</h2>
          <p class="text-gray-500">Priljubljeni {{ brand.name }} modeli na zalogi.</p>
        </div>
        <div class="grid md:grid-cols-2 gap-8">
          <div v-for="frame in featuredFrames" :key="frame.id" class="bg-white p-6 border border-gray-100 shadow-sm">
            <div class="h-48 bg-gray-50 mb-4 flex items-center justify-center">
              <img v-if="frame.image" :src="frame.image" :alt="frame.name" class="h-full w-full object-contain" />
              <span v-else class="text-xs uppercase tracking-widest text-gray-400">{{ frame.name }}</span>
            </div>
            <h3 class="font-serif text-xl text-primary-dark mb-2">{{ frame.name }}</h3>
            <p class="text-gray-500 text-sm mb-3">{{ frame.description }}</p>
            <span class="text-accent font-bold">{{ frame.price.toFixed(2) }} €</span>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section v-if="brand.faqs?.length" class="py-24 bg-white">
      <div class="container mx-auto px-6 max-w-3xl">
        <div class="text-center mb-16">
          <span class="text-accent uppercase tracking-widest text-sm font-bold mb-4 block">Pogosta vprašanja</span>
          <h2 class="text-4xl font-serif text-primary-dark">{{ brand.name }} — Najpogostejša vprašanja</h2>
        </div>
        <div class="space-y-4">
          <div v-for="(faq, i) in brand.faqs" :key="i" class="border border-gray-100 bg-cream">
            <button
              @click="toggleFaq(i)"
              class="w-full flex items-center justify-between p-6 text-left"
              :aria-expanded="openFaq === i"
            >
              <span class="font-serif text-lg text-primary-dark">{{ faq.q }}</span>
              <span class="text-accent text-xl ml-4 transition-transform duration-300" :class="{ 'rotate-45': openFaq === i }">+</span>
            </button>
            <div v-show="openFaq === i" class="px-6 pb-6">
              <p class="text-gray-600 leading-relaxed">{{ faq.a }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="py-24 bg-primary-dark text-white">
      <div class="container mx-auto px-6 text-center">
        <h3 class="text-3xl font-serif mb-4">Želite preizkusiti {{ brand.name }}?</h3>
        <p class="text-gray-300 mb-8">Rezervirajte termin in odkrijte popoln okvir za vaš obraz.</p>
        <NuxtLink to="/kontakt" data-goal="brand-book" class="inline-block border border-accent text-accent hover:bg-accent hover:text-white px-8 py-3 uppercase tracking-[0.2em] transition-all">
          Rezervirajte Termin
        </NuxtLink>
      </div>
    </section>

    <!-- Back Link -->
    <div class="text-center py-12">
      <NuxtLink to="/znamke" class="text-gray-500 hover:text-primary transition-colors text-sm uppercase tracking-widest">
        ← Nazaj na vse znamke
      </NuxtLink>
    </div>
  </div>
</template>

<script setup>
import brandsData from '~/data/brands.json'
import framesData from '~/data/frames.json'

const route = useRoute()
const slug = route.params.slug

const brand = brandsData.find(b => b.slug === slug)

if (!brand) {
  throw createError({ statusCode: 404, statusMessage: 'Znamka ni bila najdena' })
}

const featuredFrames = framesData.filter(f => brand.featured?.includes(f.id))

const openFaq = ref(null)
const toggleFaq = (i) => {
  openFaq.value = openFaq.value === i ? null : i
}

// JSON-LD structured data for rich results (SEO) — rendered SSR via useHead innerHTML
const seoUrl = `https://optikasi.si/znamke/${slug}`
const ldSchemas = []

if (featuredFrames.length) {
  ldSchemas.push({
    '@context': 'https://schema.org',
    '@type': 'ItemList',
    name: `${brand.name} očala`,
    url: seoUrl,
    itemListElement: featuredFrames.map((f, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      item: {
        '@type': 'Product',
        name: f.name,
        description: f.description,
        image: `https://optikasi.si${f.image ?? ''}`,
        brand: { '@type': 'Brand', name: brand.name },
        offers: { '@type': 'Offer', price: f.price, priceCurrency: 'EUR', availability: 'https://schema.org/InStock' }
      }
    }))
  })
}

if (brand.faqs?.length) {
  ldSchemas.push({
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: brand.faqs.map(faq => ({
      '@type': 'Question',
      name: faq.q,
      acceptedAnswer: { '@type': 'Answer', text: faq.a }
    }))
  })
}

useHead({
  title: `${brand.name} Očala | OptikaSI Ljubljana`,
  meta: [
    { name: 'description', content: brand.description?.substring(0, 160) },
    { name: 'keywords', content: [...(brand.keywords ?? []), 'ljubljana', 'bežigrad', 'vojkova 58'].join(', ') },
    { property: 'og:title', content: `${brand.name} Očala | OptikaSI Ljubljana` },
    { property: 'og:description', content: brand.description?.substring(0, 160) },
    { property: 'og:url', content: seoUrl },
    { property: 'og:type', content: 'website' },
    { property: 'og:locale', content: 'sl_SI' }
  ],
  link: [{ rel: 'canonical', href: seoUrl }],
  script: ldSchemas.map(s => ({ type: 'application/ld+json', innerHTML: JSON.stringify(s) }))
})
</script>

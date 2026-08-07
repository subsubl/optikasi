<template>
  <div>
    <section class="relative h-[45vh] min-h-[360px] flex items-center justify-center bg-primary-dark text-white overflow-hidden">
      <div class="absolute inset-0 bg-gradient-to-br from-primary-dark to-black opacity-80" />
      <div class="relative z-10 text-center px-6 max-w-4xl">
        <span class="text-accent uppercase tracking-widest text-sm font-bold mb-6 block">Optika Ljubljana - Bežigrad</span>
        <h1 class="text-5xl md:text-7xl font-serif mb-8 leading-tight">Naše Znamke</h1>
        <p class="text-xl md:text-2xl font-light text-gray-300 leading-relaxed max-w-2xl mx-auto">
          Priznane blagovne znamke, ki zagotavljajo kakovost, izdelavo in stil.
        </p>
      </div>
    </section>

    <!-- Brands Grid -->
    <section class="py-24 bg-cream">
      <div class="container mx-auto px-6">
        <div class="grid grid-cols-2 md:grid-cols-3 gap-8">
          <NuxtLink
            v-for="brand in brands"
            :key="brand.slug"
            :to="`/znamke/${brand.slug}`"
            class="group bg-white p-8 border border-gray-100 hover:border-accent shadow-sm transition-all hover:shadow-md text-center"
          >
            <div v-if="brand.image" class="h-28 mb-6 flex items-center justify-center">
              <img :src="brand.image" :alt="brand.name" class="h-full max-w-full object-contain filter grayscale-0 opacity-90 transition-all duration-300" />
            </div>
            <h3 class="font-serif text-xl text-primary-dark mb-2 group-hover:text-accent transition-colors">{{ brand.name }}</h3>
            <p class="text-gray-500 text-sm">{{ brand.tagline }}</p>
          </NuxtLink>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="py-24 bg-white">
      <div class="container mx-auto px-6 text-center">
        <h2 class="text-3xl md:text-4xl font-serif text-primary-dark mb-4">Ne najdete svoje znamke?</h2>
        <p class="text-gray-500 leading-relaxed max-w-2xl mx-auto mb-8">
          V Studio Optika SI naročamo tudi modele znamk, ki niso razstavljeni. Rezervirajte termin in z veseljem vam pomagamo najti popoln par.
        </p>
        <NuxtLink to="/kontakt" data-goal="brands-list-book" class="inline-block bg-primary text-white px-8 py-4 uppercase tracking-[0.2em] text-sm font-bold hover:bg-accent transition-colors">
          Rezervirajte Termin
        </NuxtLink>
      </div>
    </section>
  </div>
</template>

<script setup>
import brandsData from '~/data/brands.json'

useHead({
  title: 'Blagovne Znamke in Okvirji | OptikaSI Ljubljana',
  meta: [
    { name: 'description', content: 'Odkrijte vrhunske znamke očal v OptikaSI Ljubljana: Ray-Ban, Lindberg, David Beckham, Gucci, Missoni, Polar, Montana in več. Na voljo korekcijska in sončna očala.' },
    { name: 'keywords', content: 'znamke očal, ray-ban ljubljana, lindberg ljubljana, gucci očala, dizajnerska očala, optika ljubljana' }
  ]
})

const brands = brandsData
</script>

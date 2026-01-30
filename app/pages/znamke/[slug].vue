<template>
  <div class="py-24 container mx-auto px-6 max-w-4xl">
    <div class="text-center mb-16">
      <span class="text-accent uppercase tracking-widest text-sm font-bold mb-4 block">{{ brand.name }}</span>
      <h1 class="text-5xl font-serif text-primary-dark mb-6">{{ brand.tagline }}</h1>
      <p class="text-gray-600 leading-relaxed text-lg max-w-2xl mx-auto">
        {{ brand.description }}
      </p>
    </div>

    <!-- Featured Frames -->
    <div v-if="featuredFrames.length" class="mb-16">
      <h2 class="text-2xl font-serif text-primary-dark mb-8 text-center">Izbrani Modeli</h2>
      <div class="grid md:grid-cols-2 gap-8">
        <div v-for="frame in featuredFrames" :key="frame.id" class="bg-white p-6 border border-gray-100">
          <div class="h-48 bg-gray-50 mb-4 flex items-center justify-center text-gray-300">
            <span class="text-xs uppercase tracking-widest">{{ frame.name }}</span>
          </div>
          <h3 class="font-serif text-xl text-primary-dark mb-2">{{ frame.name }}</h3>
          <p class="text-gray-500 text-sm mb-3">{{ frame.description }}</p>
          <span class="text-accent font-bold">{{ frame.price.toFixed(2) }} €</span>
        </div>
      </div>
    </div>

    <!-- CTA -->
    <div class="text-center bg-primary-dark text-white p-12">
      <h3 class="text-2xl font-serif mb-4">Želite preizkusiti {{ brand.name }}?</h3>
      <p class="text-gray-300 mb-8">Rezervirajte termin in odkrijte popoln okvir za vaš obraz.</p>
      <NuxtLink to="/kontakt" class="inline-block border border-accent text-accent hover:bg-accent hover:text-white px-8 py-3 uppercase tracking-[0.2em] transition-all">
        Rezervirajte Termin
      </NuxtLink>
    </div>

    <!-- Back Link -->
    <div class="text-center mt-12">
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

useHead({
  title: `${brand.name} Očala`,
  meta: [
    { name: 'description', content: brand.description.substring(0, 160) },
    { name: 'keywords', content: brand.keywords?.join(', ') }
  ]
})
</script>

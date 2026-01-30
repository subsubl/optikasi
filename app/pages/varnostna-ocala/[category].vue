<template>
  <div v-if="pageData" class="min-h-screen pt-20">
    <!-- Hero -->
    <section class="relative h-[60vh] min-h-[500px] flex items-center justify-center bg-gray-900 text-white">
      <div class="absolute inset-0 z-0">
         <img :src="pageData.header_image" :alt="pageData.title" class="w-full h-full object-cover opacity-40" />
      </div>
      <div class="relative z-10 text-center px-4 max-w-5xl mx-auto">
        <h1 class="text-4xl md:text-6xl font-serif mb-6 leading-tight">{{ pageData.title }}</h1>
        <div class="w-24 h-1 bg-accent mx-auto"></div>
      </div>
    </section>

    <!-- Intro Content -->
    <section class="py-20 px-4 bg-white">
      <div class="container mx-auto max-w-4xl">
        <div class="prose prose-lg mx-auto text-gray-600">
          <template v-for="(paragraph, index) in pageData.intro" :key="index">
            <h3 v-if="isHeader(paragraph)" class="text-2xl font-serif text-gray-900 mt-8 mb-4">{{ paragraph }}</h3>
            <p v-else class="mb-4 leading-relaxed">{{ paragraph }}</p>
          </template>
        </div>
      </div>
    </section>

    <!-- Products Grid -->
    <section class="py-20 px-4 bg-gray-50">
      <div class="container mx-auto">
        <h2 class="text-3xl md:text-4xl font-serif text-center mb-16 text-gray-900">Priporočeni Okvirji</h2>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div v-for="(product, idx) in pageData.products" :key="idx" class="bg-white p-6 rounded-sm shadow-sm hover:shadow-md transition-shadow flex flex-col">
            <div class="aspect-video mb-6 bg-gray-100 rounded-sm overflow-hidden flex items-center justify-center p-4">
              <img :src="product.image" :alt="product.name" class="w-full h-full object-contain mix-blend-multiply" />
            </div>
            
            <h3 class="text-xl font-bold text-gray-900 mb-2">{{ product.name }}</h3>
            <p v-if="product.sku" class="text-sm text-gray-500 mb-4 font-mono">Art. {{ product.sku }}</p>
            
            <div class="mt-auto space-y-2 border-t pt-4 border-gray-100">
              <h4 class="text-sm font-semibold uppercase tracking-wider text-gray-400">Lastnosti:</h4>
              <ul class="text-sm text-gray-600 space-y-1 list-disc pl-4">
                <li v-for="(feature, fidx) in product.features" :key="fidx">{{ feature }}</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>
    
    <!-- CTA -->
     <section class="py-20 bg-primary text-white text-center">
      <div class="container mx-auto px-6">
        <h2 class="text-3xl md:text-4xl font-serif mb-8">Potrebujete svetovanje?</h2>
        <p class="text-lg md:text-xl text-white/80 mb-10 max-w-2xl mx-auto">
          Naši strokovnjaki vam bodo pomagali izbrati ustrezna varnostna očala za vaše specifične delovne pogoje.
        </p>
        <NuxtLink to="/kontakt" class="inline-block bg-white text-primary px-10 py-4 font-bold uppercase tracking-widest hover:bg-accent hover:text-white transition-all transform hover:-translate-y-1">
          Kontaktirajte nas
        </NuxtLink>
      </div>
    </section>
  </div>
</template>

<script setup>
import safetyDataRaw from '@/assets/data/safety_data.json'
const route = useRoute()
const category = route.params.category

const pageData = computed(() => {
  return safetyDataRaw[category]
})

const isHeader = (text) => {
    // Simple heuristic: short lines ending with colon or starting with "Najpogostejša"
    return text.length < 100 && (text.trim().endsWith(':') || text.includes('nevarnost'))
}

useHead({
  title: pageData.value ? `${pageData.value.title} | Varnostna Očala` : 'Varnostna Očala',
})

if (!safetyDataRaw[category]) {
    throw createError({ statusCode: 404, statusMessage: 'Category Not Found' })
}
</script>

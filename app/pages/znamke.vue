<template>
  <div class="py-24 container mx-auto px-6">
    <div class="text-center mb-16">
      <h1 class="text-4xl text-primary-dark mb-4">Naše Znamke</h1>
      <p class="text-gray-500 tracking-wide">Priznane blagovne znamke, ki zagotavljajo kakovost in stil.</p>
    </div>

    <!-- Brands Grid -->
    <div class="grid grid-cols-2 md:grid-cols-4 gap-12 items-center opacity-70">
      <!-- Placeholder for actual logos, using text for now -->
      <div v-for="brand in brands" :key="brand" class="p-8 text-center border border-transparent hover:border-gray-200 transition-all font-serif text-2xl text-gray-400 hover:text-primary">
        {{ brand }}
      </div>
    </div>
  </div>
</template>

<script setup>
useHead({
  title: 'Blagovne Znamke in Okvirji',
  meta: [
    { name: 'description', content: 'Ponujamo vrhunske okvirje priznanih znamk: Ray-Ban, Oakley, Gucci, Tom Ford, Lindberg in druge. Na voljo korekcijska in sončna očala.' }
  ]
})
</script>

<script setup>
const brands = [
  'Ray-Ban', 'Gucci', 'Prada', 'Tom Ford', 
  'Dolce & Gabbana', 'Persol', 'Oakley', 'Versace',
  'Armani', 'Burberry', 'Chanel', 'Dior'
]
</script>

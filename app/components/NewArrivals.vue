<template>
  <section class="py-24 bg-white">
    <div class="container mx-auto px-6">
      <div class="text-center mb-16">
        <span class="text-accent uppercase tracking-widest text-sm font-bold mb-4 block">Novosti</span>
        <h2 class="text-4xl text-primary-dark mb-4">Najnovejši Okvirji</h2>
        <p class="text-gray-500 max-w-xl mx-auto">Sveže prispeli modeli najboljših svetovnih znamk.</p>
      </div>

      <!-- Horizontal Scroll Container -->
      <div class="flex overflow-x-auto gap-8 pb-4 -mx-6 px-6 snap-x snap-mandatory scrollbar-hide">
        <div 
          v-for="frame in frames" 
          :key="frame.id" 
          class="flex-shrink-0 w-72 snap-start bg-cream p-6 border border-gray-100 hover:border-accent transition-colors group"
        >
          <!-- Image Placeholder -->
          <div class="h-48 bg-gray-100 mb-4 flex items-center justify-center text-gray-300 group-hover:bg-gray-50 transition-colors">
            <span class="text-xs uppercase tracking-widest">{{ frame.brand }}</span>
          </div>

          <span class="text-xs text-accent uppercase tracking-widest block mb-1">{{ frame.brand }}</span>
          <h3 class="font-serif text-lg text-primary-dark mb-2">{{ frame.name }}</h3>
          <p class="text-gray-500 text-sm mb-4 min-h-[40px]">{{ frame.description }}</p>
          <span class="text-accent font-bold">{{ frame.price.toFixed(2) }} €</span>
        </div>
      </div>

      <div class="text-center mt-12">
        <NuxtLink to="/znamke" class="inline-block border-b border-primary text-primary hover:text-accent hover:border-accent transition-colors pb-1 uppercase text-sm tracking-widest">
          Oglejte si vse znamke →
        </NuxtLink>
      </div>
    </div>
  </section>
</template>

<script setup>
import framesData from '~/data/frames.json'

const frames = framesData.filter(f => f.isNew).slice(0, 6)
</script>

<style scoped>
.scrollbar-hide::-webkit-scrollbar {
  display: none;
}
.scrollbar-hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>

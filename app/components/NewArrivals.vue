<template>
  <section class="py-24 bg-white">
    <div class="container mx-auto px-6">
      <div class="text-center mb-16">
        <span class="text-accent uppercase tracking-widest text-sm font-bold mb-4 block">Novosti</span>
        <h2 class="text-4xl text-primary-dark mb-4">Najnovejši Okvirji</h2>
        <p class="text-gray-500 max-w-xl mx-auto">Sveže prispeli modeli najboljših svetovnih znamk.</p>
      </div>

      <!-- Horizontal Scroll Container -->
      <div class="relative group/scrollnav">
        <!-- Left Navigation Button -->
        <button
          @click="scroll('left')"
          aria-label="Pomakni levo"
          aria-controls="new-arrivals-list"
          class="absolute left-0 top-1/2 -translate-y-1/2 -ml-4 z-10 w-10 h-10 rounded-full bg-white shadow-md border border-gray-100 text-primary hover:bg-accent hover:text-white hover:border-accent transition-all duration-300 flex items-center justify-center focus:outline-none focus-visible:ring-2 focus-visible:ring-accent focus:opacity-100 focus-visible:opacity-100 hidden md:flex opacity-0 group-hover/scrollnav:opacity-100 group-focus-within/scrollnav:opacity-100"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
        </button>

        <div
          id="new-arrivals-list"
          ref="scrollContainer"
          tabindex="0"
          role="region"
          aria-label="Seznam novih okvirjev"
          class="flex overflow-x-auto gap-8 pb-4 -mx-6 px-6 snap-x snap-mandatory scrollbar-hide scroll-smooth focus:outline-none focus-visible:ring-2 focus-visible:ring-accent"
        >
          <div
            v-for="frame in frames"
            :key="frame.id"
            class="flex-shrink-0 w-72 snap-start bg-cream p-6 border border-gray-100 hover:border-accent transition-colors group"
          >
            <!-- Product Image -->
            <div class="h-48 bg-gray-100 mb-4 flex items-center justify-center overflow-hidden group-hover:bg-gray-50 transition-colors">
              <img
                v-if="frame.image"
                :src="frame.image"
                :alt="frame.name"
                class="w-full h-full object-contain p-2"
              />
              <span v-else class="text-xs uppercase tracking-widest text-gray-300">{{ frame.brand }}</span>
            </div>

            <span class="text-xs text-accent uppercase tracking-widest block mb-1">{{ frame.brand }}</span>
            <h3 class="font-serif text-lg text-primary-dark mb-2">{{ frame.name }}</h3>
            <p class="text-gray-500 text-sm mb-4 min-h-[40px]">{{ frame.description }}</p>
            <span class="text-accent font-bold">{{ frame.price.toFixed(2) }} €</span>
          </div>
        </div>

        <!-- Right Navigation Button -->
        <button
          @click="scroll('right')"
          aria-label="Pomakni desno"
          aria-controls="new-arrivals-list"
          class="absolute right-0 top-1/2 -translate-y-1/2 -mr-4 z-10 w-10 h-10 rounded-full bg-white shadow-md border border-gray-100 text-primary hover:bg-accent hover:text-white hover:border-accent transition-all duration-300 flex items-center justify-center focus:outline-none focus-visible:ring-2 focus-visible:ring-accent focus:opacity-100 focus-visible:opacity-100 hidden md:flex opacity-0 group-hover/scrollnav:opacity-100 group-focus-within/scrollnav:opacity-100"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
        </button>
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

const scrollContainer = ref(null)

const scroll = (direction) => {
  if (!scrollContainer.value) return

  const scrollAmount = 320 // Approximately one card width + gap
  const targetScroll = scrollContainer.value.scrollLeft + (direction === 'left' ? -scrollAmount : scrollAmount)

  scrollContainer.value.scrollTo({
    left: targetScroll,
    behavior: 'smooth'
  })
}
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

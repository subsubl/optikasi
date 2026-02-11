<template>
  <div class="py-24 container mx-auto px-6">
    <div class="text-center mb-16">
      <h1 class="text-4xl text-primary-dark mb-4">Naše Znamke</h1>
      <p class="text-gray-500 tracking-wide">Priznane blagovne znamke, ki zagotavljajo kakovost in stil.</p>
    </div>

    <!-- Brands Grid -->
    <div class="grid grid-cols-2 md:grid-cols-4 gap-12 items-center opacity-70">
      <!-- Placeholder for actual logos, using text for now -->
      <div v-for="brand in brands" :key="brand.name" class="p-8 text-center border border-transparent hover:border-gray-200 transition-all group">
        <img :src="brand.image" :alt="brand.name" class="h-20 w-full object-contain filter grayscale opacity-70 group-hover:grayscale-0 group-hover:opacity-100 transition-all duration-300">
      </div>
    </div>
  </div>
</template>

<script setup>
useHead({
  title: 'Blagovne Znamke in Okvirji',
  meta: [
    { name: 'description', content: 'Ponujamo vrhunske okvirje priznanih znamk: Ray-Ban, Oakley, Tom Ford in druge. Na voljo korekcijska in sončna očala.' }
  ]
})

const brands = [
  { name: 'Ray Ban', image: 'https://placehold.co/400x200/ffffff/000000?text=Ray+Ban' },
  { name: 'Polar', image: 'https://placehold.co/400x200/ffffff/000000?text=Polar' },
  { name: 'People', image: 'https://placehold.co/400x200/ffffff/000000?text=People' },
  { name: 'David Beckham', image: 'https://placehold.co/400x200/ffffff/000000?text=David+Beckham' },
  { name: 'Flowers', image: 'https://placehold.co/400x200/ffffff/000000?text=Flowers' },
  { name: 'Missoni', image: 'https://placehold.co/400x200/ffffff/000000?text=Missoni' },
  { name: 'Solo', image: 'https://placehold.co/400x200/ffffff/000000?text=Solo' },
  { name: 'El Greco', image: 'https://placehold.co/400x200/ffffff/000000?text=El+Greco' },
  { name: 'Anna Riska', image: 'https://placehold.co/400x200/ffffff/000000?text=Anna+Riska' },
  { name: 'Christies', image: 'https://placehold.co/400x200/ffffff/000000?text=Christies' },
  { name: 'Montana', image: 'https://placehold.co/400x200/ffffff/000000?text=Montana' }
]
</script>

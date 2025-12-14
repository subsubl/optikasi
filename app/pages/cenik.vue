<template>
  <div class="py-24 container mx-auto px-6 max-w-4xl">
    <div class="text-center mb-16">
      <h1 class="text-4xl text-primary-dark mb-4">Cenik Storitev</h1>
      <p class="text-gray-500 tracking-wide">Transparentne cene za vrhunske optične storitve.</p>
    </div>

    <div class="bg-white p-8 md:p-12 shadow-sm border border-gray-100">
      <div v-for="(category, index) in priceList" :key="index" class="mb-12 last:mb-0">
        <h3 class="text-xl text-accent mb-6 font-bold uppercase tracking-widest">{{ category.name }}</h3>
        <div class="space-y-6">
          <div v-for="item in category.items" :key="item.name" class="flex justify-between items-baseline border-b border-gray-100 pb-2">
            <span class="text-gray-700 font-medium">{{ item.name }}</span>
            <span class="text-primary-dark font-serif font-bold text-lg">{{ item.price }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const priceList = [
  {
    name: 'Pregledi',
    items: [
      { name: 'Osnovni pregled vida', price: '30 €' },
      { name: 'Razširjen pregled vida', price: '50 €' },
      { name: 'Pregled za kontaktne leče', price: '40 €' },
    ]
  },
  {
    name: 'Servis',
    items: [
      { name: 'Ravnanje okvirja', price: 'BREZPLAČNO' },
      { name: 'Menjava vijaka', price: '2 €' },
      { name: 'Ultrazvočno čiščenje', price: 'BREZPLAČNO' },
    ]
  }
]
</script>

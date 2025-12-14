<template>
  <div class="py-24 container mx-auto px-6">
    <div class="text-center mb-16">
      <h1 class="text-4xl text-primary-dark mb-4">Spletna Trgovina</h1>
      <p class="text-gray-500 tracking-wide">Vrhunski dodatki za vaša očala. Naročite in prejmite na dom.</p>
    </div>

    <!-- Product Grid -->
    <div class="grid md:grid-cols-3 gap-12 max-w-6xl mx-auto">
      <div v-for="product in products" :key="product.id" class="bg-white p-6 border border-gray-100 shadow-sm hover:shadow-md transition-shadow group">
        <!-- Image Placeholder -->
        <div class="h-64 bg-gray-50 mb-6 flex items-center justify-center text-gray-300">
           <span class="text-sm uppercase tracking-widest">Slika Izdelka</span>
        </div>

        <h3 class="text-xl font-serif text-primary-dark mb-2">{{ product.name }}</h3>
        <p class="text-gray-500 text-sm mb-4 min-h-[40px]">{{ product.description }}</p>
        
        <div class="flex justify-between items-center pt-4 border-t border-gray-100">
          <span class="text-lg font-bold text-accent">{{ product.price.toFixed(2) }} €</span>
          <button 
            class="snipcart-add-item bg-primary-dark text-white text-sm px-6 py-3 uppercase tracking-widest hover:bg-accent transition-colors"
            :data-item-id="product.id"
            :data-item-price="product.price"
            :data-item-url="'/optikasi/trgovina'"
            :data-item-description="product.description"
            :data-item-image="product.image || ''"
            :data-item-name="product.name"
          >
            V Košarico
          </button>
        </div>
      </div>
    </div>
    
    <!-- Snipcart Hidden Settings -->
    <div id="snipcart" data-api-key="ST_NDlkZjE5YjctZWM2Yi00MTQyLTg0ZWItM2U1ZTM0ZGU4Yjg3NjM5MDEzNTMxNjM0OTkwOTgz" hidden></div>
  </div>
</template>

<script setup>
useHead({
  title: 'Trgovina - Dodatki za Očala',
  meta: [
    { name: 'description', content: 'Kupite čistilne sete, etuije in vrvice za očala preko spleta.' }
  ]
})

const products = [
  {
    id: 'clean-kit-premium',
    name: 'Premium Čistilni Set',
    description: 'Sprej za čiščenje (50ml) in krpica iz mikrovlaken v etuiju.',
    price: 12.00
  },
  {
    id: 'chain-gold',
    name: 'Verižica "Elegance" - Zlata',
    description: 'Elegantna pozlačena verižica za korekcijska očala.',
    price: 25.00
  },
  {
    id: 'anti-fog-spray',
    name: 'Sprej Proti Rosenju',
    description: 'Učinkovita zaščita pred rosenjem stekel (30ml).',
    price: 9.50
  },
  {
    id: 'case-leather',
    name: 'Usnjen Etui - Črn',
    description: 'Ročno izdelan etui iz pravega usnja za varno shranjevanje.',
    price: 35.00
  }
]
</script>

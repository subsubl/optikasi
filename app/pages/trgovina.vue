<template>
  <div class="py-24 container mx-auto px-6">
    <div class="text-center mb-16">
      <h1 class="text-4xl text-primary-dark mb-4">Spletna Trgovina</h1>
      <p class="text-gray-500 tracking-wide">Vrhunski dodatki in vintage očala. Naročite in prejmite na dom.</p>
    </div>

    <!-- Vintage Collection -->
    <div class="mb-20">
      <h2 class="text-2xl font-serif text-primary-dark mb-8 text-center">
        <span class="text-accent">✦</span> Vintage Kolekcija <span class="text-accent">✦</span>
      </h2>
      <div class="grid md:grid-cols-4 gap-8 max-w-6xl mx-auto">
        <div v-for="product in vintageProducts" :key="product.id" class="bg-white p-6 border border-gray-100 shadow-sm hover:shadow-md transition-shadow group">
          <div class="h-48 bg-gray-50 mb-4 flex items-center justify-center text-gray-300">
             <span class="text-xs uppercase tracking-widest">Vintage</span>
          </div>
          <h3 class="text-lg font-serif text-primary-dark mb-2">{{ product.name }}</h3>
          <p class="text-gray-500 text-sm mb-3 min-h-[40px]">{{ product.description }}</p>
          <div class="flex justify-between items-center pt-3 border-t border-gray-100">
            <span class="text-lg font-bold text-accent">{{ product.price.toFixed(2) }} €</span>
            <button 
              class="snipcart-add-item bg-primary-dark text-white text-xs px-4 py-2 uppercase tracking-widest hover:bg-accent transition-colors"
              :data-item-id="product.id"
              :data-item-price="product.price"
              :data-item-url="'/trgovina'"
              :data-item-description="product.description"
              :data-item-name="product.name"
            >
              Kupi
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Accessories -->
    <div>
      <h2 class="text-2xl font-serif text-primary-dark mb-8 text-center">Dodatki</h2>
      <div class="grid md:grid-cols-4 gap-8 max-w-6xl mx-auto">
        <div v-for="product in accessoryProducts" :key="product.id" class="bg-white p-6 border border-gray-100 shadow-sm hover:shadow-md transition-shadow group">
          <div class="h-48 bg-gray-50 mb-4 flex items-center justify-center text-gray-300">
             <span class="text-xs uppercase tracking-widest">Dodatek</span>
          </div>
          <h3 class="text-lg font-serif text-primary-dark mb-2">{{ product.name }}</h3>
          <p class="text-gray-500 text-sm mb-3 min-h-[40px]">{{ product.description }}</p>
          <div class="flex justify-between items-center pt-3 border-t border-gray-100">
            <span class="text-lg font-bold text-accent">{{ product.price.toFixed(2) }} €</span>
            <button 
              class="snipcart-add-item bg-primary-dark text-white text-xs px-4 py-2 uppercase tracking-widest hover:bg-accent transition-colors"
              :data-item-id="product.id"
              :data-item-price="product.price"
              :data-item-url="'/trgovina'"
              :data-item-description="product.description"
              :data-item-name="product.name"
            >
              Kupi
            </button>
          </div>
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
  // Accessories
  {
    id: 'clean-kit-premium',
    name: 'Premium Čistilni Set',
    description: 'Sprej za čiščenje (50ml) in krpica iz mikrovlaken v etuiju.',
    price: 12.00,
    category: 'accessories'
  },
  {
    id: 'chain-gold',
    name: 'Verižica "Elegance" - Zlata',
    description: 'Elegantna pozlačena verižica za korekcijska očala.',
    price: 25.00,
    category: 'accessories'
  },
  {
    id: 'anti-fog-spray',
    name: 'Sprej Proti Rosenju',
    description: 'Učinkovita zaščita pred rosenjem stekel (30ml).',
    price: 9.50,
    category: 'accessories'
  },
  {
    id: 'case-leather',
    name: 'Usnjen Etui - Črn',
    description: 'Ročno izdelan etui iz pravega usnja za varno shranjevanje.',
    price: 35.00,
    category: 'accessories'
  },
  // Vintage Collection
  {
    id: 'vintage-round-gold',
    name: 'Vintage Okrogla - Zlata',
    description: 'Klasična okrogla oblika iz 60-ih let. Pravo zlato prevleka.',
    price: 145.00,
    category: 'vintage'
  },
  {
    id: 'vintage-aviator-silver',
    name: 'Vintage Aviator - Srebrna',
    description: 'Originalni pilotski stil iz 70-ih. Popolnoma obnovljeni.',
    price: 165.00,
    category: 'vintage'
  },
  {
    id: 'vintage-cat-eye',
    name: 'Vintage Cat-Eye - Črna',
    description: 'Ikonična ženska oblika iz 50-ih let. Acetat okvir.',
    price: 125.00,
    category: 'vintage'
  },
  {
    id: 'vintage-browline',
    name: 'Vintage Browline - Tortoise',
    description: 'Klasični "clubmaster" stil iz 80-ih. Odlično ohranjen.',
    price: 155.00,
    category: 'vintage'
  }
]

const vintageProducts = computed(() => products.filter(p => p.category === 'vintage'))
const accessoryProducts = computed(() => products.filter(p => p.category === 'accessories'))
</script>

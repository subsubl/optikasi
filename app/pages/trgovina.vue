<template>
  <div class="py-24 container mx-auto px-6">
    <div class="text-center mb-16">
      <h1 class="text-4xl text-primary-dark mb-4">Spletna Trgovina</h1>
      <p class="text-gray-500 tracking-wide">Vrhunski dodatki in vintage očala. Naročite in prejmite na dom.</p>
    </div>

    <!-- Vintage Collection -->
    <div class="mb-20" v-if="vintageProducts.length">
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
    <div v-if="accessoryProducts.length">
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

    <!-- Sport Collection -->
    <div class="mt-20">
      <h2 class="text-2xl font-serif text-primary-dark mb-8 text-center">
        <span class="text-accent">✦</span> Športna Očala (Uvex) <span class="text-accent">✦</span>
      </h2>
      <div class="grid md:grid-cols-4 gap-8 max-w-6xl mx-auto">
        <div v-for="product in sportProducts" :key="product.id" class="bg-white p-6 border border-gray-100 shadow-sm hover:shadow-md transition-shadow group">
          <div class="h-48 bg-gray-50 mb-4 flex items-center justify-center overflow-hidden">
             <img :src="product.image" :alt="product.name" class="h-full w-full object-contain group-hover:scale-105 transition-transform duration-500" loading="lazy" />
          </div>
          <h3 class="text-lg font-serif text-primary-dark mb-2">{{ product.name }}</h3>
          <p class="text-gray-500 text-sm mb-3 min-h-[40px]">{{ product.description }}</p>
          <div class="flex justify-between items-center pt-3 border-t border-gray-100">
            <span class="text-lg font-bold text-accent">Pošlji povpraševanje</span>
             <a href="mailto:info@optikasi.si?subject=Povpraševanje za Uvex" 
               class="bg-primary-dark text-white text-xs px-4 py-2 uppercase tracking-widest hover:bg-accent transition-colors">
               Info
             </a>
          </div>
        </div>
      </div>
    </div>

    <!-- Naroči Leče Section -->
    <section class="mt-20 py-16 bg-primary-dark text-center">
      <div class="container mx-auto px-6 max-w-3xl">
        <h2 class="text-3xl font-serif text-white mb-4">Potrebujete Kontaktne Leče?</h2>
        <p class="text-gray-300 mb-8">
          Hitro in enostavno naročite vaše kontaktne leče brez čakanja v vrsti.
        </p>
        <NuxtLink 
          to="/narocilo-lec" 
          class="inline-block bg-accent text-white px-10 py-4 uppercase tracking-widest hover:bg-accent-light transition-colors"
        >
          Naroči Leče
        </NuxtLink>
      </div>
    </section>
    
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
  // Accessories - Hidden
  /*
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
  // Vintage Collection - Hidden
  {
    id: 'vintage-round-gold',
    name: 'Vintage Okrogla - Zlata',
    description: 'Klasična okrogla oblika iz 60-ih let. Pozlačeno s pravim zlatom.',
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
    description: 'Ikonična ženska oblika iz 50-ih let. Okvir iz acetata.',
    price: 125.00,
    category: 'vintage'
  },
  {
    id: 'vintage-browline',
    name: 'Vintage Browline - Tortoise',
    description: 'Klasični "clubmaster" stil iz 80-ih. Odlično ohranjen.',
    price: 155.00,
    category: 'vintage'
  },
  */
  // Sport Collection
  {
    "id": "sport-0",
    "name": "Uvex Sportstyle",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-sport-0.jpg"
  },
  {
    "id": "6130371",
    "name": "uvex RXd 4001 blue mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130371.jpg"
  },
  {
    "id": "6130359",
    "name": "uvex RXd 4001 red mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130359.jpg"
  },
  {
    "id": "6130369",
    "name": "uvex RXd 4001 blue-grey",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130369.jpg"
  },
  {
    "id": "6130370",
    "name": "uvex RXd 4001 blue mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130370.jpg"
  },
  {
    "id": "6130368",
    "name": "uvex RXd 4001 red mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130368.jpg"
  },
  {
    "id": "6130365",
    "name": "uvex RXd 4001 planet -gold mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130365.jpg"
  },
  {
    "id": "6130341",
    "name": "uvex RXd 4003 red mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130341.jpg"
  },
  {
    "id": "6130358",
    "name": "uvex RXd 400 3 green mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130358.jpg"
  },
  {
    "id": "6130366",
    "name": "uvex RXd 4003 planet -gold mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130366.jpg"
  },
  {
    "id": "6130372",
    "name": "uvex RXd 400 4 khaki-red mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130372.jpg"
  },
  {
    "id": "6130346",
    "name": "uvex RXd 4004 grey mat",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130346.jpg"
  },
  {
    "id": "6130346",
    "name": "uvex RXd 4004 blue mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130346.jpg"
  },
  {
    "id": "6130377",
    "name": "uvex RXd 4007 grey mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130377.jpg"
  },
  {
    "id": "6130378",
    "name": "uvex RXd 4007 orange mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130378.jpg"
  },
  {
    "id": "6130379",
    "name": "uvex RXd 4008 blue mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130379.jpg"
  },
  {
    "id": "6130380",
    "name": "uvex RXd 4008 plasma mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130380.jpg"
  },
  {
    "id": "6130381",
    "name": "uvex RXd 4009 havanna brown",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130381.jpg"
  },
  {
    "id": "6130382",
    "name": "uvex RXd 4009 violet mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130382.jpg"
  },
  {
    "id": "6130200",
    "name": "uvex RXc 4200 rose mirrorr",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130200.jpg"
  },
  {
    "id": "6130201",
    "name": "uvex RXc 4200 gold mirrorr",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130201.jpg"
  },
  {
    "id": "6130202",
    "name": "uvex RXc 4200 moder mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130202.jpg"
  },
  {
    "id": "6130408",
    "name": "uvex RXs 4302 yellow mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130408.jpg"
  },
  {
    "id": "6130410",
    "name": "uvex RXi 4303 red mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130410.jpg"
  },
  {
    "id": "6130409",
    "name": "uvex RXd 4302 lavender",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130409.jpg"
  },
  {
    "id": "6130407",
    "name": "uvex RXs 4301 violet mat",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130407.jpg"
  },
  {
    "id": "6130403",
    "name": "uvex RXs 4301 blue mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130403.jpg"
  },
  {
    "id": "6130404",
    "name": "uvex RXs 4301 gold mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130404.jpg"
  },
  {
    "id": "6130405",
    "name": "uvex RXs 4301 black-yellow",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130405.jpg"
  },
  {
    "id": "6130400",
    "name": "uvex RXs 4300 khaki-red mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130400.jpg"
  },
  {
    "id": "6130402",
    "name": "uvex RXs 4300 grey-black",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130402.jpg"
  },
  {
    "id": "6130406",
    "name": "uvex RXs 4300 silver mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130406.jpg"
  },
  {
    "id": "6130401",
    "name": "uvex RXs 4300 blue mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130401.jpg"
  },
  {
    "id": "6130356",
    "name": "uvex RXi 4104 plasma mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130356.jpg"
  },
  {
    "id": "6130367",
    "name": "uvex RXi 4104 blue mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130367.jpg"
  },
  {
    "id": "6130357",
    "name": "uvex RXi 4104 red mirror",
    "description": "Športna dioptrijska očala Uvex. Nelomljiv okvir, vrhunska zaščita.",
    "price": 0,
    "category": "sport",
    "image": "/images/shop/sport/uvex-6130357.jpg"
  }
]

const vintageProducts = computed(() => products.filter(p => p.category === 'vintage'))
const accessoryProducts = computed(() => products.filter(p => p.category === 'accessories'))
const sportProducts = computed(() => products.filter(p => p.category === 'sport'))
</script>

<template>
  <section class="py-24 bg-cream">
    <div class="container mx-auto px-6">
      <div class="text-center mb-16">
        <span class="text-accent uppercase tracking-widest text-sm font-bold mb-4 block">Mnenja Strank</span>
        <h2 class="text-4xl text-primary-dark mb-4 font-serif">Kaj Pravijo Naše Stranke</h2>
        <div class="w-16 h-1 bg-accent mx-auto mt-6"></div>
      </div>

      <div class="grid md:grid-cols-3 gap-12">
        <div v-for="(review, index) in reviews" :key="index" class="bg-white p-8 border border-gray-100 shadow-sm relative">
          <!-- Quote Icon -->
          <div class="absolute -top-4 -left-4 text-accent opacity-20 text-6xl font-serif">"</div>

          <p class="text-gray-600 leading-relaxed mb-6 italic relative z-10">
            {{ review.text }}
          </p>

          <div class="flex items-center">
            <div class="w-10 h-10 bg-primary-light rounded-full flex items-center justify-center text-white font-serif font-bold mr-4">
              {{ review.author.charAt(0) }}
            </div>
            <div>
              <h4 class="text-primary-dark font-bold text-sm uppercase tracking-wide">{{ review.author }}</h4>
              <div class="flex text-accent text-xs">
                <span v-for="i in 5" :key="i">★</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const reviews = [
  {
    author: 'Maja K.',
    text: 'Izjemno strokovno in prijazno osebje. Vzeli so si čas za natančen pregled in mi pomagali izbrati okvir, ki mi res pristaja. Toplo priporočam!'
  },
  {
    author: 'Peter Z.',
    text: 'Najboljša optika v Ljubljani. Individualni pristop se res pozna. Očala so vrhunska, pregled pa je bil opravljen brez hitenja. Hvala Optika SI!'
  },
  {
    author: 'Ana L.',
    text: 'Navdušena sem nad izbiro okvirjev in strokovnostjo. Prostor je čudovit in počutila sem se res posebno. Zagotovo se še vrnem.'
  }
]
</script>

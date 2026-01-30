<template>
  <div class="py-24 container mx-auto px-6">
    <div class="text-center max-w-3xl mx-auto mb-16">
      <h1 class="text-4xl text-primary-dark mb-6">Cenik Storitev</h1>
      <p class="text-gray-600 leading-relaxed">
        Transparentne cene za vrhunske storitev. Pri OptikaSI verjamemo v poštenost in kakovost brez skritih stroškov.
        Ob nakupu korekcijskih očal so osnovni pregledi vida <span class="text-accent font-bold">brezplačni</span>.
      </p>
    </div>

    <div class="grid md:grid-cols-2 gap-12 max-w-5xl mx-auto">
      
      <!-- Examinations -->
      <div class="bg-white p-8 shadow-sm border border-gray-100">
        <h2 class="text-2xl font-serif text-primary-dark mb-8 border-b border-gray-100 pb-4">Pregledi in Svetovanje</h2>
        <div class="space-y-6">
          <div v-for="(item, index) in exams" :key="index" class="flex justify-between items-baseline group">
            <div class="flex-grow">
              <span class="text-gray-800 font-medium group-hover:text-primary transition-colors">{{ item.name }}</span>
              <p v-if="item.note" class="text-xs text-gray-500 mt-1">{{ item.note }}</p>
            </div>
            <div class="text-accent font-bold ml-4 whitespace-nowrap">{{ item.price }}</div>
          </div>
        </div>
      </div>

      <!-- Repairs & Maintenance -->
      <div class="bg-white p-8 shadow-sm border border-gray-100">
        <h2 class="text-2xl font-serif text-primary-dark mb-8 border-b border-gray-100 pb-4">Servis in Popravila</h2>
        <div class="space-y-6">
           <div v-for="(item, index) in repairs" :key="index" class="flex justify-between items-baseline group">
            <div class="flex-grow">
              <span class="text-gray-800 font-medium group-hover:text-primary transition-colors">{{ item.name }}</span>
            </div>
            <div class="text-accent font-bold ml-4 whitespace-nowrap">{{ item.price }}</div>
          </div>
        </div>
         <div class="mt-8 bg-cream p-6 rounded-sm text-center">
            <p class="text-sm text-gray-600">Manjša popravila in čiščenje so za naše stranke <span class="font-bold text-primary">brezplačna</span>.</p>
        </div>
      </div>

    </div>
    
    <div class="text-center mt-16">
       <p class="text-xs text-gray-400 uppercase tracking-widest mb-4">Cene vključujejo DDV. Veljavnost cenika od 1. 1. 2025.</p>
       <NuxtLink to="/kontakt" class="inline-block border-b border-primary text-primary hover:text-accent hover:border-accent transition-colors pb-1">Naročite se na pregled &rarr;</NuxtLink>
    </div>

  </div>
</template>

<script setup>
useHead({
  title: 'Cenik - OptikaSI',
  meta: [
    { name: 'description', content: 'Cenik pregledov vida in popravil očal v OptikaSI.' }
  ]
})

const exams = [
  { name: 'Osnovni pregled vida', price: '35,00 €', note: 'Najnižja cena v Ljubljani! Brezplačno ob nakupu.' },

  { name: 'Pregled za vozniški izpit', price: '40,00 €', note: 'Izdaja zdravniškega potrdila.' },
  { name: 'Svetovanje pri izbiri okvirja', price: 'Brezplačno', note: 'Strokovna pomoč stilista.' }
]

const repairs = [
  { name: 'Ultrazvočno čiščenje očal', price: '5,00 €' },
  { name: 'Menjava vijaka ali matice', price: '3,00 €' },
  { name: 'Menjava nosnikov (par)', price: '6,00 €' },
  { name: 'Ravnanje in prilagoditev okvirja', price: '10,00 €' },
  { name: 'Lotanje kovinskega okvirja', price: '25,00 €' },
  { name: 'Menjava najlona (na steklo)', price: '10,00 €' },
  { name: 'Prestavitev stekel v nov okvir', price: '35,00 €' },
]
</script>

<template>
  <div class="py-24 container mx-auto px-6">
    <div class="text-center max-w-3xl mx-auto mb-16">
      <h1 class="text-4xl font-serif text-primary-dark mb-6">Cenik Storitev - Optika Ljubljana</h1>
      <p class="text-gray-600 leading-relaxed">
        Transparentne cene za vrhunske storitve. Pri OptikaSI verjamemo v poštenost in kakovost brez skritih stroškov.
        Ob nakupu korekcijskih očal so osnovni pregledi vida <span class="text-accent font-bold">brezplačni</span>. Zagotovite si <strong>najcenejši pregled vida v Ljubljani</strong> z vrhunsko obravnavo.
      </p>
    </div>

    <div class="grid md:grid-cols-2 gap-12 max-w-5xl mx-auto">
      
      <!-- Examinations -->
      <div class="bg-white p-8 shadow-sm border border-gray-100 flex flex-col justify-between">
        <div>
          <h2 class="text-2xl font-serif text-primary-dark mb-8 border-b border-gray-100 pb-4">Cena pregleda vida in svetovanja</h2>
          <div class="space-y-6">
            <div v-for="(item, index) in exams" :key="index" class="flex justify-between items-baseline group border-b border-gray-50 pb-4 last:border-b-0">
              <div class="flex-grow pr-4">
                <div class="flex items-center gap-2">
                  <span class="text-gray-800 font-medium group-hover:text-primary transition-colors">{{ item.name }}</span>
                </div>
                <p v-if="item.note" class="text-xs text-gray-500 mt-1">{{ item.note }}</p>
                <NuxtLink
                  v-if="item.serviceId"
                  :to="{ path: '/kontakt', query: { service: item.serviceId } }"
                  class="inline-block mt-2 text-xs uppercase tracking-wider font-bold text-accent hover:text-primary transition-colors focus-visible:ring-2 focus-visible:ring-accent focus:outline-none rounded-sm"
                >
                  Naroči se na termin &rarr;
                </NuxtLink>
              </div>
              <div class="text-accent font-bold whitespace-nowrap text-right">{{ item.price }}</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Repairs & Maintenance -->
      <div class="bg-white p-8 shadow-sm border border-gray-100 flex flex-col justify-between">
        <div>
          <h2 class="text-2xl font-serif text-primary-dark mb-8 border-b border-gray-100 pb-4">Servis in Popravila</h2>
          <div class="space-y-6">
             <div v-for="(item, index) in repairs" :key="index" class="flex justify-between items-baseline group">
              <div class="flex-grow">
                <span class="text-gray-800 font-medium group-hover:text-primary transition-colors">{{ item.name }}</span>
              </div>
              <div class="text-accent font-bold ml-4 whitespace-nowrap">{{ item.price }}</div>
            </div>
          </div>
        </div>
        <div class="mt-8 bg-cream p-6 rounded-sm text-center">
          <p class="text-sm text-gray-600">Manjša popravila in čiščenje so za naše stranke <span class="font-bold text-primary">brezplačna</span>.</p>
        </div>
      </div>

    </div>

    <!-- FAQ Section -->
    <section class="max-w-4xl mx-auto mt-24">
      <div class="text-center mb-12">
        <h2 class="text-3xl font-serif text-primary-dark mb-4">Pogosta Vprašanja o Ceniku in Pregledih</h2>
        <p class="text-gray-500">Vse, kar morate vedeti pred obiskom naše optike.</p>
      </div>

      <div class="space-y-6">
        <div v-for="(faq, index) in faqs" :key="index" class="bg-white p-6 border border-gray-100 shadow-sm rounded-sm">
          <h3 class="font-serif text-lg text-primary-dark mb-2 font-bold">{{ faq.question }}</h3>
          <p class="text-gray-600 text-sm leading-relaxed">{{ faq.answer }}</p>
        </div>
      </div>
    </section>
    
    <div class="text-center mt-16">
       <p class="text-xs text-gray-400 uppercase tracking-widest mb-4">Cene vključujejo DDV. Veljavnost cenika od 1. 1. 2026.</p>
       <NuxtLink to="/kontakt" class="inline-block border-b border-primary text-primary hover:text-accent hover:border-accent transition-colors pb-1 focus-visible:ring-2 focus-visible:ring-accent focus:outline-none rounded-sm">Naročite se na pregled &rarr;</NuxtLink>
    </div>

  </div>
</template>

<script setup>
const faqs = [
  {
    question: 'Ali je pregled vida res brezplačen ob nakupu očal?',
    answer: 'Da. Ob nakupu kompletnih korekcijskih očal (okvir + stekla) je celoten strokovni pregled vida (vrednost 35 €) za vas popolnoma brezplačen.'
  },
  {
    question: 'Koliko časa traja pregled vida?',
    answer: 'Za vsako stranko si vzamemo do 60 minut. To nam omogoča temeljito meritev dioptrije, preverjanje ostrine vida na daljavo in bližino ter podroben posvet o najboljših steklih za vaš način življenja.'
  },
  {
    question: 'Zakaj je termin 1-na-1 velika prednost?',
    answer: 'V Studio Optika Si vsak termin rezerviramo izključno za vas. Vrata optike so v času vašega obiska zaprta za druge stranke, kar zagotavlja 100 % zasebnost, mir in strokovno posvečenost brez motečih dejavnikov.'
  },
  {
    question: 'Kako se lahko naročim na pregled?',
    answer: 'Naročite se lahko hitro preko našega spletnega obrazca na strani Kontakt, po e-pošti na info@optikasi.si ali s klicem na telefonsko številko 041 788 516.'
  }
]

const faqSchema = {
  '@context': 'https://schema.org',
  '@type': 'FAQPage',
  'mainEntity': faqs.map(faq => ({
    '@type': 'Question',
    'name': faq.question,
    'acceptedAnswer': {
      '@type': 'Answer',
      'text': faq.answer
    }
  }))
}

useHead({
  title: 'Cenik Storitev | Najcenejši Pregled Vida v Ljubljani | Optika Si',
  meta: [
    { name: 'description', content: 'Preverite naš cenik. Najugodnejša cena pregleda vida v Ljubljani (35€) in brezplačno svetovanje ob nakupu očal. Transparentne cene servisa in popravil.' },
    { name: 'keywords', content: 'cena pregleda vida, najcenejši pregled vida ljubljana, cenik optika, servis očal cena, optika ljubljana' }
  ],
  script: [
    {
      type: 'application/ld+json',
      children: JSON.stringify(faqSchema)
    }
  ]
})

const exams = [
  { name: 'Osnovni pregled vida', price: '35,00 €', note: 'Najnižja cena v Ljubljani! Brezplačno ob nakupu očal.', serviceId: 'pregled-vida' },
  { name: 'Pregled za vozniški izpit', price: '40,00 €', note: 'Izdaja zdravniškega potrdila za CPP.', serviceId: 'pregled-vozniski' },
  { name: 'Svetovanje pri izbiri okvirja', price: 'Brezplačno', note: 'Strokovna pomoč stilista in optometrista.', serviceId: 'svetovanje-okvirji' }
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

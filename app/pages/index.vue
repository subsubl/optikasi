<template>
  <div>
    <!-- Hero Section -->
    <section class="relative h-[80vh] flex items-center justify-center bg-primary-dark overflow-hidden">
      <!-- Placeholder for Hero Image (Using gradient for now) -->
      <div class="absolute inset-0 bg-gradient-to-br from-primary-dark to-black opacity-80" />
      <div class="relative z-10 text-center px-6 max-w-4xl mx-auto">
         <h1 class="font-serif text-5xl md:text-7xl text-white mb-6 tracking-wide leading-tight">
          Butična Optika v Ljubljani
        </h1>
        <p class="text-cream text-lg md:text-xl tracking-widest font-light mb-10 max-w-2xl mx-auto">
          Strokovni pregledi vida, vrhunska korekcijska očala in osebno svetovanje brez čakanja.
        </p>
        <NuxtLink to="/kontakt" class="inline-block border border-accent text-accent hover:bg-accent hover:text-white px-8 py-3 uppercase tracking-[0.2em] transition-all duration-300">
          Rezervirajte Termin
        </NuxtLink>
      </div>
    </section>

    <!-- Intro Section -->
    <section class="py-24 bg-white">
      <div class="container mx-auto px-6 text-center max-w-3xl">
        <span class="text-accent uppercase tracking-widest text-sm font-bold mb-4 block">Optika Ljubljana - Bežigrad</span>
        <h2 class="text-4xl text-primary-dark mb-8">Strokovnost, Eleganca in Zasebnost</h2>
        <p class="text-gray-600 leading-relaxed text-lg mb-8">
          V Studio Optika Si verjamemo, da si vsak par oči zasluži posebno pozornost. Pri nas niste le številka. S pomočjo pogovora in celostne obravnave se trudimo priti do izbire očal, ki bodo zagotovila kakovostno in udobno uporabo.
        </p>
        <p class="text-primary-dark font-serif text-xl italic mb-8">
          "Vsaka stranka ima svoj termin. Brez gneče, brez čakanja. Samo vi in vaša popolna očala."
        </p>
        <div class="w-16 h-1 bg-accent mx-auto"></div>
      </div>
    </section>

    <!-- Why Us Section (New) -->
    <section class="py-24 bg-primary-dark text-white">
      <div class="container mx-auto px-6">
        <div class="grid md:grid-cols-2 gap-16 items-center">
          <div>
            <span class="text-accent uppercase tracking-widest text-sm font-bold mb-4 block">Zakaj Studio Optika SI?</span>
            <h2 class="text-4xl font-serif mb-6 text-white">Prostor, namenjen samo vam</h2>
            <p class="text-cream opacity-90 leading-relaxed mb-6">
              V hitrem tempu sodobnega življenja si vzamemo čas. Pri nas ni čakalnih vrst in hitenja. Kot <strong>butična optika v Ljubljani</strong> na Vojkovi cesti, vsak termin rezerviramo izključno za vas.
            </p>
            <ul class="space-y-4 mb-8">
              <li class="flex items-center space-x-3">
                <span class="text-accent">✦</span>
                <span class="text-sm tracking-wide"><strong>100% Zasebnost</strong> med pregledom in izbiro</span>
              </li>
              <li class="flex items-center space-x-3">
                <span class="text-accent">✦</span>
                <span class="text-sm tracking-wide"><strong>Svetovanje pri izbiri očal</strong> brez motenj</span>
              </li>
              <li class="flex items-center space-x-3">
                <span class="text-accent">✦</span>
                <span class="text-sm tracking-wide">Prilagodljivi termini (tudi večeri in vikendi)</span>
              </li>
            </ul>
             <NuxtLink to="/kontakt" class="text-accent border-b border-accent pb-1 hover:text-white hover:border-white transition-colors uppercase text-xs tracking-widest">
              Dogovorite se za obisk →
            </NuxtLink>
          </div>
          <div class="relative h-96 bg-gray-800 border border-gray-700 rounded-lg shadow-md overflow-hidden">
             <img src="/images/shop/studio-optika-si.png" alt="Studio Optika Si Interior - Butična Optika Bežigrad" class="w-full h-full object-cover" />
          </div>
        </div>
      </div>
    </section>

    <!-- USP Comparison Table -->
    <section class="py-24 bg-white">
      <div class="container mx-auto px-6 max-w-4xl">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-serif text-primary-dark mb-4">Drugačna izkušnja pregleda</h2>
          <p class="text-gray-500">Zakaj izbrati butični pristop 1-na-1 za vaš vid?</p>
        </div>
        
        <div class="overflow-x-auto border border-gray-100 shadow-sm rounded-lg">
          <table class="w-full text-left">
            <thead>
              <tr class="bg-cream">
                <th class="p-6 font-serif text-lg text-primary-dark border-b border-gray-100">Lastnost</th>
                <th class="p-6 font-serif text-lg text-primary-dark border-b border-gray-100 bg-accent/5">Studio Optika Si</th>
                <th class="p-6 font-serif text-lg text-gray-400 border-b border-gray-100">Veliki centri</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-50">
              <tr>
                <td class="p-6 font-medium">Čas za stranko</td>
                <td class="p-6 bg-accent/5 font-bold text-primary-dark">60 minut (brez hitenja)</td>
                <td class="p-6 text-gray-500 text-sm">15 - 20 minut</td>
              </tr>
              <tr>
                <td class="p-6 font-medium">Zasebnost</td>
                <td class="p-6 bg-accent/5 font-bold text-primary-dark">Popolna (vrata so zaprta za vas)</td>
                <td class="p-6 text-gray-500 text-sm">Vrvež drugih kupcev</td>
              </tr>
              <tr>
                <td class="p-6 font-medium">Svetovanje</td>
                <td class="p-6 bg-accent/5 font-bold text-primary-dark">Individualno (stilist + optometrist)</td>
                <td class="p-6 text-gray-500 text-sm">Standardna prodaja</td>
              </tr>
              <tr>
                <td class="p-6 font-medium">Cena</td>
                <td class="p-6 bg-accent/5 font-bold text-accent">Najnižja v Ljubljani</td>
                <td class="p-6 text-gray-500 text-sm">Višja (visoki stroški najema)</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- Services Grid -->
    <section id="services" class="py-24 bg-cream">
      <div class="container mx-auto px-6">
        <div class="grid md:grid-cols-3 gap-12 text-center">
          <div v-for="(service, index) in services" :key="index" class="p-8 border border-gray-200 hover:border-accent transition-colors bg-white">
             <h3 class="text-xl mb-4 font-serif">{{ service.title }}</h3>
             <p class="text-gray-500 text-sm leading-relaxed mb-4">{{ service.desc }}</p>
             <NuxtLink :to="service.link" class="text-accent text-xs uppercase tracking-widest font-bold hover:underline">Več o tem</NuxtLink>
          </div>
        </div>
      </div>
    </section>

    <!-- New Arrivals -->
    <NewArrivals />
  </div>
</template>

<script setup>
useHead({
  title: 'Optika Ljubljana | Strokovni Pregled Vida & Očala po meri | Studio Optika Si',
  meta: [
    { name: 'description', content: 'Iščete dobro optiko v Ljubljani? Studio Optika Si nudi butičen pristop, natančno merjenje dioptrije in vrhunska korekcijska očala brez čakanja na Vojkovi 58.' },
    { name: 'keywords', content: 'optika ljubljana, pregled vida ljubljana, butična optika, korekcijska očala, progresivna očala, merjenje dioptrije, optik bežigrad, okulist ljubljana' }
  ]
})

const services = [
  { 
    title: 'Korekcijska Očala', 
    desc: 'Široka izbira modnih okvirjev in vrhunskih stekel. Specializirani smo za progresivna očala in očala za računalnik.',
    link: '/korekcijska-ocala'
  },
  { 
    title: 'Kontaktne Leče', 
    desc: 'Svetovanje in uvajanje v nošenje vseh vrst kontaktnih leč za vašo svobodo brez okvirjev.',
    link: '/narocilo-lec'
  },
  { 
    title: 'Pregledi Vida', 
    desc: 'Temeljit okulistični pregled in merjenje dioptrije z najsodobnejšo opremo v zasebnem okolju.',
    link: '/storitve'
  }
]
</script>

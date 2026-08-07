<template>
  <div>
    <!-- Hero Section -->
    <section class="relative h-[60vh] min-h-[500px] flex items-center justify-center bg-gray-900 text-white overflow-hidden">
      <div class="absolute inset-0 z-0">
        <img
          src="/images/shop/studio-optika-si.png"
          alt="Studio Optika Si - Butična optika Ljubljana Bežigrad"
          class="w-full h-full object-cover opacity-50"
        />
      </div>
      <div class="absolute inset-0 bg-gradient-to-br from-primary-dark/80 to-black/60 z-0" />
      <div class="relative z-10 text-center px-6 max-w-4xl">
        <span class="text-accent uppercase tracking-widest text-sm font-bold mb-6 block">Studio Optika Si - Bežigrad</span>
        <h1 class="text-5xl md:text-7xl font-serif mb-8 leading-tight">O Nas</h1>
        <p class="text-xl md:text-2xl font-light text-gray-200 leading-relaxed max-w-2xl mx-auto">
          Butična optika v Ljubljani, kjer sta strokovnost in osebni pristop na prvem mestu.
        </p>
      </div>
    </section>

    <!-- Our Story / Philosophy -->
    <section class="py-24 bg-cream">
      <div class="container mx-auto px-6 max-w-4xl text-center">
        <span class="text-accent uppercase tracking-widest text-sm font-bold mb-4 block">Naša Zgodba</span>
        <h2 class="text-4xl font-serif text-primary-dark mb-8">Optika, zasnovana okoli vas</h2>
        <div class="space-y-6 text-gray-600 leading-relaxed text-lg">
          <p>
            V <strong>Studio Optika SI</strong> verjamemo, da si vsak par oči zasluži posebno pozornost.
            V času, ko so veliki optični centri polni vrveža in hitenja, smo se odločili za drugačno pot —
            <span class="text-accent font-bold">butični, 1-na-1 pristop</span>, kjer niste številka, ampak gost.
          </p>
          <p>
            Vsak termin je rezerviran izključno za vas. Vam na voljo posvetimo toliko časa, kot ga
            potrebujete — brez pritiskov, brez čakalnih vrst. Naša želja ni le prodati očala,
            temveč vam pomagati do izbire, ki bo zagotovila <strong>kakovostno in udobno uporabo</strong>
            ter odražala vaš osebni stil.
          </p>
        </div>
        <div class="w-16 h-1 bg-accent mx-auto mt-12"></div>
      </div>
    </section>

    <!-- Values / Why Us -->
    <section class="py-24 bg-white">
      <div class="container mx-auto px-6">
        <div class="text-center mb-16">
          <span class="text-accent uppercase tracking-widest text-sm font-bold mb-4 block">Kaj nas loči</span>
          <h2 class="text-4xl font-serif text-primary-dark">Naše vrednote</h2>
        </div>
        <div class="grid md:grid-cols-3 gap-12">
          <div v-for="value in values" :key="value.title" class="text-center p-8 border border-gray-100 bg-cream hover:border-accent transition-colors">
            <div class="text-4xl text-accent mb-6">{{ value.icon }}</div>
            <h3 class="text-xl font-serif text-primary-dark mb-4">{{ value.title }}</h3>
            <p class="text-gray-500 text-sm leading-relaxed">{{ value.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Boutique Approach -->
    <section class="py-24 bg-primary-dark text-white">
      <div class="container mx-auto px-6">
        <div class="grid md:grid-cols-2 gap-16 items-center">
          <div>
            <span class="text-accent uppercase tracking-widest text-sm font-bold mb-4 block">Butični pristop</span>
            <h2 class="text-4xl font-serif mb-6 text-white">Prostor, namenjen samo vam</h2>
            <p class="text-cream opacity-90 leading-relaxed mb-8">
              Naša optika na <strong>Vojkovi cesti 58 v Ljubljani (Bežigrad)</strong> je zasnovana tako,
              da se v njej počutite sproščeno in zasebno. Vsak pregled in vsaka izbira očal poteka
              v zaprtem, mirnem okolju — popolna zasebnost brez motenj.
            </p>
            <ul class="space-y-4 mb-8">
              <li v-for="point in approachPoints" :key="point" class="flex items-center space-x-3">
                <span class="text-accent">✦</span>
                <span class="text-sm tracking-wide">{{ point }}</span>
              </li>
            </ul>
            <NuxtLink to="/kontakt" class="text-accent border-b border-accent pb-1 hover:text-white hover:border-white transition-colors uppercase text-xs tracking-widest">
              Rezervirajte svoj termin →
            </NuxtLink>
          </div>
          <div class="relative h-96 bg-gray-800 border border-gray-700 rounded-lg shadow-md overflow-hidden">
            <img src="/images/shop/studio-optika-si.png" alt="Interier Studio Optika SI" class="w-full h-full object-cover" />
          </div>
        </div>
      </div>
    </section>

    <!-- Visit / Location -->
    <section class="py-24 bg-cream">
      <div class="container mx-auto px-6 max-w-5xl">
        <div class="text-center mb-16">
          <span class="text-accent uppercase tracking-widest text-sm font-bold mb-4 block">Obiščite nas</span>
          <h2 class="text-4xl font-serif text-primary-dark">Kje nas najdete</h2>
        </div>
        <div class="grid md:grid-cols-2 gap-12">
          <!-- Address & Hours -->
          <div class="bg-white p-8 border border-gray-100 shadow-sm">
            <h3 class="text-xl font-serif text-primary-dark mb-6">Naslov &amp; Urnik</h3>
            <div class="space-y-4 text-gray-600">
              <div class="flex items-start space-x-3">
                <span class="text-accent mt-1">📍</span>
                <div>
                  <p class="font-medium">Studio Optika SI</p>
                  <p>Vojkova cesta 58</p>
                  <p>1000 Ljubljana, Slovenija</p>
                </div>
              </div>
              <div class="flex items-start space-x-3">
                <span class="text-accent mt-1">📞</span>
                <p>
                  <a href="tel:041788516" class="hover:text-accent">041 788 516</a><br />
                  <a href="mailto:info@optikasi.si" class="hover:text-accent">info@optikasi.si</a>
                </p>
              </div>
              <div class="flex items-start space-x-3">
                <span class="text-accent mt-1">🕒</span>
                <div>
                  <p><strong>Po dogovoru</strong></p>
                  <p class="text-sm">Ponedeljek – Petek: 9:00 – 18:00</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Map / CTA -->
          <div class="bg-white p-8 border border-gray-100 shadow-sm flex flex-col justify-between">
            <div>
              <h3 class="text-xl font-serif text-primary-dark mb-4">V Bežigradu, središču Ljubljane</h3>
              <p class="text-gray-500 leading-relaxed mb-6">
                Nahajamo se v Bežigradu, lahkotno dosegljivi z javnim prevozom in avtomobilom.
                Parkiranje je v bližini, obisk pa rezerviran samo za vas.
              </p>
            </div>
            <NuxtLink
              to="/kontakt"
              class="inline-block bg-primary text-white px-8 py-4 uppercase tracking-[0.2em] text-sm font-bold hover:bg-accent transition-colors text-center"
            >
              Rezervirajte Termin
            </NuxtLink>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
useHead({
  title: 'O Nas | Studio Optika Si - Butična Optika Ljubljana',
  meta: [
    { name: 'description', content: 'Spoznajte Studio Optika Si — butično optiko v Ljubljani (Bežigrad) na Vojkovi cesti 58. Osebni 1-na-1 pristop, vrhunska očala in poglobljen pregled vida brez čakanja.' },
    { name: 'keywords', content: 'optika ljubljana, o nas, studio optika si, butična optika bežigrad, optik vojkova, optika ljubljana bežigrad' }
  ]
})

const values = [
  {
    icon: '✦',
    title: 'Zasebnost',
    desc: 'Vsak termin poteka v zaprtem okolju, namenjenem izključno vam. Brez vrveža, brez motenj.'
  },
  {
    icon: '✦',
    title: 'Čas za vas',
    desc: 'Pregledu in izbiri očal namenimo 60 minut — dovolj časa za natančne meritve in svetovanje.'
  },
  {
    icon: '✦',
    title: 'Strokovnost',
    desc: 'Združujemo izkušnje optika in stilista, da vam svetujemo po meri vašega vida in sloga.'
  }
]

const approachPoints = [
  'Pregled vida 1-na-1, brez hitenja',
  'Individualno svetovanje pri izbiri okvirjev',
  'Vrhunske znamke in stekla',
  'Prilagodljivi termini (tudi večeri in vikendi)',
  'Poštena najnižja cena v Ljubljani'
]
</script>

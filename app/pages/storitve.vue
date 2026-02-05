<template>
  <div>
    <section class="relative h-[60vh] min-h-[500px] flex items-center justify-center bg-gray-900 text-white overflow-hidden">
      <div class="absolute inset-0 z-0">
         <img src="/images/hero_services.png" alt="Pregled vida Ljubljana" class="w-full h-full object-cover opacity-60" />
      </div>
      <div class="relative z-10 text-center px-6 max-w-4xl">
        <span class="text-accent uppercase tracking-widest text-sm font-bold mb-6 block">Optika Ljubljana - Bežigrad</span>
        <h1 class="text-5xl md:text-7xl font-serif mb-8 leading-tight">
          Strokovni Pregled Vida
        </h1>
        <p class="text-xl md:text-2xl font-light text-gray-200 leading-relaxed max-w-2xl mx-auto">
           Pri nas se čas ustavi. Vzamemo si ga posebej za vas in vaše oči. Zagotovite si natančen <strong>pregled vida v Ljubljani</strong> brez čakanja.
        </p>
      </div>
    </section>

    <!-- Philosophy / Intro (From O Nas) -->
    <section class="py-24 bg-cream">
      <div class="container mx-auto px-6 max-w-4xl text-center">
        <h2 class="text-3xl font-serif text-primary-dark mb-8">Zakaj izbrati butični okulistični pregled?</h2>
        <div class="space-y-6 text-gray-600 leading-relaxed text-lg">
          <p>
            <span class="text-accent font-bold">Pozornost in čas bosta namenjena le vam.</span> 
            V sproščenem vzdušju in brez časovnih pritiskov zagotavljamo obravnavo, ki 
            omogoča maksimalno natančnost pri meritvah in izbiri očal.
          </p>
          <p>
            Naš cilj je preprost: združiti vrhunske optične lastnosti z vašim osebnim stilom. 
            <strong>Merjenje dioptrije</strong> ni le tehnični postopek, ampak prvi korak do vašega boljšega počutja.
          </p>
        </div>
      </div>
    </section>

    <!-- Process Timeline -->
    <section class="py-24 bg-white">
      <div class="container mx-auto px-6 max-w-5xl">
        <div class="text-center mb-16">
          <span class="text-accent uppercase tracking-widest text-sm font-bold mb-4 block">Kako Poteka</span>
          <h2 class="text-4xl font-serif text-primary-dark">Vaša Pot do Popolnih Očal</h2>
        </div>
        
        <!-- Desktop Timeline -->
        <div class="hidden md:flex items-start justify-between relative">
          <!-- Connecting Line -->
          <div class="absolute top-8 left-0 right-0 h-0.5 bg-gray-200 z-0"></div>
          
          <div v-for="(step, index) in processSteps" :key="index" class="flex flex-col items-center text-center relative z-10 flex-1">
            <div class="w-16 h-16 rounded-full bg-primary-dark text-white flex items-center justify-center text-2xl mb-4 shadow-lg">
              {{ step.icon }}
            </div>
            <span class="text-xs text-accent font-bold uppercase tracking-widest mb-2">{{ step.step }}</span>
            <h3 class="font-serif text-lg text-primary-dark mb-2">{{ step.title }}</h3>
            <p class="text-gray-500 text-sm leading-relaxed max-w-[180px]">{{ step.desc }}</p>
          </div>
        </div>

        <!-- Mobile Timeline -->
        <div class="md:hidden space-y-8">
          <div v-for="(step, index) in processSteps" :key="index" class="flex items-start space-x-4">
            <div class="w-12 h-12 rounded-full bg-primary-dark text-white flex items-center justify-center text-xl flex-shrink-0 shadow-lg">
              {{ step.icon }}
            </div>
            <div>
              <span class="text-xs text-accent font-bold uppercase tracking-widest">{{ step.step }}</span>
              <h3 class="font-serif text-lg text-primary-dark">{{ step.title }}</h3>
              <p class="text-gray-500 text-sm leading-relaxed">{{ step.desc }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Services Grid -->
    <section class="py-24">
      <div class="container mx-auto px-6 max-w-6xl">
        <div class="text-center mb-20">
             <span class="text-accent uppercase tracking-widest text-sm font-bold mb-4 block">Kaj Ponujamo</span>
             <h2 class="text-4xl font-serif text-primary-dark">Naše Storitve</h2>
        </div>

        <div class="grid md:grid-cols-2 gap-16">
          
          <!-- Service 1 -->
          <div class="group">
            <div class="flex items-start space-x-4 mb-4">
              <span class="text-4xl text-accent">👓</span>
              <div>
                <h2 class="text-2xl font-serif text-primary-dark mb-3">Svetovanje pri izbiri očal</h2>
                <p class="text-gray-600 leading-relaxed">
                  Pomagamo vam izbrati okvir, ki se popolnoma ujema z obliko 
                  vašega obraza in osebnostjo. Na voljo imamo <strong>modne okvirje za očala</strong> priznanih svetovnih znamk in našo lastno linijo.
                </p>
              </div>
            </div>
          </div>

          <!-- Service 2 -->
          <div class="group">
            <div class="flex items-start space-x-4 mb-4">
              <span class="text-4xl text-accent">👁️</span>
              <div>
                <h2 class="text-2xl font-serif text-primary-dark mb-3">Okulistični pregled</h2>
                <p class="text-gray-600 leading-relaxed">
                  Strokovni <strong>okulist v Ljubljani</strong> opravi temeljit pregled zdravja vaših oči. Natančno določimo vašo dioptrijo in svetujemo glede najboljše korekcije za vaš vid.
                </p>
              </div>
            </div>
          </div>

          <!-- Service 3 -->
          <div class="group">
            <div class="flex items-start space-x-4 mb-4">
              <span class="text-4xl text-accent">🔧</span>
              <div>
                <h2 class="text-2xl font-serif text-primary-dark mb-3">Servis in Popravila</h2>
                <p class="text-gray-600 leading-relaxed">
                  Zlomljen tečaj ali zrahljani vijaki? Večino popravil 
                  opravimo takoj. Nudimo tudi ultrazvočno čiščenje in 
                  nastavitev očal za optimalno udobje.
                </p>
              </div>
            </div>
          </div>

          <!-- Service 4 -->
          <div class="group">
            <div class="flex items-start space-x-4 mb-4">
              <span class="text-4xl text-accent">🌅</span>
              <div>
                <h2 class="text-2xl font-serif text-primary-dark mb-3">Progresivna Očala</h2>
                <p class="text-gray-600 leading-relaxed">
                  Strokovna meritev in vgradnja <strong>progresivnih stekel</strong> za mehak prehod 
                  med razdaljami. Garancija na privajanje in vrhunska 
                  tehnologija za vaš oster vid na vse razdalje.
                </p>
              </div>
            </div>
          </div>

          <!-- Service 5 -->
          <div class="group">
            <div class="flex items-start space-x-4 mb-4">
              <span class="text-4xl text-accent">☀️</span>
              <div>
                <h2 class="text-2xl font-serif text-primary-dark mb-3">Sončna očala z dioptrijo</h2>
                <p class="text-gray-600 leading-relaxed">
                  Zaščitite oči s stilom. Širok izbor modnih sončnih očal z UV zaščito 
                  in polarizacijo. Možnost vgradnje sončnih stekel z vašo dioptrijo za brezskrbno poletje.
                </p>
              </div>
            </div>
          </div>

          <!-- Service 6 -->
          <div class="group">
            <div class="flex items-start space-x-4 mb-4">
              <span class="text-4xl text-accent">🎯</span>
              <div>
                <h2 class="text-2xl font-serif text-primary-dark mb-3">Individualna izdelava očal</h2>
                <p class="text-gray-600 leading-relaxed">
                  Vsak okvir prilagodimo vašim anatomskim meram. Tudi najboljša stekla ne pomagajo, če okvir ne sedi pravilno. Brezplačno prilagodimo vsa očala za popolno udobje.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Reviews Section (From O Nas) -->
    <section class="py-24 bg-primary-dark text-white">
      <div class="container mx-auto px-6 max-w-5xl">
        <div class="text-center mb-16">
          <span class="text-accent uppercase tracking-widest text-sm font-bold mb-4 block">Mnenja Strank</span>
          <h2 class="text-3xl font-serif">Zakaj smo dobra optika v Ljubljani</h2>
        </div>
        
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div v-for="(review, index) in testimonials" :key="index" class="bg-white/5 backdrop-blur p-8 border border-white/10 rounded-sm hover:-translate-y-1 transition-transform duration-300 h-full flex flex-col justify-between">
            <div>
              <div class="flex justify-between items-start mb-4">
                <div class="flex text-accent text-sm">★★★★★</div>
                <span class="text-xs text-gray-400 font-mono">{{ review.date }}</span>
              </div>
              <p class="text-gray-300 text-sm leading-relaxed mb-6 italic">
                "{{ review.text }}"
              </p>
            </div>
            <div>
              <p class="text-white font-bold text-sm uppercase tracking-wider mb-1">— {{ review.name }}</p>
              <div class="text-xs text-gray-500 uppercase tracking-widest flex items-center space-x-2">
                <img v-if="review.source === 'Google'" src="https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg" alt="Google" class="h-3 opacity-50 grayscale" />
                <span v-else>{{ review.source }}</span>
              </div>
            </div>
          </div>
        </div>

        <div class="text-center mt-12">
          <a 
            href="https://g.page/r/CQnDsS_hbBdXEB0/review" 
            target="_blank" 
            rel="noopener noreferrer"
            class="inline-flex items-center space-x-3 text-accent hover:text-white transition-colors group"
          >
            <span class="uppercase text-sm tracking-widest font-bold">Preberite vse ocene na Googlu</span>
            <span class="group-hover:translate-x-1 transition-transform">→</span>
          </a>
        </div>
      </div>
    </section>

    <!-- Cenik Link -->
    <section class="py-16 bg-cream text-center">
      <div class="container mx-auto px-6">
        <p class="text-gray-600 mb-4 text-lg">Vas zanimajo cene naših storitev?</p>
        <NuxtLink 
          to="/cenik" 
          class="inline-flex items-center space-x-2 text-primary hover:text-accent transition-colors"
        >
          <span class="uppercase text-sm tracking-widest font-bold">Oglejte si Cenik</span>
          <span>→</span>
        </NuxtLink>
      </div>
    </section>

    <!-- FAQ Section -->
    <section class="py-24 bg-white">
      <div class="container mx-auto px-6 max-w-4xl">
        <div class="text-center mb-16">
          <span class="text-accent uppercase tracking-widest text-sm font-bold mb-4 block">Pogosta Vprašanja</span>
          <h2 class="text-4xl font-serif text-primary-dark">Imate Vprašanja?</h2>
        </div>
        
        <div class="space-y-4">
          <div v-for="(faq, index) in faqs" :key="index" class="border border-gray-200 rounded-lg overflow-hidden">
            <button 
              @click="faq.open = !faq.open"
              class="w-full px-6 py-5 text-left flex justify-between items-center bg-gray-50 hover:bg-gray-100 transition-colors"
            >
              <span class="font-serif text-lg text-primary-dark">{{ faq.question }}</span>
              <span class="text-accent text-xl transition-transform duration-300" :class="{ 'rotate-45': faq.open }">+</span>
            </button>
            <div 
              v-show="faq.open"
              class="px-6 py-5 bg-white text-gray-600 leading-relaxed border-t border-gray-100"
            >
              {{ faq.answer }}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="py-24 bg-white text-center">
      <div class="container mx-auto px-6 max-w-3xl">
        <h2 class="text-4xl font-serif text-primary-dark mb-6">Obiščite Nas</h2>
        <p class="text-gray-600 mb-10 text-lg leading-relaxed">
          Vabimo vas v našo <strong>butično optiko v Ljubljani</strong> na Vojkovi cesti 58. 
          Dovolite, da poskrbimo za vaš vid z osebno noto.
        </p>
        <NuxtLink 
          to="/kontakt" 
          class="inline-block bg-primary text-white px-10 py-4 uppercase tracking-widest text-sm hover:bg-primary-dark transition-colors shadow-lg hover:shadow-xl transform hover:-translate-y-1"
        >
          Rezerviraj Termin
        </NuxtLink>
      </div>
    </section>
  </div>
</template>

<script setup>
useHead({
  title: 'Pregled Vida Ljubljana | Merjenje Dioptrije & Okulist | Optika Si',
  meta: [
    { name: 'description', content: 'Strokovni pregled vida v Ljubljani brez čakanja. Natančno merjenje dioptrije, svetovanje pri izbiri očal in okulistični pregledi v butičnem ambientu Bežigrada.' },
    { name: 'keywords', content: 'optika ljubljana, pregled vida ljubljana, okulist ljubljana, merjenje dioptrije, servis očal, pregled vida cena, butična optika bežigrad' }
  ]
})

const testimonials = [
  {
    name: 'Petra',
    date: '13. 6. 2024',
    source: 'Google',
    text: 'Najboljsa optika dalec naokoli ker: - sta Simona in Matic super profesionalna - znata svetovat in vedno ponudita okvirje, ki stranki dejansko pasejo k obrazu - izbira okvirjev je ogroooomna, vsak bo nasel nekaj zase - ocala res dobis v najkrajsem moznem casu (mene ta del se vedno, po vec kot 10 letih, prav preseneti, ker sta res hitra) - ze ko vstopis se res vidi, da svoje poslanstvo delata s srcem: skrbita za nas najboljsi vid in sik izgled s top ocali ❤ Studio Optika Si vedno priporocim vsakemu, ker nikoli ne razocara. Kar tako naprej 😎'
  },
  {
    name: 'neznan',
    date: '5. 6. 2024',
    source: 'Google',
    text: 'Sem redna stranka lastnice Optike Si že več kot desetletje. Zmeraj sem zadovoljna z njeno strokovnostjo, iskrenostjo in srčnostjo. Zelo dobro svetujejo pri izbiri okvirja očal glede na karektaristike obraza. So zelo hitri, natančni in delo opravijo z nasmehom. Pri njih se vedno počutiš dobrodošlega. Za piko na i pa je še cena zelo prijazna žepu. 🙂 Še se vrnemo ❤️'
  },
  {
    name: 'neznan',
    date: '2. 6. 2024',
    source: 'Google',
    text: 'Velika izbira okvirjev,strokovni nasveti in cenovno dostopno. Simona in Matic vedno pripravljena priskociti na pomoč.'
  },
  {
    name: 'neznan',
    date: '1. 6. 2024',
    source: 'Google',
    text: 'Super optika z ocali, izjemno navdusena od natancnosti pregleda do prilagoditev… zelo vesela!😍'
  },
  {
    name: 'neznan',
    date: '1. 6. 2024',
    source: 'Google',
    text: 'Super optika, ki jo odlikuje strokovnost, izjemna prijaznost, velika izbira očal, oseben pristop in posluh za stranke☺️ vedno se ti posvetijo, si vzamejo čas zate in zagotovijo kvalitetno storitev😁 učki zadovoljni!❤️😎🤓'
  },
  {
    name: 'neznan',
    date: '1. 6. 2024',
    source: 'Google',
    text: 'super optika!'
  },
  {
    name: 'neznan',
    date: '1. 6. 2024',
    source: 'Google',
    text: 'Meni najljubsa optika v mestu, zelo prijazno in domače osebje, ki vedno poskrbi da imam ocala kakrsna si zelim! Ogromna izbira ocal in res domače sproščeno okolje! Se vedno vrnem z nasmeškom 🫶🏼 optika SI super SI!!!'
  },
  {
    name: 'neznan',
    date: '1. 6. 2024',
    source: 'Google',
    text: 'Najboljša Optika! 😍 Oseben pristop, prijaznost na vrhuncu, prilagodljivost in občutek za ljudi!! ❤️'
  }
]

const processSteps = [
  { step: 'Korak 1', icon: '📅', title: 'Rezervacija', desc: 'Pokličite ali sporočite za termin, ki vam ustreza.' },
  { step: 'Korak 2', icon: '👁️', title: 'Pregled', desc: 'Natančen pregled vida s sodobno opremo.' },
  { step: 'Korak 3', icon: '👓', title: 'Izbira', desc: 'Skupaj izberemo popoln okvir za vaš obraz.' },
  { step: 'Korak 4', icon: '🔧', title: 'Prilagoditev', desc: 'Očala prilagodimo za maksimalno udobje.' },
  { step: 'Korak 5', icon: '✨', title: 'Prevzem', desc: 'Vaša nova očala so pripravljena!' }
]

const faqs = reactive([
  { 
    question: 'Koliko časa traja pregled vida?', 
    answer: 'Pregled vida pri nas traja približno 45-60 minut. Vzamemo si čas za natančne meritve in pogovor o vaših potrebah, saj smo butična optika z osebnim pristopom.',
    open: false 
  },
  { 
    question: 'Ali sprejemate naročilnico od drugega optika?', 
    answer: 'Da, seveda. Če imate veljavno naročilnico od očesnega zdravnika ali drugega optika, jo z veseljem upoštevamo pri izdelavi očal.',
    open: false 
  },
  { 
    question: 'Kakšna je garancija na očala?', 
    answer: 'Na vsa očala nudimo 2-letno garancijo za napake materiala in izdelave. Brezplačno prilagodimo očala tudi po nakupu.',
    open: false 
  },
  { 
    question: 'Kako hitro lahko dobim očala?', 
    answer: 'Standardna očala so pripravljena v 3-5 delovnih dneh. Za nujne primere nudimo tudi hitrejšo izdelavo.',
    open: false 
  },
  { 
    question: 'Ali nudite popravila za očala kupljena drugje?', 
    answer: 'Da, opravljamo servis in popravila za vsa očala, ne glede na to, kje so bila kupljena. Večino manjših popravil opravimo takoj.',
    open: false 
  },
  { 
    question: 'Kakšni so načini plačila?', 
    answer: 'Sprejemamo gotovino, vse glavne kreditne kartice in plačilo na obroke. Za večje nakupe je možen tudi dogovor o obročnem plačilu.',
    open: false 
  }
])
</script>

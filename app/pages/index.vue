<template>
  <div>
    <!-- Hero Section -->
    <section class="relative h-[80vh] flex items-center justify-center bg-primary-dark overflow-hidden">
      <img src="/optikasi/images/hero_eyeglasses.png" alt="Hero Image" class="absolute inset-0 w-full h-full object-cover" />
      <div class="absolute inset-0 bg-gradient-to-br from-primary-dark to-black opacity-80" />
      <div class="relative z-10 text-center px-6 max-w-4xl mx-auto">
         <h1 class="font-serif text-5xl md:text-7xl text-white mb-6 tracking-wide leading-tight">
          Optika po vaši meri
        </h1>
        <p class="text-cream text-lg md:text-xl tracking-widest font-light mb-10 max-w-2xl mx-auto">
          Strokovno svetovanje in individualni pristop za popoln pogled in videz.
        </p>
        <NuxtLink to="/kontakt" class="inline-block bg-accent text-primary-dark font-bold hover:bg-white hover:text-primary-dark px-10 py-4 uppercase tracking-[0.2em] transition-all duration-300 shadow-lg transform hover:-translate-y-1">
          Rezervirajte Termin
        </NuxtLink>
      </div>
    </section>

    <!-- Intro Section -->
    <section class="py-24 bg-white">
      <div class="container mx-auto px-6 text-center max-w-3xl">
        <span class="text-accent uppercase tracking-widest text-sm font-bold mb-4 block">O Nas</span>
        <h2 class="text-4xl text-primary-dark mb-8">Strokovnost in Eleganca</h2>
        <p class="text-gray-600 leading-relaxed text-lg mb-8">
          S pomočjo pogovora in celostne obravnave se trudimo priti do izbire očal, ki bodo zagotovila kakovostno in udobno uporabo.
          Potrebno je združiti optične in fizične lastnosti očal, želje posameznika in seveda končni izgled.
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
              V hitrem tempu sodobnega življenja si vzamemo čas. Pri nas ni čakalnih vrst in hitenja. 
              Vsak termin je rezerviran izključno za vas, kar nam omogoča, da se vam popolnoma posvetimo.
            </p>
            <ul class="space-y-4 mb-8">
              <li class="flex items-center space-x-3">
                <span class="text-accent">✦</span>
                <span class="text-sm tracking-wide">100% Zasebnost med pregledom in izbiro</span>
              </li>
              <li class="flex items-center space-x-3">
                <span class="text-accent">✦</span>
                <span class="text-sm tracking-wide">Svetovanje brez motenj in pritiska</span>
              </li>
              <li class="flex items-center space-x-3">
                <span class="text-accent">✦</span>
                <span class="text-sm tracking-wide">Prilagodljivi termini ob večerih ali vikendih</span>
              </li>
            </ul>
             <NuxtLink to="/kontakt" class="text-accent border-b border-accent pb-1 hover:text-white hover:border-white transition-colors uppercase text-xs tracking-widest">
              Dogovorite se za obisk →
            </NuxtLink>
          </div>
          <div class="relative h-96 border border-gray-700">
             <img src="/optikasi/images/shop/studio-optika-si.png" alt="Prostor Butične Optike" class="w-full h-full object-cover" />
          </div>
        </div>
      </div>
    </section>

    <!-- Services Grid -->
    <section id="services" class="py-24 bg-cream">
      <div class="container mx-auto px-6">
        <div class="grid md:grid-cols-3 gap-12 text-center">
          <div v-for="(service, index) in services" :key="index" class="p-8 border border-gray-200 hover:border-accent transition-colors bg-white">
             <h3 class="text-xl mb-4">{{ service.title }}</h3>
             <p class="text-gray-500 text-sm leading-relaxed">{{ service.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- New Arrivals -->
    <NewArrivals />

    <!-- Testimonials -->
    <ClientTestimonials />

    <!-- Direct Booking Section -->
    <section class="py-24 bg-white relative overflow-hidden">
      <div class="absolute inset-0 bg-cream opacity-50 transform -skew-y-3 origin-bottom-right scale-110"></div>
      <div class="container mx-auto px-6 relative z-10">
        <div class="max-w-4xl mx-auto bg-white p-8 md:p-12 shadow-2xl border-t-4 border-accent">
          <div class="text-center mb-10">
            <span class="text-accent uppercase tracking-widest text-sm font-bold mb-4 block">Rezervacija</span>
            <h2 class="text-3xl md:text-4xl text-primary-dark mb-4 font-serif">Naročite se na Pregled</h2>
            <p class="text-gray-500">Izpolnite spodnji obrazec in potrdili bomo vaš termin v najkrajšem možnem času.</p>
          </div>
          <BookingForm />
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
useHead({
  title: 'OptikaSI - Butična optika v Ljubljani',
  meta: [
    { name: 'description', content: 'Strokovno svetovanje in individualni pristop. Optika po vaši meri v Ljubljani na Vojkovi cesti 58.' }
  ]
})

const services = [
  { title: 'Korekcijska Očala', desc: 'Široka izbira okvirjev priznanih blagovnih znamk prilagojena vašemu obrazu.' },
  { title: 'Kontaktne Leče', desc: 'Svetovanje in uvajanje v nošenje kontaktnih leč vseh vrst.' },
  { title: 'Pregledi Vida', desc: 'Natančni pregledi vida s sodobno opremo za optimalno korekcijo.' }
]
</script>

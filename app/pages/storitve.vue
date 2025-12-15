<template>
  <div>
    <!-- Hero Section -->
    <section class="py-24 bg-primary-dark text-white text-center">
      <div class="container mx-auto px-6 max-w-4xl">
        <h1 class="text-5xl font-serif mb-6">Naše Storitve</h1>
        <p class="text-xl text-gray-300 leading-relaxed">
          Strokovna optika z individualnim pristopom. Vsaka storitev je prilagojena vašim edinstvenim potrebam.
        </p>
      </div>
    </section>

    <!-- Intro -->
    <section class="py-20 bg-cream">
      <div class="container mx-auto px-6 max-w-4xl text-center">
        <p class="text-lg text-gray-600 leading-relaxed">
          Pri OptikaSI združujemo desetletja izkušenj z najsodobnejšo tehnologijo. 
          Od izbire popolnega okvirja do natančne izdelave stekel — vsak korak naredimo skupaj z vami.
        </p>
      </div>
    </section>

    <!-- Services Grid -->
    <section class="py-20">
      <div class="container mx-auto px-6 max-w-6xl">
        <div class="grid md:grid-cols-2 gap-16">
          
          <!-- Service 1 -->
          <div class="group">
            <div class="flex items-start space-x-4 mb-4">
              <span class="text-4xl text-accent">👓</span>
              <div>
                <h2 class="text-2xl font-serif text-primary-dark mb-3">Izbira Okvirjev</h2>
                <p class="text-gray-600 leading-relaxed">
                  Vsak obraz je edinstven. Pomagamo vam izbrati okvir, ki se popolnoma ujema z obliko 
                  vašega obraza, osebnim stilom in vsakodnevnimi potrebami. Na voljo imamo več kot 
                  500 modelov priznanih svetovnih znamk.
                </p>
              </div>
            </div>
          </div>

          <!-- Service 2 -->
          <div class="group">
            <div class="flex items-start space-x-4 mb-4">
              <span class="text-4xl text-accent">🔧</span>
              <div>
                <h2 class="text-2xl font-serif text-primary-dark mb-3">Popravila in Servis</h2>
                <p class="text-gray-600 leading-relaxed">
                  Zlomljen tečaj, zrahljani vijaki ali poškodovane blazinice? Večino popravil 
                  opravimo na mestu, medtem ko počakate. Za zahtevnejša popravila nudimo 
                  hitro in zanesljivo storitev.
                </p>
              </div>
            </div>
          </div>

          <!-- Service 3 -->
          <div class="group">
            <div class="flex items-start space-x-4 mb-4">
              <span class="text-4xl text-accent">✨</span>
              <div>
                <h2 class="text-2xl font-serif text-primary-dark mb-3">Vintage Kolekcija</h2>
                <p class="text-gray-600 leading-relaxed">
                  Ljubitelje retro stila vabimo k ogledu naše unikatne kolekcije vintage očal. 
                  Skrbno izbrani kosi iz 50-ih do 80-ih let, obnovljeni in pripravljeni za 
                  novo življenje. Klasika, ki nikoli ne gre iz mode.
                </p>
              </div>
            </div>
          </div>

          <!-- Service 4 -->
          <div class="group">
            <div class="flex items-start space-x-4 mb-4">
              <span class="text-4xl text-accent">🌅</span>
              <div>
                <h2 class="text-2xl font-serif text-primary-dark mb-3">Progresivna Stekla</h2>
                <p class="text-gray-600 leading-relaxed">
                  Strokovna prilagoditev progresivnih stekel zagotavlja mehak prehod med 
                  razdaljami brez vidnih črt. Pomagamo vam izbrati prava stekla za vaš 
                  življenjski slog — od pisarniškega dela do aktivnega prostega časa.
                </p>
              </div>
            </div>
          </div>

          <!-- Service 5 -->
          <div class="group">
            <div class="flex items-start space-x-4 mb-4">
              <span class="text-4xl text-accent">☀️</span>
              <div>
                <h2 class="text-2xl font-serif text-primary-dark mb-3">Sončna Očala</h2>
                <p class="text-gray-600 leading-relaxed">
                  Zaščitite svoje oči s stilom. Ponujamo širok izbor sončnih očal z UV zaščito 
                  in polarizirajočimi stekli. Na voljo tudi z dioptrijo za tiste, ki potrebujejo 
                  korekcijo vida.
                </p>
              </div>
            </div>
          </div>

          <!-- Service 6 -->
          <div class="group">
            <div class="flex items-start space-x-4 mb-4">
              <span class="text-4xl text-accent">🎯</span>
              <div>
                <h2 class="text-2xl font-serif text-primary-dark mb-3">Prilagajanje Okvirjev</h2>
                <p class="text-gray-600 leading-relaxed">
                  Tudi najboljša stekla ne pomagajo, če okvir ne sedi pravilno. Brezplačno 
                  prilagodimo vse okvirje, kupljene pri nas — ter tudi tiste, kupljene drugje. 
                  Udobje je ključ do dolgotrajnega nošenja.
                </p>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- Cenik Link -->
    <section class="py-12 bg-cream text-center">
      <div class="container mx-auto px-6">
        <p class="text-gray-600 mb-4">Zanima vas cenik naših storitev?</p>
        <NuxtLink 
          to="/cenik" 
          class="inline-flex items-center space-x-2 text-primary hover:text-accent transition-colors"
        >
          <span class="uppercase text-sm tracking-widest font-medium">Oglejte si Cenik</span>
          <span>→</span>
        </NuxtLink>
      </div>
    </section>

    <!-- CTA -->
    <section class="py-20 bg-primary-dark text-center">
      <div class="container mx-auto px-6 max-w-3xl">
        <h2 class="text-3xl font-serif text-white mb-6">Obiščite Nas</h2>
        <p class="text-gray-300 mb-8">
          Vabimo vas, da nas obiščete v naši butični optiki. Pokličite nas ali 
          izpolnite obrazec za termin.
        </p>
        <NuxtLink 
          to="/kontakt" 
          class="inline-block bg-accent text-white px-10 py-4 uppercase tracking-widest hover:bg-accent-light transition-colors"
        >
          Kontaktirajte Nas
        </NuxtLink>
      </div>
    </section>
  </div>
</template>

<script setup>
useHead({
  title: 'Storitve - Optika in Očala',
  meta: [
    { name: 'description', content: 'Izbira okvirjev, popravila očal, vintage kolekcija, progresivna stekla in sončna očala. Butična optika v Ljubljani.' },
    { name: 'keywords', content: 'optika ljubljana, očala, okvirji, sončna očala, vintage očala' }
  ]
})
</script>

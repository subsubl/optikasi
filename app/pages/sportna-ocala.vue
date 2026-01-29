<template>
  <div>
    <!-- Hero Section -->
    <section class="relative h-[60vh] min-h-[500px] flex items-center justify-center overflow-hidden">
      <div class="absolute inset-0 z-0">
        <img :src="'/optikasi/images/sport/hero-general.jpg'" alt="Športna Očala" class="w-full h-full object-cover" />
        <div class="absolute inset-0 bg-black/40"></div>
      </div>
      <div class="relative z-10 text-center px-6 max-w-4xl mx-auto text-white">
        <span class="text-accent uppercase tracking-widest text-sm font-bold mb-4 block">Brezkompromisen Vid</span>
        <h1 class="text-5xl md:text-7xl font-serif mb-6">Športna Očala</h1>
        <p class="text-xl md:text-2xl font-light opacity-90 max-w-2xl mx-auto">
          Vrhunska zaščita in popoln vid v vsakem trenutku. Ker v športu šteje vsaka podrobnost.
        </p>
      </div>
    </section>

    <!-- Intro -->
    <section class="py-24 bg-cream">
      <div class="container mx-auto px-6 max-w-4xl text-center">
        <h2 class="text-3xl font-serif text-primary-dark mb-8">Vid je v Športu Ključnega Pomena</h2>
        <p class="text-gray-600 leading-relaxed text-lg mb-8">
          Večina informacij (kar 85%), ki jih potrebujemo za uspešno športno udejstvovanje, prejemamo preko oči. 
          Vrhunska športna očala ne nudijo le zaščite pred UV žarki, vetrom in tujki, ampak z ustreznimi 
          stekli izboljšajo kontrast, globinsko zaznavo in s tem vašo reakcijsko dobo.
        </p>
        <p class="text-gray-600 leading-relaxed text-lg">
          V sodelovanju z blagovno znamko <strong>Uvex</strong> vam nudimo 
          individualno prilagojena športna dioptrijska očala, ki sledijo ukrivljenosti okvirja in 
          zagotavljajo široko vidno polje brez popačevanj.
        </p>
      </div>
    </section>

    <!-- Sports Categories -->
    <section class="py-24">
      <div class="container mx-auto px-6 max-w-6xl">
        <h2 class="text-3xl font-serif text-primary-dark mb-16 text-center">Rešitve za Vaš Šport</h2>
        
        <div class="grid md:grid-cols-2 gap-12">
          <!-- Cycling -->
          <div class="group">
            <div class="relative h-80 overflow-hidden mb-6 rounded-lg">
              <img :src="'/optikasi/images/sport/hero-cycling.jpg'" alt="Kolesarska Očala"
                   class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent flex items-end p-8">
                <h3 class="text-3xl font-serif text-white">Kolesarstvo</h3>
              </div>
            </div>
            <p class="text-gray-600 leading-relaxed">
              Na cesti ali v gozdu – kolesarji potrebujejo zaščito pred vetrom in hitro prilagajanje 
              svetlobnim pogojem. Priporočamo fotokromatska stekla (Variomatic), ki se samodejno 
              zatemnijo, ali Colorvision tehnologijo za boljši kontrast na asfaltu in brezpotjih.
            </p>
          </div>

          <!-- Winter Sports -->
          <div class="group">
            <div class="relative h-80 overflow-hidden mb-6 rounded-lg">
              <img :src="'/optikasi/images/sport/hero-winter.jpg'" alt="Zimska Očala"
                   class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent flex items-end p-8">
                <h3 class="text-3xl font-serif text-white">Zimski Športi</h3>
              </div>
            </div>
            <p class="text-gray-600 leading-relaxed">
              Sneg odbija do 80% UV žarkov. Potrebujete močno zaščito (kategorija 3 ali 4) in 
              stekla, ki povečajo kontrast v megli ali difuzni svetlobi. Naša smučarska očala 
              z dioptrijo zagotavljajo varnost in jasen pogled na strmini.
            </p>
          </div>

          <!-- Running/Hiking -->
          <div class="group">
            <div class="relative h-80 overflow-hidden mb-6 rounded-lg bg-gray-200 flex items-center justify-center">
               <!-- Placeholder or reused image if specific one missing -->
              <span class="text-6xl">🏃</span>
              <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent flex items-end p-8">
                <h3 class="text-3xl font-serif text-white">Tek in Pohodništvo</h3>
              </div>
            </div>
            <p class="text-gray-600 leading-relaxed">
              Lahka in stabilna očala, ki ne drsijo. Pomembno je zračenje, da se očala ne rosijo, 
              in zaščita pred bleščanjem v gorah. Polarizirana stekla so odlična izbira za zmanjšanje 
              odsevov.
            </p>
          </div>

          <!-- Water/General -->
           <div class="group">
            <div class="relative h-80 overflow-hidden mb-6 rounded-lg bg-blue-100 flex items-center justify-center">
               <span class="text-6xl">🌊</span>
              <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent flex items-end p-8">
                <h3 class="text-3xl font-serif text-white">Vodni Športi</h3>
              </div>
            </div>
            <p class="text-gray-600 leading-relaxed">
              Voda in sonce sta močna kombinacija. Obvezna so polarizirana stekla, ki izničijo 
              slepeče odseve z vodne gladine in omogočajo sproščen pogled v daljavo.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Technologies -->
    <section class="py-24 bg-primary-dark text-white">
      <div class="container mx-auto px-6 max-w-6xl">
        <h2 class="text-3xl font-serif mb-16 text-center">Napredna Tehnologija Stekel</h2>
        
        <div class="space-y-24">
          <!-- Variomatic -->
          <div class="grid md:grid-cols-2 gap-12 items-center">
            <div class="order-2 md:order-1">
              <h3 class="text-2xl font-serif text-accent mb-4">Uvex Variomatic®</h3>
              <h4 class="text-xl font-light mb-6 opacity-80">Samodejno prilagajanje svetlobi</h4>
              <p class="text-gray-300 leading-relaxed mb-6">
                Stekla Variomatic se v nekaj sekundah samodejno prilagodijo vsem svetlobnim pogojem. 
                Od svetlega sonca do temnega gozda – vaša očala se zatemnijo ali posvetlijo glede na UV sevanje.
                Pokrivajo zaščitne kategorije od S1 do S3.
              </p>
              <ul class="space-y-2 text-gray-400">
                <li>✓ Brez menjavanja očal</li>
                <li>✓ Popolna zaščita v vsakem vremenu</li>
              </ul>
            </div>
            <div class="order-1 md:order-2 rounded-lg overflow-hidden border border-white/10">
              <img :src="'/optikasi/images/sport/tech-variomatic.jpg'" alt="Variomatic Tehnologija" class="w-full" />
            </div>
          </div>

          <!-- Colorvision -->
          <div class="grid md:grid-cols-2 gap-12 items-center">
             <div class="rounded-lg overflow-hidden border border-white/10">
              <img :src="'/optikasi/images/sport/tech-colorvision.jpg'" alt="Colorvision Tehnologija" class="w-full" />
            </div>
            <div>
              <h3 class="text-2xl font-serif text-accent mb-4">Uvex Colorvision®</h3>
              <h4 class="text-xl font-light mb-6 opacity-80">Ultimativni kontrast</h4>
              <p class="text-gray-300 leading-relaxed mb-6">
                Vidite več. Inovativna tehnologija barvnih filtrov poudari kontraste, ki so v vašem 
                okolju najpomembnejši. Zelena za golf/naravo, rumena za sneg, rjava za cesto. 
                Hitrejše zaznavanje ovir pomeni večjo varnost.
              </p>
              <ul class="space-y-2 text-gray-400">
                <li>✓ Briljantne barve</li>
                <li>✓ Povečana globinska zaznava</li>
              </ul>
            </div>
          </div>

           <!-- Supravision -->
          <div class="grid md:grid-cols-2 gap-12 items-center">
            <div class="order-2 md:order-1">
              <h3 class="text-2xl font-serif text-accent mb-4">Uvex Supravision®</h3>
              <h4 class="text-xl font-light mb-6 opacity-80">Popolnoma brez rosenja</h4>
              <p class="text-gray-300 leading-relaxed mb-6">
                Edinstven premaz proti rosenju na notranji strani stekla zagotavlja jasen pogled 
                tudi med najbolj intenzivnim naporom ali pri velikih temperaturnih spremembah. 
                Premaz je vzdržljiv in optično nevtralen.
              </p>
            </div>
            <div class="order-1 md:order-2 rounded-lg overflow-hidden border border-white/10">
              <img :src="'/optikasi/images/sport/tech-supravision.jpg'" alt="Supravision Tehnologija" class="w-full" />
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Diopter Solutions -->
    <section class="py-24 bg-cream">
       <div class="container mx-auto px-6 max-w-4xl text-center">
        <h2 class="text-3xl font-serif text-primary-dark mb-12">Kako do Športnih Očal z Dioptrijo?</h2>
        <div class="grid md:grid-cols-3 gap-8 text-left">
           <div class="bg-white p-8 border border-gray-100 shadow-sm">
             <h3 class="font-serif text-xl text-primary-dark mb-3">Direktna Vgradnja</h3>
             <p class="text-gray-600 text-sm">
               Najbolj estetska in udobna rešitev. Dioptrijska stekla se vgradijo neposredno v športni okvir. 
               Možno tudi pri ukrivljenih očalih.
             </p>
           </div>
           <div class="bg-white p-8 border border-gray-100 shadow-sm">
             <h3 class="font-serif text-xl text-primary-dark mb-3">Clip-in Vložek</h3>
             <p class="text-gray-600 text-sm">
               Ekonomična rešitev. Notranji okvirček z dioptrijo se vpne v športna očala. 
               Omogoča enostavno menjavo zunanjih stekel.
             </p>
           </div>
           <div class="bg-white p-8 border border-gray-100 shadow-sm">
             <h3 class="font-serif text-xl text-primary-dark mb-3">Flip-up Sistem</h3>
             <p class="text-gray-600 text-sm">
               Klasična očala z dodatnim dvižnim sončnim nastavkom. Primerno za tiste, 
               ki želijo univerzalnost.
             </p>
           </div>
        </div>
       </div>
    </section>

    <!-- CTA -->
    <section class="py-20 text-center">
      <div class="container mx-auto px-6 max-w-3xl">
        <h2 class="text-3xl font-serif text-primary-dark mb-6">Pripravljeni na Akcijo?</h2>
        <p class="text-gray-600 mb-8 leading-relaxed">
          Ne dovolite, da vas slab vid ovira pri vaših dosežkih. Obiščite nas za posvet in izmero, 
          kjer bomo našli idealno rešitev za vaš šport.
        </p>
        <NuxtLink 
          to="/kontakt" 
          class="inline-block bg-primary text-white px-10 py-4 uppercase tracking-widest hover:bg-primary-light transition-colors"
        >
          Rezerviraj Termin za Športna Očala
        </NuxtLink>
      </div>
    </section>
  </div>
</template>

<script setup>
useHead({
  title: 'Športna Očala z Dioptrijo - Uvex in Alcom',
  meta: [
    { name: 'description', content: 'Vrhunska športna očala z dioptrijo. Kolesarska, smučarska in tekaška očala s tehnologijo Variomatic in Colorvision. Uradni partner Alcom in Uvex.' },
    { name: 'keywords', content: 'športna očala, dioptrija, uvex, alcom, kolesarska očala, smučarska očala, variomatic' }
  ]
})
</script>

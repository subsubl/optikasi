<template>
  <div class="py-24 container mx-auto px-6 max-w-4xl">
    <NuxtLink to="/blog" class="text-accent uppercase text-xs tracking-widest mb-8 inline-block hover:text-primary-dark transition-colors">
      ← Nazaj na blog
    </NuxtLink>
    
    <article class="prose prose-lg max-w-none">
      <h1 class="font-serif text-4xl md:text-5xl text-primary-dark mb-8 leading-tight">
        Zakaj je 1-na-1 pregled vida (60 min) ključen za tvoje zdravje?
      </h1>
      
      <div class="h-96 w-full bg-cream mb-12 flex items-center justify-center text-gray-300">
         <img src="/images/hero_services.png" alt="Pregled vida" class="w-full h-full object-cover rounded-lg shadow-sm" />
      </div>

      <p class="text-xl text-gray-600 leading-relaxed mb-8 font-light italic">
        Ste se kdaj vprašali, zakaj nekateri pregledi vida trajajo le 15 minut, drugi pa celo uro? V svetu optike hitrost ni vrlina. V Studio Optika Si verjamemo, da so vaše oči unikatne in si zaslužijo čas, ki ga potrebujejo za popolno diagnozo.
      </p>

      <h2 class="text-2xl font-serif text-primary-dark mt-12 mb-4">1. Brez hitenja, brez napak</h2>
      <p class="text-gray-600 mb-6">
        Pri standardnih pregledih se optometristi pogosto srečujejo s pritiskom časa. Pri nas je vsak termin rezerviran za 60 minut. To pomeni, da se vaše oči sprostijo, meritve pa so zato bolj natančne. Nič več občutka "ugibanja" med lečami. Ko so oči spočite in niso pod stresom hitenja, so rezultati meritve dioptrije bistveno bolj zanesljivi.
      </p>

      <h2 class="text-2xl font-serif text-primary-dark mt-12 mb-4">2. Celostno svetovanje</h2>
      <p class="text-gray-600 mb-6">
        Pregled ni le določanje dioptrije. Je pogovor o vašem življenjskem slogu. Ali veliko časa preživite pred zaslonom? Se ukvarjate s športom? Vozite veliko ponoči? V 60 minutah lahko skupaj ugotovimo, kateri nanosi in tipi stekel bodo dejansko izboljšali vašo kakovost življenja. Naš cilj je, da očala niso le pripomoček, ampak podaljšek vašega vida, ki vas ne omejuje.
      </p>

      <h2 class="text-2xl font-serif text-primary-dark mt-12 mb-4">3. Zasebnost, ki šteje</h2>
      <p class="text-gray-600 mb-6">
        V našem butiku ste v času termina sami. Brez drugih strank, ki bi opazovale vašo izbiro okvirjev ali motile pogovor z optometristom. To ustvari varno okolje, kjer se lahko odkrito pogovorimo o vseh težavah z vidom, od suhih oči do glavobolov. Mirno okolje pripomore k boljši koncentraciji tako stranke kot strokovnjaka.
      </p>

      <div class="my-16 p-8 bg-primary-dark text-white rounded-lg shadow-xl">
         <h3 class="text-2xl font-serif mb-4 italic text-accent">"Vaš vid je dragocen. Ne dovolite, da ga nekdo obravnava kot številko na tekočem traku."</h3>
         <p class="text-cream opacity-80 mb-6">Rezervirajte svoj termin in izkusite razliko, ki jo prinese osebna obravnava.</p>
         <NuxtLink to="/kontakt" class="inline-block bg-accent text-white px-8 py-3 uppercase tracking-widest text-sm hover:bg-accent-light transition-all">Rezerviraj svoj termin</NuxtLink>
      </div>

      <h2 class="text-2xl font-serif text-primary-dark mt-12 mb-4">Zaključek</h2>
      <p class="text-gray-600 mb-8">
        V Studio Optika Si na Vojkovi 58 v Ljubljani smo zavezani kakovosti. Verjamemo, da je ura časa, ki jo posvetimo vašim očem, najboljša naložba v vaš dolgoročni vid. Ne pristajajte na manj, ko gre za vaše zdravje.
      </p>
    </article>
  </div>
</template>

<script setup>
useHead({
  title: 'Zakaj 1-na-1 pregled vida (60 min) ključen za tvoje zdravje? | Blog Optika Si',
  meta: [
    { name: 'description', content: 'Preberite zakaj je 60-minutni pregled vida brez hitenja ključen za natančno dioptrijo in vaše dobro počutje. Studio Optika Si Ljubljana.' }
  ]
})
</script>

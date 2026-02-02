<template>
  <div class="py-24 container mx-auto px-6 max-w-4xl">
    <NuxtLink to="/blog" class="text-accent uppercase text-xs tracking-widest mb-8 inline-block hover:text-primary-dark transition-colors">
      ← Nazaj na blog
    </NuxtLink>
    
    <article class="prose prose-lg max-w-none">
      <h1 class="font-serif text-4xl md:text-5xl text-primary-dark mb-8 leading-tight">
        Vodič po športnih dioptrijskih očalih Uvex – od smučanja do kolesarjenja
      </h1>
      
      <div class="h-96 w-full bg-cream mb-12 flex items-center justify-center text-gray-300">
         <img src="/images/sport/hero-general.jpg" alt="Uvex športna očala" class="w-full h-full object-cover rounded-lg shadow-sm" />
      </div>

      <h2 class="text-2xl font-serif text-primary-dark mt-12 mb-4">Zakaj običajna očala niso primerna za šport?</h2>
      <p class="text-gray-600 mb-6 leading-relaxed">
        Običajni korekcijski okvirji niso zasnovani za ekstremne gibe, znojenje in morebitne udarce. Če se ukvarjate s športom, veste, kako pomembno je, da so očala stabilna in varna. Pri športu potrebujete:
      </p>
      <ul class="list-disc pl-6 mb-8 text-gray-600 space-y-2">
        <li><strong>Stabilnost</strong>: Očala morajo ostati na mestu kljub hitrim gibom glave ali tresljajem.</li>
        <li><strong>Zaščito</strong>: Nelomljivi materiali okvirja in stekel so ključni za preprečevanje poškodb pri morebitnih padcih.</li>
        <li><strong>Vidno polje</strong>: Športna očala imajo pogosto bolj ukrivljeno obliko, kar nudi širši pogled brez popačenj na robovih.</li>
      </ul>

      <h2 class="text-2xl font-serif text-primary-dark mt-12 mb-4">Uvex RX – Revolucija v športni optiki</h2>
      <p class="text-gray-600 mb-6">
        Uvex je svetovni vodja na področju zaščitne in športne opreme. Njihova linija dioptrijskih očal, ki jo ponujamo v sodelovanju s podjetjem Alcom, predstavlja vrhunec tehnologije.
      </p>
      
      <div class="grid md:grid-cols-2 gap-8 my-12">
        <div class="bg-gray-50 p-6 border-l-4 border-accent">
           <h3 class="font-bold text-primary-dark mb-2 text-lg">Nelomljivi okvirji</h3>
           <p class="text-sm text-gray-500">Posebni visokotehnološki polimeri zagotavljajo, da okvirji zdržijo ekstremne obremenitve brez loma.</p>
        </div>
        <div class="bg-gray-50 p-6 border-l-4 border-accent">
           <h3 class="font-bold text-primary-dark mb-2 text-lg">Colorvision®</h3>
           <p class="text-sm text-gray-500">Tehnologija stekel, ki poudari določene barve in izboljša kontrast za hitrejšo reakcijo.</p>
        </div>
      </div>

      <h2 class="text-2xl font-serif text-primary-dark mt-12 mb-4">Kateri model izbrati za svojo aktivnost?</h2>
      <div class="space-y-6 text-gray-600 mb-12">
        <p><strong>Kolesarjenje:</strong> Izberite modele s širokimi, ukrivljenimi stekli, ki ščitijo oči pred vetrom, prahom in mrčesom, hkrati pa nudijo jasen pregled nad cesto ali potjo.</p>
        <p><strong>Smučanje in zimski športi:</strong> Uvex nudi specifične rešitve z vgradnjo dioptrije v smučarske maske ali športne okvirje z visoko kategorijo zatemnitve in zaščito pred bleščanjem snega.</p>
        <p><strong>Tek in igre z žogo:</strong> Ključna je lahkotnost. Ultralahki titan ali specifični acetatni modeli z gumiranimi nosniki bodo ostali na mestu tudi med najbolj intenzivnim gibanjem.</p>
      </div>

      <h2 class="text-2xl font-serif text-primary-dark mt-12 mb-4">Kje jih preizkusiti?</h2>
      <p class="text-gray-600 mb-8">
        V Studio Optika Si smo specialisti za športno optiko. Pridite na posvet na Vojkovo 58 v Ljubljani, kjer bomo skupaj izbrali pravi model Uvex za vašo najljubšo aktivnost. Na voljo imamo širok izbor demo okvirjev, ki jih lahko preizkusite.
      </p>

      <div class="mt-16 text-center border-t border-gray-100 pt-12">
        <NuxtLink to="/kontakt" class="bg-primary-dark text-white px-10 py-4 uppercase tracking-[0.2em] hover:bg-accent transition-all">Naroči se na posvet za športna očala</NuxtLink>
      </div>
    </article>
  </div>
</template>

<script setup>
useHead({
  title: 'Vodič po športnih dioptrijskih očalih Uvex | Blog Optika Si',
  meta: [
    { name: 'description', content: 'Zakaj so športna očala z dioptrijo Uvex najboljša izbira za aktivne? Spoznajte prednosti nelomljivih okvirjev in tehnologije Colorvision.' }
  ]
})
</script>

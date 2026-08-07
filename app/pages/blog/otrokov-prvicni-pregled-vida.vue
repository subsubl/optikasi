<template>
  <div class="max-w-4xl mx-auto px-4 py-8">
    <NuxtLink to="/blog" class="text-primary-dark hover:text-accent flex items-center mb-6">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l4.293 4.293a1 1 0 010 1.414z" clip-rule="evenodd" />
      </svg>
      Nazaj na blog
    </NuxtLink>
    
    <article>
      <h1 class="font-serif text-4xl md:text-5xl text-primary-dark mb-6">Kdaj naj gre otrok prvič na pregled vida?</h1>
      
      <img :src="'/images/hero_services.png'" alt="Otrok na pregledu vida" class="w-full h-96 object-cover rounded-lg mb-8" />
      
      <div class="prose prose-lg max-w-none">
        <p class="mb-4">Pregled vida je ključen za zdravje oči otrok. Pravilno zgodnje zaznavanje očesnih težav omogoča učinkovito zdravljenje in preprečevanje hudega vidnega defekta. V tej objavi bomo razložili, kdaj naj otrok prvič obišče optikala in kakšne znake naj starši opazijo.</p>
        
        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Kdaj naj otrok prvič obišče optikala?</h2>
        <p class="mb-4">Po svetovni zdravstveni organizaciji (WHO) naj otrok obišče optikala prvič pred šolsko dobo, najkasneje do age 3 let. V Sloveniji pa je priporočljivo, da otrok obišče optikala že v starosti 1 leta, če obstajajo kakršnekoli sumi o vidnem razvoju.</p>
        
        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Kakšni so znaki, ki jih morate opaziti?</h2>
        <p class="mb-4">Starši morajo opazovati naslednje znake, ki lahko kažejo na očesne težave:</p>
        <ul class="list-disc pl-6 mb-4">
          <li>Neuspešno spremljanje predmetov z očmi</li>
          <li>Čustveno zamegljenje ali zamegljenje vida</li>
          <li>Nepravilno usmerjenost oči (stranjski pogled)</li>
          <li>Težave s koncentriranjem pri branju ali risanju</li>
          <li>Čustveno zamegljenje ali zamegljenje vida</li>
          <li>Stalno zamašenje oči ali zamašenje</li>
        </ul>
        
        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Zakaj so letni pregledi pomembni?</h2>
        <p class="mb-4">Letni pregledi vida so pomembni zaradi več razlogov:</p>
        <ul class="list-disc pl-6 mb-4">
          <li>Zaznavanje ranljivih vidnih težav</li>
          <li>Preprečevanje šolske miopije (šolske miopije)</li>
          <li>Učinkovito zdravljenje, če je potrebno</li>
          <li>Podpora razvoju vidnih sposobnosti</li>
        </ul>
        
        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Kaj se dogaja na otrokovem pregledu vida?</h2>
        <p class="mb-4">Pregled vida za otroke vključuje:</p>
        <ul class="list-disc pl-6 mb-4">
          <li>Opazovanje očesne zdravstvene zgodovine</li>
          <li>Testiranje vidnega ostrosti</li>
          <li>Testiranje očesne koordinacije</li>
          <li>Preverjanje očesne zdravstvene stanja</li>
          <li>Preverjanje možnosti miopije</li>
        </ul>
        
        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Miopija in šolska miopija</h2>
        <p class="mb-4">Miopija je pogosta vidna težava, ki vodi do zamegljenega vida pri oddaljenih predmetih. Šolska miopija je pogosta pri otrocih, ki preživijo veliko časa pred zasloni. Pregledi vida so ključni za zaznavanje in nadzor šolske miopije.</p>
        
        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Zaščita otrokovega vida</h2>
        <p class="mb-4">Za zaščito otrokovega vida priporočamo:</p>
        <ul class="list-disc pl-6 mb-4">
          <li>Redne očesne preglede</li>
          <li>Pravilno osvetlitveno okolje</li>
          <li>Redne počitnice od zaslonov</li>
          <li>Uporabo sončnih očesnih stekel</li>
        </ul>
        
        <p class="mb-4">Če želite dodatno pomoč pri pregledu vida otroka, nas kontaktirajte v Studio Optika Si v Ljubljani ali Bežigradu. Naši specialisti vam bodo pomagali izbrati najbolj primerne rešitve za zaščito otrokovega vida.</p>
      </div>
      
      <div class="bg-primary-dark text-white p-6 rounded-lg mt-8">
        <h3 class="font-serif text-xl mb-4">Potrebujete dodatno pomoč?</h3>
        <p class="mb-4">Naši specialisti v Studio Optika Si v Ljubljani vam bodo pomagali izbrati najboljše rešitve za zaščito otrokovega vida.</p>
        <NuxtLink to="/kontakt" class="inline-block bg-accent text-primary-dark font-bold py-2 px-6 rounded hover:bg-opacity-90 transition duration-300">
          Kontaktirajte nas
        </NuxtLink>
      </div>
    </article>
  </div>
</template>

<script setup lang="ts">
import { useArticleSchema } from '~/composables/useArticleSchema'

useArticleSchema({
  title: 'Kdaj naj gre otrok prvič na pregled vida?',
  description: 'Spoznajte, kdaj naj otrok prvič obišče optikala in kakšne znake naj starši opazijo.',
  datePublished: '2023-06-20',
  dateModified: '2023-06-20',
  image: 'https://optikasi.si/images/hero_services.png',
  keywords: ['otrok', 'pregled vida', 'oči', 'miopija', 'starši'],
  slug: '/blog/otrokov-prvicni-pregled-vida'
})
</script>
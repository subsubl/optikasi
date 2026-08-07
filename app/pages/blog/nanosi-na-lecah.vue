<template>
  <div class="max-w-4xl mx-auto px-4 py-8">
    <NuxtLink to="/blog" class="text-primary-dark hover:text-accent transition-colors flex items-center mb-6">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l4.293 4.293a1 1 0 010 1.414z" clip-rule="evenodd" />
      </svg>
      Nazaj na blog
    </NuxtLink>

    <article>
      <h1 class="font-serif text-4xl md:text-5xl text-primary-dark mb-6">Nanosi na lečah: antirefleksni, oleo/hidrofobni, UV — kaj izbrati?</h1>

      <img :src="'/images/coatings/mirror-rose.jpg'" alt="Nanosi na lečah" class="w-full h-96 object-cover rounded-lg mb-8">

      <div class="prose prose-lg max-w-none">
        <p class="mb-4">Nanosi na lečah so pomembni za izboljšanje kakovosti vida in dolgotrajnosti leč. Različni nanosi omogočajo različne koristi, kot so zmanjšanje odbojev, lažje čiščenje in zaščita pred škodljivo UV svetlobo. V tem članku bomo razložili različne vrste nanosov in kako izbrati najboljše za vaše potrebe.</p>

        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Antirefleksni nanosi</h2>
        <p class="mb-4">Antirefleksni nanosi zmanjšujejo odboje na lečah, kar izboljša vidnost, zlasti v nočnih pogojih ali pri uporabi zaslonov. Koristi:</p>
        <ul class="list-disc pl-5 mb-4">
          <li>Zmanjšanje odbojev</li>
          <li>Izboljšana vidnost v nočnih pogojih</li>
          <li>Manjša motnja pri uporabi računalnikov in mobilnih naprav</li>
          <li>Manjša verjetnost zaslepljenja</li>
        </ul>

        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Oleo/hidrofobni in trdi/bruški nanosi</h2>
        <p class="mb-4">Oleo/hidrofobni nanosi omogočajo lažje čiščenje leč in boljšo odpornost na praske. Trdi/bruški nanosi zagotavljajo dodatno zaščito pred poštenjem:</p>
        <ul class="list-disc pl-5 mb-4">
          <li>Oleo/hidrofobni nanosi: lažje čiščenje, odpornost na praske</li>
          <li>Trdi/bruški nanosi: zaščita pred poštenjem in zlomljenjem</li>
        </ul>

        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">UV400 zaščita</h2>
        <p class="mb-4">UV400 zaščita preprečuje škodljivo UV svetlobo, ki lahko poškoduje oči. Ta zaščita je zelo pomembna za dolgotrajno zdravje očes.</p>

        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Filter za modro svetlobo</h2>
        <p class="mb-4">Filter za modro svetlobo zmanjšuje škodljivo modro svetlobo, ki jo oddajajo zaslonski zasloni. To zmanjšuje utrujenost očes in izboljša udobje pri uporabi elektronskih naprav.</p>

        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Blue-cut proti AR nanosu</h2>
        <p class="mb-4">Blue-cut nanosi so namenjeni zmanjšanju škodljive modre svetlobe, medtem ko AR nanosi zmanjšujejo odboje. Razlike:</p>
        <ul class="list-disc pl-5 mb-4">
          <li><strong>Blue-cut:</strong> Zmanjšuje škodljivo modro svetlobo</li>
          <li><strong>AR:</strong> Zmanjšuje odboje</li>
        </ul>

        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Praktični nasveti glede izbire nanosov</h2>
        <p class="mb-4">Izbira nanosa je odvisna od vaše vsakdanje rabe:</p>
        <ul class="list-disc pl-5 mb-4">
          <li><strong>Za vožnjo:</strong> Anti-reflection in UV400</li>
          <li><strong>Za delo na računalniku:</strong> Blue-cut in hidrofobni nanosi</li>
          <li><strong>Za šport:</strong> Trdi nanosi in UV400</li>
          <li><strong>Za splošno uporabo:</strong> Kombinacija AR, UV400 in hidrofobnih nanosov</li>
        </ul>

        <div class="bg-primary-dark text-white p-6 rounded-lg mt-8">
          <h3 class="text-xl font-bold mb-2">Potrebujete pomoč pri izbiri nanosov?</h3>
          <p class="mb-4">Pridite v Studio Optika Si v Ljubljani, kjer vam bodo pomagali izbrati najboljše nanose za vaše potrebe.</p>
          <NuxtLink to="/kontakt" class="inline-block bg-accent text-primary-dark py-2 px-6 rounded hover:bg-opacity-90 transition-colors">
            Kontaktirajte nas
          </NuxtLink>
        </div>
      </div>
    </article>
  </div>
</template>

<script setup>
import { useArticleSchema } from '~/composables/useArticleSchema'

useArticleSchema({
  title: 'Nanosi na lečah: antirefleksni, oleo/hidrofobni, UV — kaj izbrati?',
  description: 'Izvedite več o različnih nanosih na lečah in kako izbrati najboljše za vaše potrebe.',
  datePublished: '2026-08-17',
  dateModified: '2026-08-17',
  image: '/images/coatings/mirror-rose.jpg',
  keywords: ['nanosi na lečah', 'antirefleksni', 'UV400', 'studio optika si', 'ljubljana'],
  slug: '/blog/nanosi-na-lecah'
})
</script>
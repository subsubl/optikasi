<template>
  <div class="max-w-4xl mx-auto px-4 py-8">
    <NuxtLink to="/blog" class="text-primary-dark hover:text-accent transition-colors flex items-center mb-6">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l4.293 4.293a1 1 0 010 1.414z" clip-rule="evenodd" />
      </svg>
      Nazaj na blog
    </NuxtLink>

    <article>
      <h1 class="font-serif text-4xl md:text-5xl text-primary-dark mb-6">Kontaktne leče: vodič od izbire do nošenja</h1>

      <img :src="'/images/hero_services.png'" alt="Kontaktne leče" class="w-full h-96 object-cover rounded-lg mb-8">

      <div class="prose prose-lg max-w-none">
        <p class="mb-4">Kontaktne leče so zelo pogosta rešitev za popravljanje vida, ki omogočajo boljše vizualne izkušnje kot običajne okularje. Vendar je izbira pravih kontaktnih leč za vas pomembna, saj vpliva na udobje, varnost in učinkovitost. V tem vodiču bomo razložili različne vrste kontaktnih leč, kako se pravilno prilagajajo in kako izbrati najboljšo možnost za vaše potrebe.</p>

        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Vrste kontaktnih leč</h2>
        <ul class="list-disc pl-5 mb-4">
          <li><strong>Dnevne kontaktne leče:</strong> Primerne za dnevno uporabo, pogosto narejene iz hidrofilnih materialov. Pogosto se uporabljajo za dnevno uporabo in se morajo redno menjavati glede na priporočila proizvajalca.</li>
          <li><strong>Mesečne kontaktne leče:</strong> Zmerni rok uporabe, pogosto bolj ekonomične. Pravilno upravljanje s takšnimi lečami zahteva strogo sledenje higieni in pravilnemu čiščenju.</li>
          <li><strong>Toric kontaktne leče:</strong> Namenjene za osebe z astigmatizmom. Imajo poseben oblikovanje, ki omogoča ravnanje z nepravilnostmi ročice.</li>
          <li><strong>Multifokalne kontaktne leče:</strong> Prilagojene za presbiopijo, ki omogočajo dobro videno na različnih razdaljah. Lahko vključujejo tudi kombinacijo dvojnih ali več fokusnih točk.</li>
        </ul>

        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Kako deluje prilagoditev kontaktne leče?</h2>
        <p class="mb-4">Prilagoditev kontaktne leče je ključna za udobje in varnost. Pri nas v Studio Optika Si v Ljubljani imamo izkušene optike, ki vam pomagajo pri izbiri pravih leč ter pravilnem prilagajanju. Postopek vključuje:</p>
        <ul class="list-disc pl-5 mb-4">
          <li>Preverjanje vaše očesne zdravstvene stanja</li>
          <li>Meritve očesne lastnosti (keratometrija, pupila)</li>
          <li>Izbira primernih materialov in oblik</li>
          <li>Uvodna prilagoditev in nadzor</li>
        </ul>

        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Udobje in suhost</h2>
        <p class="mb-4">Za optimalno udobje pri uporabi kontaktnih leč je pomembno upoštevati:</p>
        <ul class="list-disc pl-5 mb-4">
          <li>Izbira pravih materialov za vaše oči (hidrofilni ali silikon-soft)</li>
          <li>Redna uporaba kapljic za oči za preprečevanje suhosti</li>
          <li>Redna menjava leč po priporočilih proizvajalca</li>
          <li>Pravilno čiščenje in hranjenje</li>
        </ul>

        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Higiena in varnost</h2>
        <p class="mb-4">Higiena je ključna za varno uporabo kontaktnih leč. Priporočamo:</p>
        <ul class="list-disc pl-5 mb-4">
          <li>Redno umivanje rok pred dotikanjem leč</li>
          <li>Uporabo ustreznih čistilnih sredstev</li>
          <li>Redno menjavo leč in nosilcev</li>
          <li>Neuporabo leč po pretečenem roku</li>
        </ul>

        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Cena v primerjavi z okularji</h2>
        <p class="mb-4">Kontaktne leče so pogosto dražje kot običajni okularji, vendar ponujajo več prednosti:</p>
        <ul class="list-disc pl-5 mb-4">
          <li>Boljše vizualne izkušnje brez omejitve vida</li>
          <li>Ni omejitve na gibanje ali aktivnosti</li>
          <li>Manjša verjetnost poštenja ali zlomljenja</li>
          <li>Večja estetska vrednost</li>
        </ul>

        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Zakaj kupiti pri optiku?</h2>
        <p class="mb-4">Kupovanje kontaktnih leč pri izkušenem optiku vključuje:</p>
        <ul class="list-disc pl-5 mb-4">
          <li>Precizne meritve za pravilno prilagoditev</li>
          <li>Profesionalno nasvetovanje glede materialov in tipov</li>
          <li>Garancijo za kakovost in varnost</li>
          <li>Nadzor in podpora po nakupu</li>
        </ul>

        <div class="bg-primary-dark text-white p-6 rounded-lg mt-8">
          <h3 class="text-xl font-bold mb-2">Potrebujete pomoč pri izbiri kontaktnih leč?</h3>
          <p class="mb-4">Pridite v Studio Optika Si v Ljubljani, kjer vam bodo pomagali izbrati najboljše kontaktne leče za vaše potrebe.</p>
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
  title: 'Kontaktne leče: vodič od izbire do nošenja',
  description: 'Izvedite več o različnih vrstah kontaktnih leč, njihovi izbiri, prilagajanju in varnosti.',
  datePublished: '2026-08-15',
  dateModified: '2026-08-15',
  image: '/images/hero_services.png',
  keywords: ['kontaktne leče', 'optika', 'studio optika si', 'ljubljana', 'vodič'],
  slug: '/blog/kontaktne-lece-vodic'
})
</script>
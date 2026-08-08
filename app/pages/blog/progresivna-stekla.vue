<template>
  <div class="max-w-4xl mx-auto px-4 py-8">
    <NuxtLink to="/blog" class="text-primary-dark hover:text-accent transition-colors flex items-center mb-6">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l4.293 4.293a1 1 0 010 1.414z" clip-rule="evenodd" />
      </svg>
      Nazaj na blog
    </NuxtLink>

    <article>
      <h1 class="font-serif text-4xl md:text-5xl text-primary-dark mb-6">Progresivna stekla: za koga so in kako se nanje navaditi</h1>

      <img src="/images/blog/progresivna-stekla.jpg" alt="Progresivna stekla" class="w-full h-96 object-cover rounded-lg mb-8" />

      <div class="prose prose-lg max-w-none">
        <p class="mb-4">Progresivna stekla so zelo pogosta rešitev za osebe, ki imajo presbiopijo – starostno slabovidnost. Te stekla omogočajo dobro videno na različnih razdaljah brez vidne linije, kar jih naredi zelo prijetne za uporabo. V tem članku bomo razložili, kaj je presbiopija, kako delujejo progresivna stekla in kako se nanje navaditi.</p>

        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Kaj je presbiopija?</h2>
        <p class="mb-4">Presbiopija je naraven proces, ki se dogaja s staranjem. Ko oči izgubijo sposobnost za prilagajanje (ako), postane težje videti blizu. Ta stanje se običajno začne po 40. letu življenja in se pogosto povezuje z potrebno za uporabo povečevalnih stekel.</p>

        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Kako delujejo progresivna stekla?</h2>
        <p class="mb-4">Progresivna stekla imajo gladko prehod med različnimi fokusnimi točkami – daleč, vmes in blizu – brez vidne linije. To omogoča:</p>
        <ul class="list-disc pl-5 mb-4">
          <li>Udobje pri gledanju na različnih razdaljah</li>
          <li>Estetsko izgledanje brez vidne linije</li>
          <li>Manjšo omejitev gibanja</li>
          <li>Večjo funkcionalnost v vsakdanjem življenju</li>
        </ul>

        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Progresivna stekla proti bifokalnim steklom</h2>
        <p class="mb-4">Bifokalna stekla imajo vidno linijo, ki loči daleč in blizu. Progresivna stekla pa omogočajo gladko prehod med različnimi vidnimi območji. Razlike:</p>
        <ul class="list-disc pl-5 mb-4">
          <li><strong>Bifokal:</strong> Vidna linija, ki loči daleč in blizu</li>
          <li><strong>Progressivna:</strong> Brez linije, gladko prehajanje med različnimi vidnimi območji</li>
        </ul>

        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Za koga so progresivna stekla?</h2>
        <p class="mb-4">Progresivna stekla so najbolj primerna za osebe, ki:</p>
        <ul class="list-disc pl-5 mb-4">
          <li>Imajo presbiopijo po 40. letu življenja</li>
          <li>Uporabljajo okularje za dnevno uporabo</li>
          <li>Iskajo estetsko rešitev brez vidne linije</li>
          <li>Imajo aktivno življenje in potrebujejo funkcionalnost</li>
        </ul>

        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Kako se navaditi na progresivna stekla?</h2>
        <p class="mb-4">Prilagoditev progresivnim steklam lahko traja nekaj tednov. Priporočamo:</p>
        <ul class="list-disc pl-5 mb-4">
          <li>Redno uporabo vseh dnevih</li>
          <li>Postopno prilagajanje gibanju glave</li>
          <li>Uporabo v različnih situacijah</li>
          <li>Čakanje na prilagoditev (do 2 tednov)</li>
        </ul>

        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Pomembnost natančne prilagoditve</h2>
        <p class="mb-4">Natančna prilagoditev je ključna za uspešno uporabo progresivnih stekel. Pravilna meritev vključuje:</p>
        <ul class="list-disc pl-5 mb-4">
          <li>Pravilno položaj očes</li>
          <li>Pravilno razdaljo med očesom in steklom</li>
          <li>Prilagoditev glede na vaše potrebe</li>
          <li>Ustrezno izbiro velikosti okvirja</li>
        </ul>

        <div class="bg-primary-dark text-white p-6 rounded-lg mt-8">
          <h3 class="text-xl font-bold mb-2">Potrebujete pomoč pri izbiri progresivnih stekel?</h3>
          <p class="mb-4">Pridite v Studio Optika Si v Ljubljani, kjer vam bodo pomagali izbrati najboljše progresivne stekla za vaše potrebe.</p>
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
  title: 'Progresivna stekla: za koga so in kako se nanje navaditi',
  description: 'Izvedite več o progresivnih steklah, njihovi uporabi in prilagoditvi za presbiopijo.',
  datePublished: '2026-08-16',
  dateModified: '2026-08-16',
  image: 'https://optikasi.si/images/blog/progresivna-stekla.jpg',
  keywords: ['progresivna stekla', 'presbiopija', 'optika', 'studio optika si', 'ljubljana'],
  slug: '/blog/progresivna-stekla'
})
</script>
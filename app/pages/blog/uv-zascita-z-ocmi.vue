<template>
  <div class="max-w-4xl mx-auto px-4 py-8">
    <NuxtLink to="/blog" class="text-primary-dark hover:text-accent flex items-center mb-6">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l4.293 4.293a1 1 0 010 1.414z" clip-rule="evenodd" />
      </svg>
      Nazaj na blog
    </NuxtLink>
    
    <article>
      <h1 class="font-serif text-4xl md:text-5xl text-primary-dark mb-6">UV zaščita za oči skozi vse leto</h1>
      
      <img src="/images/blog/uv-zascita-z-ocmi.jpg" alt="UV zaščita za oči" class="w-full h-96 object-cover rounded-lg mb-8" />
      
      <div class="prose prose-lg max-w-none">
        <p class="mb-4">UV (ultravioletna) svetloba je del sončne svetlobe, ki lahko povzroči škodo očem. Kljub temu, da je UV najmočnejši v poletju, je zaščita za oči pomembna tudi v drugih letnih časih. V tej objavi bomo razložili, zakaj je UV zaščita pomembna za oči skozi vse leto.</p>
        
        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Kaj so UVA in UVB?</h2>
        <p class="mb-4">UVA in UVB so dve vrsti ultravioletne svetlobe:</p>
        <ul class="list-disc pl-6 mb-4">
          <li><strong>UVA:</strong> Dljevalne ultravioletne valovne dolžine, ki penetrirajo globlje v kožo in oči. Povzročajo starenje in škodo DNA.</li>
          <li><strong>UVB:</strong> Krajševalne ultravioletne valovne dolžine, ki povzročajo direktno škodo koži in očim. Povzročajo sunčične pšenice in očesne bolezni.</li>
        </ul>
        
        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Zakaj je UV zaščita pomembna v zimi?</h2>
        <p class="mb-4">UV zaščita je pomembna tudi v zimi zaradi:</p>
        <ul class="list-disc pl-6 mb-4">
          <li>Odboja svetlobe na snegu, ki lahko poveča UV izpust do 80%</li>
          <li>Višje položaje sonca, ki lahko povzročijo več UV izpusta</li>
          <li>Večje izpostavljenost soncu pri aktivnostih na zimi</li>
        </ul>
        
        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Kakšne so zaščitne lastnosti sončnih očesnih stekel?</h2>
        <p class="mb-4">Sončna očesna stekla imajo različne zaščitne lastnosti:</p>
        <ul class="list-disc pl-6 mb-4">
          <li><strong>Samoobarvna (photochromic) stekla:</strong> Prilagajajo se svetlobi in se temnejša v sončnem svetlu.</li>
          <li><strong>Polarizirana stekla:</strong> Zmanjšajo odboj svetlobe in izboljšajo vidnost.</li>
          <li><strong>CE/UV400 standard:</strong> Garantira zaščito pred 100% UVA in UVB.</li>
        </ul>
        
        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Zaščita otrokovega vida</h2>
        <p class="mb-4">Otroci so bolj ranjivi za UV škodo zaradi:</p>
        <ul class="list-disc pl-6 mb-4">
          <li>Manjše zaščite kože in oči</li>
          <li>Večje izpostavljenosti soncu</li>
          <li>Večje časa v zunanji prostoru</li>
        </ul>
        
        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Kako izbrati pravilne sončne očesne stekle?</h2>
        <p class="mb-4">Pri izbiri sončnih očesnih stekel priporočamo:</p>
        <ul class="list-disc pl-6 mb-4">
          <li>Uporabo stekel z CE/UV400 zaščito</li>
          <li>Polarizirane ali samoobarvne stekle</li>
          <li>Pravilno prilagojeni modeli</li>
          <li>Ustrezen oblikovani model za otroka</li>
        </ul>
        
        <p class="mb-4">Če želite dodatno pomoč pri izbiri zaščitnih očesnih stekel, nas kontaktirajte v Studio Optika Si v Ljubljani ali Bežigradu. Naši specialisti vam bodo pomagali izbrati najbolj primerne rešitve za zaščito oči pred UV.</p>
      </div>
      
      <div class="bg-primary-dark text-white p-6 rounded-lg mt-8">
        <h3 class="font-serif text-xl mb-4">Potrebujete dodatno pomoč?</h3>
        <p class="mb-4">Naši specialisti v Studio Optika Si v Ljubljani vam bodo pomagali izbrati najboljše sončne očesne stekle za zaščito oči pred UV.</p>
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
  title: 'UV zaščita za oči skozi vse leto',
  description: 'Spoznajte, zakaj je UV zaščita pomembna za oči skozi vse leto in kakšne so zaščitne lastnosti sončnih očesnih stekel.',
  datePublished: '2026-07-15',
  dateModified: '2026-07-15',
  image: 'https://optikasi.si/images/blog/uv-zascita-z-ocmi.jpg',
  keywords: ['UV', 'oči', 'sončna zaščita', 'zaščita', 'sonce'],
  slug: '/blog/uv-zascita-z-ocmi'
})
</script>
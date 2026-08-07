<template>
  <div class="max-w-4xl mx-auto px-4 py-8">
    <NuxtLink to="/blog" class="text-primary-dark hover:text-accent flex items-center mb-6">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l4.293 4.293a1 1 0 010 1.414z" clip-rule="evenodd" />
      </svg>
      Nazaj na blog
    </NuxtLink>
    
    <article>
      <h1 class="font-serif text-4xl md:text-5xl text-primary-dark mb-6">Modra svetloba in oči: kaj res deluje za zaslone</h1>
      
      <img :src="'/images/coatings/opal-ultra-uv.jpg'" alt="Modra svetloba in oči" class="w-full h-96 object-cover rounded-lg mb-8" />
      
      <div class="prose prose-lg max-w-none">
        <p class="mb-4">V današnjem svetu, kjer preživimo večino časa pred zasloni računalnikov, tablic in pametnih telefonov, se postavlja vprašanje, kako modra svetloba vpliva na naše oči. Modra svetloba je del spektra vidne svetlobe, ki jo izseva zaslon, in njena vloga pri zdravju oči je pomembna.</p>
        
        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Kaj je modra svetloba?</h2>
        <p class="mb-4">Modra svetloba je elektromagnetna valna dolžina med 400 in 500 nanometri. Zasloni računalnikov, tablic in mobilnih naprav emitirajo veliko modre svetlobe, kar lahko vpliva na naše oči in spanec.</p>
        
        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Začasnost in digitalna utrujenost oči</h2>
        <p class="mb-4">Dolgotrajna uporaba digitalnih naprav lahko povzroči digitalno utrujenost oči (Digital Eye Strain), ki vključuje simptome kot so:</p>
        <ul class="list-disc pl-6 mb-4">
          <li>Utrujenost oči</li>
          <li>Zamegljenje vida</li>
          <li>Bol v vratu in ramenih</li>
          <li>Težave s koncentracijo</li>
        </ul>
        
        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Filter za modro svetlobo</h2>
        <p class="mb-4">Filterji za modro svetlobo so različni načini za zmanjšanje izpusta modre svetlobe. Obstajajo dve glavni vrsti:</p>
        <ul class="list-disc pl-6 mb-4">
          <li><strong>Fizični filtri:</strong> Uporabljajo se na očesnih steklilih ali zaslonih za zmanjšanje izpusta modre svetlobe.</li>
          <li><strong>Programski filtri:</strong> Programi kot so f.lux ali Night Shift na iOS napravah, ki prilagajajo barvo zaslona glede na čas dneva.</li>
        </ul>
        
        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Znanstveni dokazi</h2>
        <p class="mb-4">Znanstveni dokazi kažejo, da modra svetloba vpliva na naš biološki ura, posebej na izločanje melatonina, hormona, ki regulira spanec. Čeprav obstaja nekaj študij, ki kažejo koristi pri uporabi filtrov za modro svetlobo, še vedno ni jasno, ali imajo dolgoročne učinke na zdravje oči.</p>
        
        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Kdaj je uporaba filtrov primerna?</h2>
        <p class="mb-4">Uporaba filtrov za modro svetlobo je najbolj koristna za:</p>
        <ul class="list-disc pl-6 mb-4">
          <li>Osebe, ki imajo težave s spanjem</li>
          <li>Pri uporabi naprav v nočnem času</li>
          <li>Osebe z občutljivimi očmi</li>
        </ul>
        
        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Anti-reflective coating</h2>
        <p class="mb-4">Anti-reflective (AR) coating je tlačna plast na očesnih steklilih, ki zmanjša odboj svetlobe. To zmanjša zamegljenje in izboljša vidnost, kar je koristno za uporabo digitalnih naprav. AR coating je zelo učinkovit pri zmanjšanju odboja svetlobe, kar zmanjša utrujenost oči.</p>
        
        <h2 class="font-serif text-2xl text-primary-dark mt-8 mb-4">Priporočila za zaščito oči</h2>
        <p class="mb-4">Za zaščito oči pred škodo, povzročeno z modro svetlobo, priporočamo:</p>
        <ul class="list-disc pl-6 mb-4">
          <li>Redno počitnice od zaslonov (pravilo 20-20-20)</li>
          <li>Pravilno osvetlitveno okolje</li>
          <li>Uporabo AR coating na očesnih steklilih</li>
          <li>Uporabo filtrov za modro svetlobo v nočnem času</li>
        </ul>
        
        <p class="mb-4">Če želite dodatno zaščito svojih oči, nas kontaktirajte v Studio Optika Si v Ljubljani ali Bežigradu. Naši specialisti vam bodo pomagali izbrati najbolj primerne očesne steklene za vaše potrebe.</p>
      </div>
      
      <div class="bg-primary-dark text-white p-6 rounded-lg mt-8">
        <h3 class="font-serif text-xl mb-4">Potrebujete dodatno pomoč?</h3>
        <p class="mb-4">Naši specialisti v Studio Optika Si v Ljubljani vam bodo pomagali izbrati najboljše očesne steklene za zaščito oči pred modro svetlobo.</p>
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
  title: 'Modra svetloba in oči: kaj res deluje za zaslone',
  description: 'Spoznajte, kako modra svetloba vpliva na naše oči in kakšne mere za zaščito pred njo obstajajo.',
  datePublished: '2023-05-15',
  dateModified: '2023-05-15',
  image: 'https://optikasi.si/images/coatings/opal-ultra-uv.jpg',
  keywords: ['modra svetloba', 'digitalna utrujenost', 'oči', 'zasloni', 'zaščita'],
  slug: '/blog/modra-svetloba-in-oci'
})
</script>
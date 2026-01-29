<template>
  <div class="min-h-screen pt-20">
    <!-- Hero Section -->
    <section class="relative h-[50vh] min-h-[400px] flex items-center justify-center bg-gray-900 text-white overflow-hidden">
      <div class="absolute inset-0 z-0">
        <img :src="'/optikasi/images/safety/industrija-in-rudarstvo_header_varilec-header-1.jpg'" alt="Varnostna Očala" class="w-full h-full object-cover opacity-50" />
      </div>
      <div class="relative z-10 text-center px-4 max-w-4xl mx-auto">
        <h1 class="text-5xl md:text-7xl font-serif mb-6">Varnostna Očala</h1>
        <p class="text-xl md:text-2xl font-light tracking-wide">
          Vrhunska zaščita za vaš vid v vsakem delovnem okolju.
        </p>
      </div>
    </section>

    <!-- Investment Section -->
    <section class="py-24 bg-gray-50">
      <div class="container mx-auto px-4 max-w-6xl">
        <div class="text-center mb-16">
          <span class="text-accent uppercase tracking-widest text-sm font-bold mb-4 block">Varnost kot Naložba</span>
          <h2 class="text-4xl font-serif text-primary-dark mb-6">Zakaj so Varnostna Očala Pametna Odločitev?</h2>
          <p class="text-gray-600 max-w-2xl mx-auto leading-relaxed text-lg">
            Poleg preprečevanja poškodb, kakovostna zaščitna oprema dokazano povečuje produktivnost in dolgoročno znižuje stroške.
          </p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-12">
          <!-- Produktivnost -->
          <div class="text-center group">
            <div class="w-16 h-16 mx-auto bg-white rounded-full shadow-md flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
               <span class="text-3xl">📈</span>
            </div>
            <h3 class="text-xl font-serif text-primary-dark mb-4">Višja Produktivnost</h3>
            <p class="text-gray-600 text-sm leading-relaxed">
              Študije kažejo, da se učinkovitost zaposlenih z ustreznimi korekcijskimi očali poveča za <strong class="text-primary-dark">20% do 34%</strong>. Dober vid pomeni manj napak in hitrejše delo.
            </p>
          </div>

          <!-- ROI -->
          <div class="text-center group">
             <div class="w-16 h-16 mx-auto bg-white rounded-full shadow-md flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
               <span class="text-3xl">💰</span>
            </div>
            <h3 class="text-xl font-serif text-primary-dark mb-4">Visok Donos (ROI)</h3>
            <p class="text-gray-600 text-sm leading-relaxed">
              Vsak evro, vložen v varnost in zdravje pri delu, se povrne z <strong class="text-primary-dark">2,5 do 4,8 EUR</strong>. Manj bolniških odsotnosti in odškodnin pomeni prihranek.
            </p>
          </div>

          <!-- Optika -->
          <div class="text-center group">
             <div class="w-16 h-16 mx-auto bg-white rounded-full shadow-md flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
               <span class="text-3xl">👁️</span>
            </div>
            <h3 class="text-xl font-serif text-primary-dark mb-4">Vrhunska Optika</h3>
            <p class="text-gray-600 text-sm leading-relaxed">
              Korekcijska zaščitna očala nudijo <strong class="text-primary-dark">98% prepustnost svetlobe</strong> in 9x manj odsevov v primerjavi z nošenjem zaščitnih očal čez navadna očala (OTG).
            </p>
          </div>

          <!-- Zdravje -->
          <div class="text-center group">
             <div class="w-16 h-16 mx-auto bg-white rounded-full shadow-md flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
               <span class="text-3xl">🛡️</span>
            </div>
            <h3 class="text-xl font-serif text-primary-dark mb-4">Dolgoročno Zdravje</h3>
            <p class="text-gray-600 text-sm leading-relaxed">
              Preprečite trajne poškodbe vida. 33% delovne populacije ima težave z nekorigiranim vidom, kar vodi v dolgoročne zdravstvene težave in nesreče.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Categories Grid -->
    <section class="py-20 px-4 bg-white">
      <div class="container mx-auto">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <NuxtLink v-for="(data, slug) in safetyData" :key="slug" :to="`/varnostna-ocala/${slug}`" class="group block bg-gray-50 hover:shadow-xl transition-shadow duration-300">
            <div class="aspect-video overflow-hidden">
              <img :src="data.header_image" :alt="data.title" class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" />
            </div>
            <div class="p-8">
              <h3 class="text-2xl font-serif mb-4 group-hover:text-primary transition-colors text-gray-900">{{ data.title }}</h3>
              <p class="text-gray-600 line-clamp-3 mb-6">{{ getIntroText(data.intro) }}</p>
              <span class="inline-block border-b border-primary text-primary uppercase tracking-widest text-sm pb-1">Preberi več</span>
            </div>
          </NuxtLink>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import safetyDataRaw from '@/assets/data/safety_data.json'

const safetyData = safetyDataRaw

const getIntroText = (introArray) => {
  if (!introArray || introArray.length === 0) return ''
  // Return the first paragraph that isn't a header (heuristic) or just the first one
  // In our JSON, intro items are just strings.
  return introArray.find(p => p.length > 50) || introArray[0]
}

useHead({
  title: 'Varnostna Očala | Optika',
  meta: [
    { name: 'description', content: 'Vrhunska zaščitna očala z dioptrijo za vsa delovna okolja.' }
  ]
})
</script>


<template>
  <div>
    <!-- Hero Section -->
    <section class="relative h-[60vh] min-h-[500px] flex items-center justify-center overflow-hidden">
      <div class="absolute inset-0 z-0">
        <!-- Using one of the ingested images as hero foundation, with overlay -->
        <img :src="'/optikasi/images/driving/drive_car.png'" alt="Očala za vožnjo" class="w-full h-full object-cover blur-[2px]" />
        <div class="absolute inset-0 bg-black/60"></div>
      </div>
      <div class="relative z-10 text-center px-6 max-w-4xl mx-auto text-white">
        <span class="text-accent uppercase tracking-widest text-sm font-bold mb-4 block">Varnost na Cesti</span>
        <h1 class="text-5xl md:text-7xl font-serif mb-6">Očala za Vožnjo</h1>
        <p class="text-xl md:text-2xl font-light opacity-90 max-w-2xl mx-auto">
          Drivewear: Ena stekla za vse svetlobne pogoje. Popoln vid v vsakem trenutku.
        </p>
      </div>
    </section>

    <!-- Intro -->
    <section class="py-24 bg-cream">
      <div class="container mx-auto px-6 max-w-4xl text-center">
        <h2 class="text-3xl font-serif text-primary-dark mb-8">STEKLA DRIVEWEARZA VARNEJŠO VOŽNJO</h2>
        <p class="text-gray-600 leading-relaxed text-lg mb-8">
          Med vožnjo imamo vozniki različne zahteve. Potrebujemo širok, nemoten vid na daljavo ter dober vid na bližino. 
          Prav tako želimo odličen vid v različnih svetlobnih pogojih, kot so sonce, megla, dež. 
          Vse to vam omogočimo z izborom polariziranih stekel Drivewear.
        </p>
      </div>
    </section>

    <!-- 3 States Grid -->
    <section class="py-24">
      <div class="container mx-auto px-6 max-w-6xl">
        <h2 class="text-3xl font-serif text-primary-dark mb-16 text-center">3 Pogoji - 1 Rešitev</h2>
        
        <div class="grid md:grid-cols-3 gap-8">
          <!-- Oblačno -->
          <div class="group bg-white p-4 border border-gray-100 rounded-lg shadow-sm hover:shadow-md transition-all">
            <div class="relative h-64 overflow-hidden mb-6 rounded-lg">
              <img :src="'/optikasi/images/driving/drive_cloudy.png'" alt="Oblačno vreme"
                   class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/50 to-transparent flex items-end p-6">
                <h3 class="text-xl font-serif text-white">Oblačno Vreme</h3>
              </div>
            </div>
            <p class="text-gray-600 leading-relaxed text-sm">
              Visokokontrastna zeleno rumena barva, ki omogoča, da kar največ svetlobe doseže oko. 
              Polarizacija odpravi bleščanje, ki bi drugače motilo vid v razmerah z malo svetlobe.
            </p>
          </div>

          <!-- Avto -->
          <div class="group bg-white p-4 border border-gray-100 rounded-lg shadow-sm hover:shadow-md transition-all">
            <div class="relative h-64 overflow-hidden mb-6 rounded-lg">
              <img :src="'/optikasi/images/driving/drive_car.png'" alt="Svetloba v avtu"
                   class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/50 to-transparent flex items-end p-6">
                <h3 class="text-xl font-serif text-white">Svetloba v Avtu</h3>
              </div>
            </div>
            <p class="text-gray-600 leading-relaxed text-sm">
              Bakrena barva blokira odvečno svetlobo. Poudari rdečo in zeleno svetlobo (signalizacija). 
              Polarizacija odpravi bleščanje in zagotavlja varno vožnjo.
            </p>
          </div>

          <!-- Prostem -->
          <div class="group bg-white p-4 border border-gray-100 rounded-lg shadow-sm hover:shadow-md transition-all">
            <div class="relative h-64 overflow-hidden mb-6 rounded-lg">
              <img :src="'/optikasi/images/driving/drive_outdoor.png'" alt="Močna svetloba"
                   class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/50 to-transparent flex items-end p-6">
                <h3 class="text-xl font-serif text-white">Na Prostem</h3>
              </div>
            </div>
            <p class="text-gray-600 leading-relaxed text-sm">
              Temna rdeče-rjava barva maksimalno blokira odvečno svetlobo in prepreči zasičenje očesa. 
              Polarizacija zagotavlja največje ugodje v razmerah z močno svetlobo.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Video Section -->
    <section class="py-24 bg-primary-dark text-white">
      <div class="container mx-auto px-6 max-w-4xl text-center">
        <h2 class="text-3xl font-serif mb-8">Nova Dimenzija Vožnje</h2>
        <p class="text-gray-300 mb-12">
            Drivewear stekla temnijo v različnih svetlobnih pogojih, zunaj in za vetrobranskim steklom avtomobila.
        </p>
        <div class="relative aspect-video rounded-xl overflow-hidden shadow-2xl border border-white/20">
             <video class="w-full h-full object-cover" controls poster="/images/driving/drive_outdoor.png">
                <source src="https://www.alcom.si/wp-content/uploads/2020/05/Transitions-Drivewearkompresirano.mp4" type="video/mp4">
                Vaš brskalnik ne podpira videa.
             </video>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="py-20 text-center">
      <div class="container mx-auto px-6 max-w-3xl">
        <h2 class="text-3xl font-serif text-primary-dark mb-6">Želite Varno Vožnjo?</h2>
        <p class="text-gray-600 mb-8 leading-relaxed">
          Naročite se na pregled ali obiščite našo optiko, da preizkusite Drivewear tehnologijo v živo.
        </p>
        <NuxtLink 
          to="/kontakt" 
          class="inline-block bg-primary text-white px-10 py-4 uppercase tracking-widest hover:bg-primary-light transition-colors"
        >
          Kontaktirajte Nas
        </NuxtLink>
      </div>
    </section>
  </div>
</template>

<script setup>
useHead({
  title: 'Očala za Vožnjo - Drivewear',
  meta: [
    { name: 'description', content: 'Drivewear očala za varno vožnjo v vseh pogojih. Polarizirana stekla, ki se prilagajajo svetlobi v avtu in na prostem.' }
  ]
})
</script>

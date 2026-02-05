<template>
  <div class="py-24 container mx-auto px-6 max-w-3xl">
    <div class="text-center mb-12">
      <h1 class="text-4xl font-serif text-primary-dark mb-4">Kontaktne Leče - Naročilo</h1>
      <p class="text-gray-600">Hitro in enostavno naročite nove zaloge vaših leč v <strong>Optiki Ljubljana</strong>.</p>
    </div>

    <form @submit.prevent="submitOrder" class="bg-white p-8 md:p-12 shadow-sm border border-gray-100 space-y-8">

      <!-- Personal Details -->
      <div>
        <h3 class="text-lg font-serif text-primary-dark border-b border-gray-100 pb-2 mb-6">Osebni Podatki</h3>
        <div class="grid md:grid-cols-2 gap-6">
          <div class="flex flex-col">
            <label for="name" class="text-xs uppercase tracking-widest text-gray-500 mb-2">Ime in Priimek</label>
            <input id="name" v-model="form.name" type="text" required class="bg-cream border-none p-4 focus:ring-1 focus:ring-accent outline-none">
          </div>
          <div class="flex flex-col">
            <label for="email" class="text-xs uppercase tracking-widest text-gray-500 mb-2">E-naslov</label>
            <input id="email" v-model="form.email" type="email" required class="bg-cream border-none p-4 focus:ring-1 focus:ring-accent outline-none">
          </div>
        </div>
      </div>

      <!-- Lens Details -->
      <div>
        <h3 class="text-lg font-serif text-primary-dark border-b border-gray-100 pb-2 mb-6">Podatki o Lečah</h3>
        <div class="space-y-6">
          <div class="flex flex-col">
            <label for="brand" class="text-xs uppercase tracking-widest text-gray-500 mb-2">Znamka Kontaktnih Leč (npr. Acuvue, Air Optix, Biofinity)</label>
            <input id="brand" v-model="form.brand" type="text" required class="bg-cream border-none p-4 focus:ring-1 focus:ring-accent outline-none">
          </div>

          <div class="grid md:grid-cols-2 gap-6">
            <!-- Left Eye -->
            <div class="bg-gray-50 p-4 rounded-sm">
              <span class="block text-center font-bold text-primary-dark mb-4">Levo Oko (OS)</span>
              <div class="space-y-3">
                <input v-model="form.os.power" placeholder="Dioptrija (SPH)" aria-label="Levo oko: Dioptrija (SPH)" class="w-full bg-white border border-gray-200 p-2 text-sm focus:ring-1 focus:ring-accent focus:outline-none">
                <input v-model="form.os.cyl" placeholder="Cilinder (CYL)" aria-label="Levo oko: Cilinder (CYL)" class="w-full bg-white border border-gray-200 p-2 text-sm focus:ring-1 focus:ring-accent focus:outline-none">
                <input v-model="form.os.axis" placeholder="Os (AX)" aria-label="Levo oko: Os (AX)" class="w-full bg-white border border-gray-200 p-2 text-sm focus:ring-1 focus:ring-accent focus:outline-none">
              </div>
            </div>

            <!-- Right Eye -->
            <div class="bg-gray-50 p-4 rounded-sm">
              <span class="block text-center font-bold text-primary-dark mb-4">Desno Oko (OD)</span>
              <div class="space-y-3">
                <input v-model="form.od.power" placeholder="Dioptrija (SPH)" aria-label="Desno oko: Dioptrija (SPH)" class="w-full bg-white border border-gray-200 p-2 text-sm focus:ring-1 focus:ring-accent focus:outline-none">
                <input v-model="form.od.cyl" placeholder="Cilinder (CYL)" aria-label="Desno oko: Cilinder (CYL)" class="w-full bg-white border border-gray-200 p-2 text-sm focus:ring-1 focus:ring-accent focus:outline-none">
                <input v-model="form.od.axis" placeholder="Os (AX)" aria-label="Desno oko: Os (AX)" class="w-full bg-white border border-gray-200 p-2 text-sm focus:ring-1 focus:ring-accent focus:outline-none">
              </div>
            </div>
          </div>

           <div class="flex flex-col">
            <label for="quantity" class="text-xs uppercase tracking-widest text-gray-500 mb-2">Količina (škatlice)</label>
            <select id="quantity" v-model="form.quantity" class="bg-cream border-none p-4 focus:ring-1 focus:ring-accent outline-none">
              <option>1 par / škatlica</option>
              <option>2 para / škatlici</option>
              <option>3 pari / škatlice (Zaloga za 3 mesece)</option>
              <option>6 parov / škatlic (Zaloga za 6 mesecev)</option>
            </select>
          </div>
        </div>
      </div>

      <button
        type="submit"
        :disabled="isSubmitting"
        class="w-full bg-primary-dark text-white py-4 uppercase tracking-[0.2em] hover:bg-accent transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
      >
        <span v-if="isSubmitting">Oddajam...</span>
        <span v-else>Oddaj Naročilo</span>
      </button>

      <p v-if="success" role="alert" aria-live="polite" class="text-center text-green-600 mt-4 transition-all duration-300 ease-in-out">
        Naročilo uspešno oddano! Poslali vam bomo predračun.
      </p>

    </form>

    <div class="mt-16 text-center text-gray-500 text-sm">
      <p>Še niste preizkusili kontaktnih leč? <NuxtLink to="/storitve" class="text-accent hover:underline">Rezervirajte termin</NuxtLink> za uvajanje in strokovni pregled.</p>
    </div>
  </div>
</template>

<script setup>
useHead({
  title: 'Naročilo Kontaktnih Leč | Kontaktne Leče Ljubljana | Optika Si',
  meta: [
    { name: 'description', content: 'Hitro naročanje kontaktnih leč preko spleta. Široka izbira znamk (Acuvue, Biofinity, Air Optix). Možnost osebnega prevzema v Ljubljani ali dostave.' },
    { name: 'keywords', content: 'kontaktne leče, naročilo kontaktnih leč, kontaktne leče ljubljana, tekočina za leče, optika ljubljana' }
  ]
})

const form = reactive({
  name: '',
  email: '',
  brand: '',
  quantity: '3 pari / škatlice (Zaloga za 3 mesece)',
  os: { power: '', cyl: '', axis: '' },
  od: { power: '', cyl: '', axis: '' }
})

const success = ref(false)
const isSubmitting = ref(false)

const submitOrder = () => {
  if (isSubmitting.value) return

  isSubmitting.value = true
  success.value = false

  // Simulate API call
  setTimeout(() => {
    console.log('Order:', form)
    success.value = true
    isSubmitting.value = false
  }, 1000)
}
</script>

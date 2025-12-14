<template>
  <form @submit.prevent="submitForm" class="space-y-6 bg-white p-8 border border-gray-100 shadow-sm">
    <div class="grid md:grid-cols-2 gap-6">
      <div class="space-y-2">
        <label class="text-xs uppercase tracking-widest text-gray-500 font-bold">Ime in Priimek</label>
        <input v-model="form.name" type="text" required class="w-full border-b border-gray-300 focus:border-accent outline-none py-2 transition-colors" placeholder="Janez Novak" />
      </div>
      <div class="space-y-2">
        <label class="text-xs uppercase tracking-widest text-gray-500 font-bold">Email Naslov</label>
        <input v-model="form.email" type="email" required class="w-full border-b border-gray-300 focus:border-accent outline-none py-2 transition-colors" placeholder="janez@example.com" />
      </div>
    </div>

    <div class="space-y-2">
      <label class="text-xs uppercase tracking-widest text-gray-500 font-bold">Telefonska Številka</label>
      <input v-model="form.phone" type="tel" class="w-full border-b border-gray-300 focus:border-accent outline-none py-2 transition-colors" placeholder="041 123 456" />
    </div>

    <div class="space-y-4 pt-4">
      <label class="text-xs uppercase tracking-widest text-gray-500 font-bold block">Želeni Termini (Izberite več možnosti)</label>
      
      <!-- Weekdays -->
      <div class="flex flex-wrap gap-3 mb-4">
        <label v-for="day in days" :key="day" class="cursor-pointer">
          <input type="checkbox" :value="day" v-model="form.preferredDays" class="hidden peer" />
          <span class="px-3 py-1 border border-gray-200 text-sm text-gray-600 peer-checked:bg-primary-light peer-checked:text-white peer-checked:border-primary-light transition-all select-none">
            {{ day }}
          </span>
        </label>
      </div>

      <!-- Time Slots -->
      <div class="flex flex-wrap gap-3">
        <label v-for="slot in slots" :key="slot" class="cursor-pointer">
          <input type="checkbox" :value="slot" v-model="form.preferredSlots" class="hidden peer" />
          <span class="px-3 py-1 border border-gray-200 text-sm text-gray-600 peer-checked:bg-accent peer-checked:text-white peer-checked:border-accent transition-all select-none">
            {{ slot }}
          </span>
        </label>
      </div>
    </div>

    <div class="space-y-2">
      <label class="text-xs uppercase tracking-widest text-gray-500 font-bold">Sporočilo (Opcijsko)</label>
      <textarea v-model="form.message" rows="4" class="w-full border bg-gray-50 border-gray-200 focus:border-accent outline-none p-3 transition-colors text-sm"></textarea>
    </div>

    <button type="submit" class="w-full bg-primary text-white py-4 uppercase tracking-[0.15em] hover:bg-primary-dark transition-colors font-bold text-sm">
      Pošlji Povpraševanje
    </button>
  </form>
</template>

<script setup>
const days = ['Ponedeljek', 'Torek', 'Sreda', 'Četrtek', 'Petek']
const slots = ['Dopoldan (8:00 - 12:00)', 'Popoldan (12:00 - 16:00)', 'Po 16:00']

const form = reactive({
  name: '',
  email: '',
  phone: '',
  preferredDays: [],
  preferredSlots: [],
  message: ''
})

const submitForm = () => {
  // Simulate submission
  console.log('Form Submitted:', form)
  alert('Hvala za vaše povpraševanje! Kontaktirali vas bomo v najkrajšem možnem času.')
  // Reset form functionality would happen here
}
</script>

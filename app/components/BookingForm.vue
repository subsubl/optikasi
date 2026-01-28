<template>
  <form @submit.prevent="submitForm" class="space-y-6 bg-white p-8 border border-gray-100 shadow-sm">
    <div class="grid md:grid-cols-2 gap-6">
      <div class="space-y-2">
        <label for="booking-name" class="text-xs uppercase tracking-widest text-gray-500 font-bold">Ime in Priimek</label>
        <input id="booking-name" v-model="form.name" type="text" required class="w-full border-b border-gray-300 focus:border-accent outline-none py-2 transition-colors" placeholder="Janez Novak" />
      </div>
      <div class="space-y-2">
        <label for="booking-email" class="text-xs uppercase tracking-widest text-gray-500 font-bold">Email Naslov</label>
        <input id="booking-email" v-model="form.email" type="email" required class="w-full border-b border-gray-300 focus:border-accent outline-none py-2 transition-colors" placeholder="janez@example.com" />
      </div>
    </div>

    <div class="space-y-2">
      <label for="booking-phone" class="text-xs uppercase tracking-widest text-gray-500 font-bold">Telefonska Številka</label>
      <input id="booking-phone" v-model="form.phone" type="tel" class="w-full border-b border-gray-300 focus:border-accent outline-none py-2 transition-colors" placeholder="041 123 456" />
    </div>

    <div class="space-y-4 pt-4">
      <span class="text-xs uppercase tracking-widest text-gray-500 font-bold block">Želeni Termini (Izberite več možnosti)</span>
      
      <!-- Weekdays -->
      <div class="flex flex-wrap gap-3 mb-4">
        <label v-for="day in days" :key="day" class="cursor-pointer">
          <input type="checkbox" :value="day" v-model="form.preferredDays" class="sr-only peer" />
          <span class="px-3 py-1 border border-gray-200 text-sm text-gray-600 peer-checked:bg-primary-light peer-checked:text-white peer-checked:border-primary-light peer-focus:ring-2 peer-focus:ring-primary peer-focus:ring-offset-1 transition-all select-none rounded-sm">
            {{ day }}
          </span>
        </label>
      </div>

      <!-- Time Slots -->
      <div class="flex flex-wrap gap-3">
        <label v-for="slot in slots" :key="slot" class="cursor-pointer">
          <input type="checkbox" :value="slot" v-model="form.preferredSlots" class="sr-only peer" />
          <span class="px-3 py-1 border border-gray-200 text-sm text-gray-600 peer-checked:bg-accent peer-checked:text-white peer-checked:border-accent peer-focus:ring-2 peer-focus:ring-accent peer-focus:ring-offset-1 transition-all select-none rounded-sm">
            {{ slot }}
          </span>
        </label>
      </div>
    </div>

    <div class="space-y-2">
      <label for="booking-message" class="text-xs uppercase tracking-widest text-gray-500 font-bold">Sporočilo (Opcijsko)</label>
      <textarea id="booking-message" v-model="form.message" rows="4" class="w-full border bg-gray-50 border-gray-200 focus:border-accent outline-none p-3 transition-colors text-sm"></textarea>
    </div>

    <button
      type="submit"
      :disabled="isSubmitting"
      class="w-full bg-primary text-white py-4 uppercase tracking-[0.15em] hover:bg-primary-dark transition-colors font-bold text-sm disabled:opacity-70 disabled:cursor-not-allowed"
    >
      <span v-if="isSubmitting">Pošiljam...</span>
      <span v-else>Pošlji Povpraševanje</span>
    </button>

    <div v-if="showSuccess" class="mt-4 p-4 bg-primary-light/10 text-primary-dark text-center rounded-sm border border-primary-light/20 flex items-center justify-center gap-2" role="alert">
      <svg class="w-5 h-5 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
      </svg>
      <span class="text-sm font-medium">Hvala! Vaše povpraševanje je bilo uspešno poslano.</span>
    </div>
  </form>
</template>

<script setup>
import { ref, reactive } from 'vue'

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

const isSubmitting = ref(false)
const showSuccess = ref(false)

const submitForm = async () => {
  if (isSubmitting.value) return

  isSubmitting.value = true

  // Simulate network delay
  await new Promise(resolve => setTimeout(resolve, 1500))

  console.log('Form Submitted:', form)

  isSubmitting.value = false
  showSuccess.value = true

  // Reset form
  form.name = ''
  form.email = ''
  form.phone = ''
  form.preferredDays = []
  form.preferredSlots = []
  form.message = ''

  // Hide success message after 5 seconds
  setTimeout(() => {
    showSuccess.value = false
  }, 5000)
}
</script>

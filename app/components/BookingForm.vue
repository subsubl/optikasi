<template>
  <form @submit.prevent="submitForm" class="space-y-6 bg-white p-8 border border-gray-100 shadow-sm">
    <!-- Hidden Web3Forms fields -->
    <input type="hidden" name="access_key" :value="accessKey" />
    <input type="hidden" name="subject" value="Nova rezervacija termina - OptikaSI" />
    <input type="hidden" name="from_name" value="OptikaSI Spletna Stran" />
    <input type="checkbox" name="botcheck" class="hidden" style="display: none;" />

    <div class="grid md:grid-cols-2 gap-6">
      <div class="space-y-2">
        <label for="name" class="text-xs uppercase tracking-widest text-gray-500 font-bold">Ime in Priimek</label>
        <input id="name" v-model="form.name" type="text" name="name" required class="w-full border-b border-gray-300 focus:border-accent outline-none py-2 transition-colors" placeholder="Janez Novak" />
      </div>
      <div class="space-y-2">
        <label for="email" class="text-xs uppercase tracking-widest text-gray-500 font-bold">Email Naslov</label>
        <input id="email" v-model="form.email" type="email" name="email" required class="w-full border-b border-gray-300 focus:border-accent outline-none py-2 transition-colors" placeholder="janez@example.com" />
      </div>
    </div>

    <div class="space-y-2">
      <label for="phone" class="text-xs uppercase tracking-widest text-gray-500 font-bold">Telefonska Številka</label>
      <input id="phone" v-model="form.phone" type="tel" name="phone" class="w-full border-b border-gray-300 focus:border-accent outline-none py-2 transition-colors" placeholder="041 123 456" />
    </div>

    <fieldset class="space-y-4 pt-4">
      <legend class="text-xs uppercase tracking-widest text-gray-500 font-bold block">Želeni Termini (Izberite več možnosti)</legend>

      <!-- Weekdays -->
      <div class="flex flex-wrap gap-3 mb-4">
        <label v-for="day in days" :key="day" class="cursor-pointer">
          <input type="checkbox" :value="day" v-model="form.preferredDays" class="sr-only peer" />
          <span class="px-3 py-1 border border-gray-200 text-sm text-gray-600 peer-checked:bg-primary-light peer-checked:text-white peer-checked:border-primary-light peer-focus-visible:ring-2 peer-focus-visible:ring-offset-2 peer-focus-visible:ring-primary-light transition-all select-none">
            {{ day }}
          </span>
        </label>
      </div>

      <!-- Time Slots -->
      <div class="flex flex-wrap gap-3">
        <label v-for="slot in slots" :key="slot" class="cursor-pointer">
          <input type="checkbox" :value="slot" v-model="form.preferredSlots" class="sr-only peer" />
          <span class="px-3 py-1 border border-gray-200 text-sm text-gray-600 peer-checked:bg-accent peer-checked:text-white peer-checked:border-accent peer-focus-visible:ring-2 peer-focus-visible:ring-offset-2 peer-focus-visible:ring-accent transition-all select-none">
            {{ slot }}
          </span>
        </label>
      </div>
    </fieldset>

    <div class="space-y-2">
      <label for="message" class="text-xs uppercase tracking-widest text-gray-500 font-bold">Sporočilo (Opcijsko)</label>
      <textarea id="message" v-model="form.message" name="message" rows="4" class="w-full border bg-gray-50 border-gray-200 focus:border-accent outline-none p-3 transition-colors text-sm"></textarea>
    </div>

    <!-- Status Messages -->
    <div v-if="submitStatus === 'success'" role="alert" aria-live="polite" class="bg-green-50 border border-green-200 text-green-700 px-4 py-3 rounded">
      ✓ Hvala za vaše povpraševanje! Kontaktirali vas bomo v najkrajšem možnem času.
    </div>
    <div v-if="submitStatus === 'error'" role="alert" aria-live="polite" class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded">
      ✗ Prišlo je do napake. Prosimo, poskusite znova ali nas kontaktirajte na info@optikasi.si
    </div>

    <button
      type="submit"
      :disabled="isSubmitting"
      class="w-full bg-primary text-white py-4 uppercase tracking-[0.15em] hover:bg-primary-dark transition-colors font-bold text-sm disabled:opacity-50 disabled:cursor-not-allowed"
    >
      <span v-if="isSubmitting">Pošiljam...</span>
      <span v-else>Pošlji Povpraševanje</span>
    </button>
  </form>
</template>

<script setup>
const accessKey = '01ce0d78-40da-4e31-a46d-a26af4c4752a'

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
const submitStatus = ref(null) // null, 'success', 'error'

const submitForm = async () => {
  isSubmitting.value = true
  submitStatus.value = null

  try {
    // Build the form data for Web3Forms
    const formData = {
      access_key: accessKey,
      subject: `Nova rezervacija termina - ${form.name}`,
      from_name: 'OptikaSI Spletna Stran',
      name: form.name,
      email: form.email,
      phone: form.phone || 'Ni naveden',
      'Želeni dnevi': form.preferredDays.length > 0 ? form.preferredDays.join(', ') : 'Ni izbrano',
      'Želeni termini': form.preferredSlots.length > 0 ? form.preferredSlots.join(', ') : 'Ni izbrano',
      message: form.message || 'Brez sporočila'
    }

    const response = await fetch('https://api.web3forms.com/submit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify(formData)
    })

    const result = await response.json()

    if (result.success) {
      submitStatus.value = 'success'
      // Reset form
      form.name = ''
      form.email = ''
      form.phone = ''
      form.preferredDays = []
      form.preferredSlots = []
      form.message = ''
    } else {
      submitStatus.value = 'error'
      console.error('Web3Forms error:', result)
    }
  } catch (error) {
    submitStatus.value = 'error'
    console.error('Submission error:', error)
  } finally {
    isSubmitting.value = false
  }
}
</script>

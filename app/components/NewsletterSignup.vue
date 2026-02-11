<template>
  <div class="bg-primary-dark text-white py-12 px-6 rounded-sm relative overflow-hidden">
    <!-- Decorative background element -->
    <div class="absolute top-0 right-0 -mr-16 -mt-16 w-64 h-64 border border-white/10 rounded-full"></div>

    <div class="relative z-10 max-w-xl mx-auto text-center">
      <span class="text-accent uppercase tracking-[0.2em] text-xs font-bold mb-3 block">VIP Klub</span>
      <h3 class="text-2xl font-serif mb-4">Postanite del naše zgodbe</h3>
      <p class="text-gray-300 text-sm mb-6 font-light leading-relaxed">
        Prijavite se na novičke in bodite prvi obveščeni o novih, ekskluzivnih kolekcijah ter dogodkih.
      </p>

      <form @submit.prevent="subscribe" class="flex flex-col sm:flex-row gap-4">
        <input
          v-model="email"
          type="email"
          placeholder="Vaš e-naslov"
          aria-label="Vaš e-naslov"
          required
          :disabled="isLoading"
          class="flex-grow bg-white/5 border border-white/20 text-white placeholder-gray-400 px-4 py-3 focus:outline-none focus-visible:ring-2 focus-visible:ring-accent focus:border-accent transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
        >
        <button
          type="submit"
          :disabled="isLoading"
          class="bg-accent text-white px-8 py-3 uppercase tracking-widest text-sm font-bold hover:bg-white hover:text-primary-dark transition-all duration-300 disabled:opacity-70 disabled:cursor-not-allowed"
        >
          {{ isLoading ? 'Prijavljanje...' : 'Prijavi se' }}
        </button>
      </form>
      <p v-if="success" role="status" class="text-accent text-xs mt-4 tracking-wide">Hvala za prijavo! Dobrodošli v klubu.</p>
    </div>
  </div>
</template>

<script setup>
const email = ref('')
const success = ref(false)
const isLoading = ref(false)

const subscribe = () => {
  if (isLoading.value) return

  isLoading.value = true
  console.log('Subscribing:', email.value)

  // Simulate API call
  setTimeout(() => {
    success.value = true
    email.value = ''
    isLoading.value = false
    setTimeout(() => success.value = false, 5000)
  }, 1000)
}
</script>

<template>
  <nav class="fixed w-full z-50 transition-all duration-300 bg-white/90 backdrop-blur-md shadow-sm">
    <div class="container mx-auto px-6 h-20 flex items-center justify-between">
      <!-- Logo -->
      <NuxtLink to="/" class="text-2xl font-serif font-bold text-primary-dark tracking-widest">
        OPTIKASI
      </NuxtLink>

      <!-- Mobile Menu Button -->
      <button @click="isOpen = !isOpen" class="md:hidden text-primary-dark focus:outline-none">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path v-if="!isOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>

      <!-- Desktop Links -->
      <div class="hidden md:flex space-x-8 items-center">
        <NuxtLink v-for="link in links" :key="link.path" :to="link.path" 
          class="text-sm uppercase tracking-widest text-gray-600 hover:text-accent transition-colors font-medium">
          {{ link.name }}
        </NuxtLink>
        <NuxtLink to="/kontakt" class="bg-primary text-white px-6 py-2 rounded-none hover:bg-primary-dark transition-colors uppercase text-xs tracking-widest">
          Naročite se
        </NuxtLink>
      </div>
    </div>

    <!-- Mobile Menu -->
    <div v-show="isOpen" class="md:hidden bg-white border-t">
      <div class="flex flex-col p-4 space-y-4">
        <NuxtLink v-for="link in links" :key="link.path" :to="link.path" 
          @click="isOpen = false"
          class="text-sm uppercase tracking-widest text-gray-600 hover:text-accent">
          {{ link.name }}
        </NuxtLink>
         <NuxtLink to="/kontakt" @click="isOpen = false" class="text-primary font-bold uppercase text-sm tracking-widest">
          Naročite se
        </NuxtLink>
      </div>
    </div>
  </nav>
</template>

<script setup>
const isOpen = ref(false)
const links = [
  { name: 'Domov', path: '/' },
  { name: 'O Nas', path: '/o-nas' },
  { name: 'Storitve', path: '/storitve' },
  { name: 'Korekcijska Očala', path: '/korekcijska-ocala' },
  { name: 'Sončna Očala', path: '/soncna-ocala' },
  { name: 'Znamke', path: '/znamke' },
  { name: 'Trgovina', path: '/trgovina' },
]
</script>

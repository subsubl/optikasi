<template>
  <nav class="fixed w-full z-50 transition-all duration-300 bg-white/90 backdrop-blur-md shadow-sm">
    <div class="container mx-auto px-6 h-20 flex items-center justify-between">
      <!-- Logo -->
      <NuxtLink to="/" class="text-2xl font-serif font-bold text-primary-dark tracking-widest">
        OPTIKASI
      </NuxtLink>

      <!-- Mobile Menu Button -->
      <button
        @click="isOpen = !isOpen"
        class="md:hidden text-primary-dark focus:outline-none"
        aria-label="Glavni meni"
        :aria-expanded="isOpen"
        aria-controls="mobile-menu"
      >
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path v-if="!isOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>

      <!-- Desktop Links -->
      <div class="hidden md:flex space-x-8 items-center">
        <div v-for="link in links" :key="link.path" class="relative group h-20 flex items-center">
          <NuxtLink :to="link.path" 
            class="text-sm uppercase tracking-widest text-gray-600 hover:text-accent transition-colors font-medium h-full flex items-center">
            {{ link.name }}
          </NuxtLink>
           <!-- Dropdown -->
            <div v-if="link.children" class="absolute left-0 top-full w-72 bg-white shadow-lg py-2 border-t-2 border-primary opacity-0 invisible group-hover:opacity-100 group-hover:visible group-focus-within:opacity-100 group-focus-within:visible transition-all duration-300 transform origin-top-left z-50">
                <NuxtLink v-for="child in link.children" :key="child.path" :to="child.path" class="block px-6 py-3 text-xs text-gray-600 hover:text-primary hover:bg-gray-50 uppercase tracking-wider border-b border-gray-50 last:border-0 text-left">
                    {{ child.name }}
                </NuxtLink>
            </div>
        </div>
        <NuxtLink to="/kontakt" class="bg-primary text-white px-6 py-2 rounded-none hover:bg-primary-dark transition-colors uppercase text-xs tracking-widest ml-4">
          Naročite se
        </NuxtLink>
      </div>
    </div>

    <!-- Mobile Menu -->
    <div v-show="isOpen" id="mobile-menu" class="md:hidden bg-white border-t max-h-[80vh] overflow-y-auto">
      <div class="flex flex-col p-4 space-y-4">
        <template v-for="link in links" :key="link.path">
           <div class="flex flex-col">
                <NuxtLink :to="link.path" 
                @click="isOpen = false"
                class="text-sm uppercase tracking-widest text-gray-600 hover:text-accent mb-2">
                {{ link.name }}
                </NuxtLink>
                 <div v-if="link.children" class="pl-4 border-l-2 border-gray-100 space-y-3 mb-2">
                     <NuxtLink v-for="child in link.children" :key="child.path" :to="child.path"
                        @click="isOpen = false"
                        class="block text-xs uppercase tracking-wide text-gray-500 hover:text-accent">
                        {{ child.name }}
                    </NuxtLink>
                </div>
           </div>
        </template>
         <NuxtLink to="/kontakt" @click="isOpen = false" class="text-primary font-bold uppercase text-sm tracking-widest mt-2 block">
          Naročite se
        </NuxtLink>
      </div>
    </div>
  </nav>
</template>

<script setup>
const isOpen = ref(false)
const links = [


  { name: 'Storitve', path: '/storitve' },
  { name: 'Korekcijska Očala', path: '/korekcijska-ocala' },
  { name: 'Sončna Očala', path: '/soncna-ocala' },
  { name: 'Športna Očala', path: '/sportna-ocala' },
  { name: 'Očala za Vožnjo', path: '/ocala-za-voznjo' },
  { 
      name: 'Varnostna Očala', 
      path: '/varnostna-ocala',
      children: [
          { name: 'Industrija in rudarstvo', path: '/varnostna-ocala/industrija-in-rudarstvo' },
          { name: 'Farmacija in biotehnologija', path: '/varnostna-ocala/farmacija-in-biotehnologija' },
          { name: 'Obrt in Delavnica', path: '/varnostna-ocala/obrtna-delavnica' },
          { name: 'Gozdarstvo in kmetijstvo', path: '/varnostna-ocala/gozdarstvo' },
          { name: 'Gradbeništvo in zunanja dela', path: '/varnostna-ocala/gradbenistvo' },
          { name: 'IT in Pisarne', path: '/varnostna-ocala/pisarne' }
      ]
  },
  { name: 'Znamke', path: '/znamke' },
  { name: 'Trgovina', path: '/trgovina' },
]
</script>

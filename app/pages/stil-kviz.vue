<template>
  <div class="py-24 container mx-auto px-6 max-w-2xl">
    <div class="text-center mb-12">
      <h1 class="text-4xl text-primary-dark mb-4">Stil Kviz</h1>
      <p class="text-gray-600">Odkrijte katera oblika okvirja vam najbolj pristaja.</p>
    </div>

    <div class="bg-white p-8 md:p-12 shadow-sm border border-gray-100">
      <!-- Step Indicator -->
      <div class="flex justify-center mb-12">
        <div v-for="s in 3" :key="s" class="flex items-center">
          <div :class="[
            'w-10 h-10 rounded-full flex items-center justify-center text-sm font-bold transition-colors',
            step >= s ? 'bg-accent text-white' : 'bg-gray-100 text-gray-400'
          ]">{{ s }}</div>
          <div v-if="s < 3" class="w-12 h-0.5 bg-gray-200"></div>
        </div>
      </div>

      <!-- Step 1: Face Shape -->
      <div v-if="step === 1" class="space-y-6">
        <h2 class="text-2xl font-serif text-primary-dark text-center mb-8">Kakšna je oblika vašega obraza?</h2>
        <div class="grid grid-cols-2 gap-4">
          <button 
            v-for="shape in faceShapes" 
            :key="shape.id"
            @click="selectFaceShape(shape.id)"
            :aria-pressed="form.faceShape === shape.id"
            :class="[
              'p-6 border text-center transition-all duration-300 focus-visible:ring-2 focus-visible:ring-accent focus:outline-none hover:-translate-y-1 hover:shadow-md',
              form.faceShape === shape.id ? 'border-accent bg-accent/5' : 'border-gray-200 hover:border-gray-300'
            ]"
          >
            <span class="text-4xl block mb-2">{{ shape.icon }}</span>
            <span class="font-medium">{{ shape.name }}</span>
          </button>
        </div>
      </div>

      <!-- Step 2: Style Preference -->
      <div v-if="step === 2" class="space-y-6">
        <h2 class="text-2xl font-serif text-primary-dark text-center mb-8">Kateri stil vam je najbližji?</h2>
        <div class="grid grid-cols-1 gap-4">
          <button 
            v-for="style in styles" 
            :key="style.id"
            @click="selectStyle(style.id)"
            :aria-pressed="form.style === style.id"
            :class="[
              'p-6 border text-left transition-all duration-300 flex items-center space-x-4 focus-visible:ring-2 focus-visible:ring-accent focus:outline-none hover:-translate-y-1 hover:shadow-md',
              form.style === style.id ? 'border-accent bg-accent/5' : 'border-gray-200 hover:border-gray-300'
            ]"
          >
            <span class="text-3xl">{{ style.icon }}</span>
            <div>
              <span class="font-medium block">{{ style.name }}</span>
              <span class="text-sm text-gray-500">{{ style.desc }}</span>
            </div>
          </button>
        </div>
      </div>

      <!-- Step 3: Budget -->
      <div v-if="step === 3" class="space-y-6">
        <h2 class="text-2xl font-serif text-primary-dark text-center mb-8">Kakšen je vaš proračun?</h2>
        <div class="grid grid-cols-1 gap-4">
          <button 
            v-for="budget in budgets" 
            :key="budget.id"
            @click="selectBudget(budget.id)"
            :aria-pressed="form.budget === budget.id"
            :class="[
              'p-6 border text-center transition-all duration-300 focus-visible:ring-2 focus-visible:ring-accent focus:outline-none hover:-translate-y-1 hover:shadow-md',
              form.budget === budget.id ? 'border-accent bg-accent/5' : 'border-gray-200 hover:border-gray-300'
            ]"
          >
            <span class="font-medium block text-lg">{{ budget.name }}</span>
            <span class="text-sm text-gray-500">{{ budget.range }}</span>
          </button>
        </div>
      </div>

      <!-- Results -->
      <div v-if="step === 4" class="text-center space-y-8">
        <div class="text-accent text-6xl mb-4">✓</div>
        <h2 class="text-2xl font-serif text-primary-dark">Vaše priporočilo</h2>
        <p class="text-gray-600">Na podlagi vaših odgovorov vam priporočamo:</p>
        <div class="bg-cream p-6 rounded-sm">
          <p class="font-serif text-xl text-primary-dark">{{ recommendation }}</p>
        </div>
        <NuxtLink to="/kontakt" class="inline-block bg-primary-dark text-white px-8 py-4 uppercase tracking-widest hover:bg-accent transition-colors">
          Rezervirajte Posvet
        </NuxtLink>
      </div>

      <!-- Navigation -->
      <div v-if="step < 4" class="flex justify-between mt-12">
        <button v-if="step > 1" @click="step--" class="text-gray-500 hover:text-primary transition-colors focus-visible:ring-2 focus-visible:ring-accent focus:outline-none rounded-sm px-2">
          ← Nazaj
        </button>
        <div v-else></div>
      </div>
    </div>
  </div>
</template>

<script setup>
useHead({
  title: 'Stil Kviz - Najdi Svoj Okvir',
  meta: [
    { name: 'description', content: 'Odkrijte kateri okvirji očal vam najbolj pristajajo glede na obliko obraza in osebni stil.' }
  ]
})

const step = ref(1)

const form = reactive({
  faceShape: '',
  style: '',
  budget: ''
})

const faceShapes = [
  { id: 'round', name: 'Okrogla', icon: '🔵' },
  { id: 'oval', name: 'Ovalna', icon: '🥚' },
  { id: 'square', name: 'Kvadratna', icon: '🟨' },
  { id: 'heart', name: 'Srčasta', icon: '💜' }
]

const styles = [
  { id: 'classic', name: 'Klasika', desc: 'Brezčasni okvirji, ki nikoli ne gredo iz mode.', icon: '🎩' },
  { id: 'modern', name: 'Sodobno', desc: 'Čiste linije in minimalistična estetika.', icon: '✨' },
  { id: 'bold', name: 'Drzno', desc: 'Izraziti okvirji, ki pritegnejo pozornost.', icon: '🔥' }
]

const budgets = [
  { id: 'essential', name: 'Esencialno', range: 'Do 150 €' },
  { id: 'premium', name: 'Premium', range: '150 – 350 €' },
  { id: 'luxury', name: 'Luksuz', range: 'Nad 350 €' }
]

const recommendation = computed(() => {
  const recs = {
    'round-classic': 'Pravokotni ali kvadratni okvirji (npr. Ray-Ban Wayfarer)',
    'round-modern': 'Geometrijski okvirji z ostrimi robovi (npr. Lindberg)',
    'round-bold': 'Veliki kvadratni okvirji (npr. Gucci Square)',
    'oval-classic': 'Aviator ali okrogli okvirji (npr. Ray-Ban Aviator)',
    'oval-modern': 'Minimalistični rimless okvirji (npr. Lindberg Air)',
    'oval-bold': 'Cat-eye ali oversized okvirji (npr. Tom Ford)',
    'square-classic': 'Okrogli ali ovalni okvirji (npr. Persol 649)',
    'square-modern': 'Tanki kovinski okvirji (npr. Oliver Peoples)',
    'square-bold': 'Geometrični okvirji z mehkimi robovi',
    'heart-classic': 'Aviator ali bottom-heavy okvirji',
    'heart-modern': 'Rimless ali poltransparentni okvirji',
    'heart-bold': 'Cat-eye ali retro oblika'
  }
  const key = `${form.faceShape}-${form.style}`
  return recs[key] || 'Za osebno priporočilo vas vabimo na posvet.'
})

const selectFaceShape = (id) => {
  form.faceShape = id
  step.value = 2
}

const selectStyle = (id) => {
  form.style = id
  step.value = 3
}

const selectBudget = (id) => {
  form.budget = id
  step.value = 4
}
</script>

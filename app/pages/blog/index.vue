<template>
  <div class="max-w-6xl mx-auto px-4 py-8">
    <h1 class="font-serif text-4xl md:text-5xl text-primary-dark mb-8">Blog</h1>
    
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      <div v-for="post in posts" :key="post.slug" class="bg-white rounded-lg shadow-md overflow-hidden">
        <NuxtLink :to="post.slug">
          <img :src="post.image" :alt="post.title" class="w-full h-48 object-cover">
        </NuxtLink>
        <div class="p-6">
          <span class="text-sm text-accent font-semibold">{{ post.category }}</span>
          <NuxtLink :to="post.slug" class="block mt-2 text-primary-dark hover:text-accent font-serif text-xl">
            {{ post.title }}
          </NuxtLink>
          <p class="mt-2 text-gray-600">{{ post.excerpt }}</p>
          <p class="mt-4 text-sm text-gray-500">{{ formatDate(post.date) }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const formatDate = (dateString: string) => {
  const options: Intl.DateTimeFormatOptions = { year: 'numeric', month: 'long', day: 'numeric' }
  return new Date(dateString).toLocaleDateString('sl-SI', options)
}

const posts = [
  {
    title: 'Zakaj 1 na 1 pregled očesnih stekel?',
    slug: '/blog/zakaj-1-na-1',
    category: 'Očesna zdravstvena varnost',
    image: '/images/blog/zakaj-1-na-1.jpg',
    excerpt: 'Spoznajte prednosti posameznega pregleda očesnih stekel.',
    date: '2023-01-15'
  },
  {
    title: 'Izbira očesnih stekel glede na obliko obraza',
    slug: '/blog/izbira-ocala-oblika-obraza',
    category: 'Izbira očesnih stekel',
    image: '/images/blog/izbira-ocala-oblika-obraza.jpg',
    excerpt: 'Kako izbrati pravilne očesne stekle glede na obliko obraza.',
    date: '2023-02-20'
  },
  {
    title: 'Barvane očesne stekle – trend 2026',
    slug: '/blog/obarvana-ocala-trend-2026',
    category: 'Trendi',
    image: '/images/blog/obarvana-ocala-trend-2026.jpg',
    excerpt: 'Spoznajte najnovejše trende v barvanih očesnih stekel.',
    date: '2023-03-10'
  },
  {
    title: 'Retro sončne očesne stekle 2026',
    slug: '/blog/retro-soncna-ocala-2026',
    category: 'Trendi',
    image: '/images/blog/retro-soncna-ocala-2026.jpg',
    excerpt: 'Retro stil v sončnih očesnih stekel.',
    date: '2023-04-05'
  },
  {
    title: 'UVEX Guide – zaščita za oči',
    slug: '/blog/uvex-guide',
    category: 'Očesna zaščita',
    image: '/images/blog/uvex-guide.jpg',
    excerpt: 'Kompleten vodnik o UVEX zaščiti za oči.',
    date: '2023-05-01'
  },
  {
    title: 'Modra svetloba in oči: kaj res deluje za zaslone',
    slug: '/blog/modra-svetloba-in-oci',
    category: 'Zdravje oči',
    image: '/images/blog/modra-svetloba-in-oci.jpg',
    excerpt: 'Spoznajte, kako modra svetloba vpliva na naše oči in kakšne mere za zaščito obstajajo.',
    date: '2023-05-15'
  },
  {
    title: 'Kdaj naj gre otrok prvič na pregled vida?',
    slug: '/blog/otrokov-prvicni-pregled-vida',
    category: 'Očesna zdravstvena varnost',
    image: '/images/blog/otrokov-prvicni-pregled-vida.jpg',
    excerpt: 'Spoznajte, kdaj naj otrok prvič obišče optikala in kakšne znake naj starši opazijo.',
    date: '2023-06-20'
  },
  {
    title: 'UV zaščita za oči skozi vse leto',
    slug: '/blog/uv-zascita-z-ocmi',
    category: 'Očesna zaščita',
    image: '/images/blog/uv-zascita-z-ocmi.jpg',
    excerpt: 'Spoznajte, zakaj je UV zaščita pomembna za oči skozi vse leto in kakšne so zaščitne lastnosti sončnih očesnih stekel.',
    date: '2023-07-10'
  },
  {
    title: 'Kontaktne leče: vodič od izbire do nošenja',
    slug: '/blog/kontaktne-lece-vodic',
    category: 'Kontaktne leče',
    image: '/images/blog/kontaktne-lece-vodic.jpg',
    excerpt: 'Izvedite več o različnih vrstah kontaktnih leč, njihovi izbiri, prilagajanju, higieni in varnosti.',
    date: '2026-08-15'
  },
  {
    title: 'Progresivna stekla: za koga so in kako se nanje navaditi',
    slug: '/blog/progresivna-stekla',
    category: 'Stekla',
    image: '/images/blog/progresivna-stekla.jpg',
    excerpt: 'Spoznajte, kaj so progresivna stekla, za koga so primerna in kako poteka prilagajanje na njih.',
    date: '2026-08-16'
  },
  {
    title: 'Nanosi na lečah: antirefleksni, oleo/hidrofobni, UV',
    slug: '/blog/nanosi-na-lecah',
    category: 'Tehnologija',
    image: '/images/blog/nanosi-na-lecah.jpg',
    excerpt: 'Razložimo, kaj so antirefleksni, oleo/hidrofobni in UV nanosi ter kako izbrati prave za vaš način življenja.',
    date: '2026-08-17'
  }
]
</script>
<template>
  <div class="py-24 container mx-auto px-6">
    <div class="text-center mb-20">
      <h1 class="font-serif text-5xl text-primary-dark mb-4">Blog & Svetovanje</h1>
      <p class="text-gray-500 tracking-widest uppercase text-sm">Vaš vir informacij za boljši vid</p>
    </div>

    <div class="grid md:grid-cols-2 gap-12 max-w-5xl mx-auto">
      <article v-for="post in posts" :key="post.slug" class="group bg-white border border-gray-100 overflow-hidden shadow-sm hover:shadow-xl transition-all duration-500">
        <NuxtLink :to="post.slug" class="block">
          <div class="h-64 overflow-hidden relative">
            <img :src="post.image" :alt="post.title" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
            <div class="absolute top-4 left-4 bg-accent text-white text-[10px] uppercase tracking-widest px-3 py-1 font-bold">
               {{ post.category }}
            </div>
          </div>
          <div class="p-8">
            <h2 class="font-serif text-2xl text-primary-dark mb-4 group-hover:text-accent transition-colors">{{ post.title }}</h2>
            <p class="text-gray-600 text-sm leading-relaxed mb-6 line-clamp-3">{{ post.excerpt }}</p>
            <span class="text-xs uppercase tracking-widest font-bold border-b border-accent pb-1">Preberi več →</span>
          </div>
        </NuxtLink>
      </article>
    </div>
  </div>
</template>

<script setup>
useHead({
  title: 'Blog in nasveti o vidu | Optika Si Ljubljana',
  meta: [
    { name: 'description', content: 'Preberite strokovne nasvete o zdravju oči, vodiče za izbiro očal in novosti iz sveta optike.' }
  ]
})

const posts = [
  {
    title: 'Retro sončna očala 2026: Povratek 70-ih',
    slug: '/blog/retro-soncna-ocala-2026',
    category: 'Trendi 2026',
    excerpt: 'Oversized okvirji in futuristični vizirji so nazaj. Poglejte, kako 70-ta leta navdihujejo letošnjo pomlad v Ljubljani.',
    image: '/images/shop/studio-optika-si.png'
  },
  {
    title: 'Ljubljana Ulični Stil 2026: Obarvana Očala',
    slug: '/blog/obarvana-ocala-trend-2026',
    category: 'Trendi 2026',
    excerpt: 'Zakaj so nežno obarvana očala (soft tints) nova maskara? Trend, ki definira ulice Ljubljane.',
    image: '/images/coatings/mirror-rose.jpg'
  },
  {
    title: 'Kako izbrati prava očala za vašo obliko obraza?',
    slug: '/blog/izbira-ocala-oblika-obraza',
    category: 'Svetovanje',
    excerpt: 'Izbira popolnih očal je kombinacija umetnosti in znanosti. Spoznajte, kateri okvirji najbolje pristajajo vašemu obrazu in kako poudariti svoje najlepše poteze.',
    image: '/images/fashion/swarovski/Glasses-Swarovski2.jpg'
  },
  {
    title: 'Zakaj je 1-na-1 pregled vida ključen?',
    slug: '/blog/zakaj-1-na-1',
    category: 'Svetovanje',
    excerpt: 'Ste se kdaj vprašali, zakaj nekateri pregledi vida trajajo le 15 minut, drugi pa celo uro? Spoznajte prednosti 60-minutnega termina.',
    image: '/images/hero_services.png'
  },
  {
    title: 'Vodič po športnih očalih Uvex',
    slug: '/blog/uvex-guide',
    category: 'Športna optika',
    excerpt: 'Običajni okvirji niso zasnovani za ekstremne gibe. Spoznajte nelomljive okvirje in Colorvision tehnologijo podjetja Uvex.',
    image: '/images/sport/hero-general.jpg'
  }
]
</script>

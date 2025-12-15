// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss', '@nuxtjs/sitemap', '@nuxtjs/robots'],
  site: {
    url: 'https://optikasi.si',
    name: 'OptikaSI'
  },
  app: {
    head: {
      titleTemplate: '%s | Optika Ljubljana',
      link: [
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap' },
        { rel: 'stylesheet', href: 'https://cdn.snipcart.com/themes/v3.4.1/default/snipcart.css' }
      ],
      script: [
        { src: 'https://cdn.snipcart.com/themes/v3.4.1/default/snipcart.js', async: true }
      ]
    },
    baseURL: '/optikasi/'
  }
})
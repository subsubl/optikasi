// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss', '@nuxtjs/sitemap', '@nuxtjs/robots'],
  robots: {
    robotsTxt: false
  },
  site: {
    url: 'https://optikasi.si',
    name: 'OptikaSI'
  },
  app: {
    head: {
      titleTemplate: '%s | Optika Ljubljana',
      link: [
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Source+Sans+3:wght@300;400;600;700&display=swap&subset=latin-ext' },
        { rel: 'stylesheet', href: 'https://cdn.snipcart.com/themes/v3.4.1/default/snipcart.css' },
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
        { rel: 'icon', type: 'image/png', href: '/icon.png' }
      ],
      script: [
        { src: 'https://cdn.snipcart.com/themes/v3.4.1/default/snipcart.js', async: true }
      ]
    },
    // Use '/' for optikasi.si, '/optikasi/' for GitHub Pages
    baseURL: process.env.NUXT_APP_BASE_URL || '/'
  }
})
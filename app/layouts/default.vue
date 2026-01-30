<template>
  <div class="flex flex-col min-h-screen bg-cream font-sans">
    <AppNavbar />
    <main class="flex-grow pt-20"> <!-- Padding top for fixed navbar -->
      <slot />
      <InstagramFeed />
      <div class="container mx-auto px-6 mt-16 mb-12">
        <NewsletterSignup />
      </div>
    </main>
    <footer class="bg-primary-dark text-white py-12">
      <div class="container mx-auto px-6 text-center">
        <h3 class="font-serif text-2xl tracking-widest mb-6">OPTIKASI</h3>
        <p class="text-sm tracking-wide opacity-80 mb-6">Vojkova cesta 58, Ljubljana<br>info@optikasi.si | 041 788 516</p>
        
        <!-- Social Links -->
        <a href="https://www.instagram.com/optikasi/?hl=en" target="_blank" rel="noopener noreferrer" class="inline-block text-white hover:text-accent transition-colors mb-6">
          <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path fill-rule="evenodd" d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772 4.902 4.902 0 011.772-1.153c.636-.247 1.363-.416 2.427-.465 1.067-.047 1.409-.06 4.123-.06h.08zM12.001 5.838c-3.403 0-6.162 2.76-6.162 6.162s2.76 6.162 6.162 6.162 6.162-2.76 6.162-6.162-2.76-6.162-6.162-6.162zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.88 1.44 1.44 0 000-2.88z" clip-rule="evenodd" />
          </svg>
        </a>

        <p class="text-xs text-gray-400">&copy; {{ new Date().getFullYear() }} OptikaSI. Vse pravice pridržane.</p>
      </div>
    </footer>
  </div>
</template>

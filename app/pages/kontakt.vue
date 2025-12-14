<template>
  <div class="py-24 container mx-auto px-6">
    <div class="grid md:grid-cols-2 gap-16">
      
      <!-- Contact Info -->
      <div>
        <h1 class="text-4xl text-primary-dark mb-8">Stopite v Stik</h1>
        <p class="text-gray-600 mb-12 leading-relaxed text-lg">
          Za osebni posvet in strokovni pregled vida nas kontaktirajte ali izpolnite obrazec.
          Veselimo se vašega obiska v našem butiku.
        </p>

        <div class="space-y-8">
          <div>
            <h3 class="text-accent uppercase tracking-widest text-xs font-bold mb-2">Naslov</h3>
            <p class="text-xl text-primary-dark font-serif">Vojkova cesta 58<br>1000 Ljubljana</p>
          </div>

          <div>
            <h3 class="text-accent uppercase tracking-widest text-xs font-bold mb-2">Kontakt</h3>
            <p class="text-lg text-gray-700">info@optikasi.si</p>
            <p class="text-lg text-gray-700">041 788 516</p>
          </div>

          <div>
             <h3 class="text-accent uppercase tracking-widest text-xs font-bold mb-2">Delovni Čas</h3>
             <p class="text-gray-600">Po dogovoru (Prosimo, rezervirajte termin)</p>
          </div>

          <div>
            <h3 class="text-accent uppercase tracking-widest text-xs font-bold mb-2">Socialna Omrežja</h3>
            <a href="https://www.instagram.com/optikasi/?hl=en" target="_blank" rel="noopener noreferrer" class="flex items-center space-x-2 text-gray-700 hover:text-primary transition-colors">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                <path fill-rule="evenodd" d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772 4.902 4.902 0 011.772-1.153c.636-.247 1.363-.416 2.427-.465 1.067-.047 1.409-.06 4.123-.06h.08zM12.001 5.838c-3.403 0-6.162 2.76-6.162 6.162s2.76 6.162 6.162 6.162 6.162-2.76 6.162-6.162-2.76-6.162-6.162-6.162zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.88 1.44 1.44 0 000-2.88z" clip-rule="evenodd" />
              </svg>
              <span class="text-lg">@optikasi</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Booking Form -->
      <div>
        <BookingForm />
      </div>

    </div>
  </div>
</template>

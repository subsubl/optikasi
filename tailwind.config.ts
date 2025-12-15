/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./app/components/**/*.{js,vue,ts}",
        "./app/layouts/**/*.vue",
        "./app/pages/**/*.vue",
        "./app/plugins/**/*.{js,ts}",
        "./app/app.vue",
        "./app/error.vue",
    ],
    theme: {
        extend: {
            colors: {
                primary: {
                    DEFAULT: '#1B4D3E', // Deep Forest Green
                    light: '#2C6E5A',
                    dark: '#113329',
                },
                accent: {
                    DEFAULT: '#D4AF37', // Gold/Bronze
                    light: '#E5C564',
                },
                cream: {
                    DEFAULT: '#F9F7F2', // Warm off-white
                    dark: '#EBE7DD',
                }
            },
            fontFamily: {
                serif: ['Cormorant Garamond', 'serif'],
                sans: ['Source Sans 3', 'sans-serif'],
            },
            container: {
                center: true,
                padding: '1rem',
            }
        },
    },
    plugins: [],
}

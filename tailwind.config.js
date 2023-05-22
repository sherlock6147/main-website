/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/base/**/*.{html,js}",
    "./app/projects/**/*.{html,js}",
    "./app/website/**/*.{html,js}"
  ],
  theme: {
    extend: {
      fontFamily: {
        'ubuntu-mono': ["'Ubuntu Mono'",'mono','sans-serif'],
        'gugi': ["'Gugi'",'mono','sans-serif'],
        'raleway': ["'Raleway'",'sans-serif'],
      }
    },
  },
  plugins: [],
}

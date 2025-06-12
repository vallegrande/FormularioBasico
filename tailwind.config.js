/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",     // Para archivos HTML en Flask
    "./static/**/*.js",          // Si usas JS con clases Tailwind
    "./**/*.py"                  // Opcional: si generas clases desde Flask
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

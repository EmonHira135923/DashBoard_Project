/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html/", // template at the project level   
    "./**/templates/**/*.html/", // template at the inside app file level   

  ],
  theme: {
    extend: {},
  },
  plugins: [],
}


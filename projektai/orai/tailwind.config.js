module.exports = {
  content: [
    "./src/data/DailyData.jsx",
    "./src/data/GetData.jsx",
    "./src/data/HourlyData.jsx",
    "./src/data/CurrentData.jsx",
    "./src/App.js"
  ],
  theme: {
    extend: {
      backgroundImage: (theme) => ({
        night: "url('./img/pink.jpg')",
      })
    },
  },
  plugins: [],
}

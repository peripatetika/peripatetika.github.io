// za verziju sa strelicom
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("main a").forEach(el => {
    // If the visible text equals the Croatian translation
    if (el.textContent.trim() === "Natrag na indeks") {
      // Replace the text
      el.textContent = "Natrag na početnu";
      
      // Add the left arrow before the text
      const arrow = document.createElement("span");
      arrow.textContent = "‹"; // Unicode left arrow
      el.prepend(arrow);
    }
  });
});


// za verziju bez strelice
// document.addEventListener("DOMContentLoaded", () => {
//   document.querySelectorAll("main a").forEach(el => {
//     // If the visible text equals the Croatian translation
//     if (el.textContent.trim() === "Natrag na indeks") {
//       el.textContent = "Natrag na početnu";
//     }
//   });
// });


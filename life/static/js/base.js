document.addEventListener("DOMContentLoaded", () => {
  console.log("Base JS loaded ✔");
});

/* OPTIONAL: COPY URL FUNCTION */
function copyURL(btn) {
  navigator.clipboard.writeText(window.location.href);
  btn.innerText = "Copied!";
  setTimeout(() => btn.innerText = "🔗 Copy URL", 1500);
}

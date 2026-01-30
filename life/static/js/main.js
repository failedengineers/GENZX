function showResult() {
  const cls = document.getElementById("class").value;
  const sem = document.getElementById("sem").value;

  if (!cls || !sem) {
    alert("Select class and semester");
    return;
  }

}
function copyURL(btn) {
  navigator.clipboard.writeText(window.location.href);

  btn.textContent = "✅ Copied";
  btn.style.opacity = "0.7";

  setTimeout(() => {
    btn.textContent = "🔗 Copy URL";
    btn.style.opacity = "1";
  }, 1500);
}

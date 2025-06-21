document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.getElementById("menu-toggle");
  const nav = document.getElementById("nav-links");

  if (toggle && nav) {
    toggle.addEventListener("click", () => {
      if (nav.classList.contains("active")) {
        nav.style.opacity = 0;
        nav.style.transform = "translateY(-10px)";
        setTimeout(() => {
          nav.classList.remove("active");
        }, 300); // Match CSS transition duration
      } else {
        nav.classList.add("active");
        setTimeout(() => {
          nav.style.opacity = 1;
          nav.style.transform = "translateY(0)";
        }, 10); // Tiny delay to trigger transition
      }

      toggle.classList.toggle("open");
    });
  }
});

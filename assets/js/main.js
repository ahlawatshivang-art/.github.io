// Highlights the current tab and fades sections in as you scroll.
document.documentElement.classList.remove("no-js");

// Active tab: matches the current file name to each tab's href
const page = location.pathname.split("/").pop() || "index.html";
document.querySelectorAll(".tabs a").forEach(a => {
  if (a.getAttribute("href") === page) a.classList.add("active");
});

// Fade-ins: any element with class="reveal" fades in when it scrolls into view
const items = document.querySelectorAll(".reveal");
if ("IntersectionObserver" in window) {
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add("visible"); io.unobserve(e.target); }
    });
  }, { threshold: 0.12 });
  items.forEach(el => io.observe(el));
} else {
  items.forEach(el => el.classList.add("visible"));
}

// Footer year
const y = document.getElementById("year");
if (y) y.textContent = new Date().getFullYear();

document.body.classList.add("js-ready");

const header = document.getElementById("header");
const navToggle = document.querySelector(".nav-toggle");
const navLinks = document.getElementById("nav-links");
const leadForm = document.getElementById("lead-form");

const syncHeader = () => {
  if (!header) return;
  header.classList.toggle("is-scrolled", window.scrollY > 10);
};

syncHeader();
window.addEventListener("scroll", syncHeader, { passive: true });

if (navToggle && navLinks) {
  navToggle.addEventListener("click", () => {
    const isOpen = navLinks.classList.toggle("is-open");
    navToggle.classList.toggle("is-open", isOpen);
    navToggle.setAttribute("aria-expanded", String(isOpen));
  });

  navLinks.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      navLinks.classList.remove("is-open");
      navToggle.classList.remove("is-open");
      navToggle.setAttribute("aria-expanded", "false");
    });
  });
}

const revealItems = document.querySelectorAll(".reveal");

if (revealItems.length) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    {
      rootMargin: "0px 0px -12% 0px",
      threshold: 0.14,
    },
  );

  revealItems.forEach((item) => observer.observe(item));
}

if (leadForm) {
  leadForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const data = new FormData(leadForm);
    const name = (data.get("name") || "").toString().trim();
    const company = (data.get("company") || "").toString().trim();
    const contact = (data.get("contact") || "").toString().trim();
    const stage = (data.get("stage") || "").toString().trim();
    const need = (data.get("need") || "").toString().trim();

    const message = [
      "Oi, vim pelo site da AVANT e quero agendar uma reunião.",
      "",
      `Nome: ${name}`,
      `Empresa: ${company || "Não informado"}`,
      `Contato: ${contact}`,
      `Momento da marca: ${stage}`,
      `O que precisa mudar agora: ${need}`,
    ].join("\n");

    window.open(`https://wa.me/5538999351032?text=${encodeURIComponent(message)}`, "_blank", "noreferrer");
  });
}

(() => {
  const body = document.body;
  const menuToggle = document.querySelector(".menu-toggle");
  const sidebar = document.getElementById("sidebar");
  const progressBar = document.querySelector(".page-progress > span");
  const searchInput = document.getElementById("navSearch");
  const navLinks = Array.from(document.querySelectorAll(".nav-link"));

  if (menuToggle && sidebar) {
    menuToggle.addEventListener("click", () => {
      const isOpen = body.classList.toggle("menu-open");
      menuToggle.setAttribute("aria-expanded", String(isOpen));
    });

    document.addEventListener("click", (event) => {
      if (!body.classList.contains("menu-open")) return;
      const target = event.target;
      if (!(target instanceof Node)) return;
      const clickedInsideSidebar = sidebar.contains(target);
      const clickedToggle = menuToggle.contains(target);
      if (!clickedInsideSidebar && !clickedToggle) {
        body.classList.remove("menu-open");
        menuToggle.setAttribute("aria-expanded", "false");
      }
    });

    navLinks.forEach((link) => {
      link.addEventListener("click", () => {
        if (window.matchMedia("(max-width: 1120px)").matches) {
          body.classList.remove("menu-open");
          menuToggle.setAttribute("aria-expanded", "false");
        }
      });
    });
  }

  if (searchInput) {
    searchInput.addEventListener("input", () => {
      const query = searchInput.value.trim().toLowerCase();
      navLinks.forEach((link) => {
        const title = (link.dataset.title || link.textContent || "").toLowerCase();
        link.hidden = query.length > 0 && !title.includes(query);
      });
    });
  }

  const updateProgress = () => {
    if (!progressBar) return;
    const scrollTop = window.scrollY;
    const height = document.documentElement.scrollHeight - window.innerHeight;
    const ratio = height <= 0 ? 1 : Math.min(1, Math.max(0, scrollTop / height));
    progressBar.style.width = `${Math.round(ratio * 100)}%`;
  };

  window.addEventListener("scroll", updateProgress, { passive: true });
  window.addEventListener("resize", updateProgress);
  updateProgress();

  navLinks.forEach((link, idx) => {
    link.style.animationDelay = `${Math.min(idx * 18, 360)}ms`;
  });
})();

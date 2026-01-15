document.addEventListener("DOMContentLoaded", () => {
    for (const wrap of document.getElementsByTagName("section")) {
        // Bind click evts
        const projWrap = wrap.nextElementSibling;
        let timeout;

        const toggleFocus = function() {
            // Toggle class
            const icon = wrap.children[2];
            if (!icon.className.includes("active")) {
                icon.classList.add("active");
                projWrap.classList.remove("hidden");
                projWrap.classList.add("animate-in");

                if (timeout) clearTimeout(timeout); // Trigger animation
                timeout = setTimeout(() => projWrap.classList.remove("animate-in"), 150);
            } else {
                icon.classList.remove("active");
                projWrap.classList.add("animate-out");

                if (timeout) clearTimeout(timeout); // Trigger animation
                timeout = setTimeout(() => {
                    projWrap.classList.remove("animate-out");
                    projWrap.classList.add("hidden");
                }, 120);
            }
        };

        wrap.addEventListener("click", e => (e.target === wrap || e.target === wrap.children[1] || e.target === wrap.children[2]) ? toggleFocus() : null);
        wrap.children[2].addEventListener("keyup", e => e.code === "Enter" && toggleFocus());
    }
});
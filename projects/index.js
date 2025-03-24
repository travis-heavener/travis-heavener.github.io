document.addEventListener("DOMContentLoaded", () => {
    [...document.getElementsByClassName("section-wrapper")].forEach(wrapper => {
        // Bind click evts
        const projectsWrapper = wrapper.nextElementSibling;
        let timeout = null;

        const toggleFocus = function() {
            // Toggle class
            const icon = this.children[2];
            if (!icon.className.includes("active")) {
                icon.classList.add("active");
                projectsWrapper.classList.remove("hidden"); // Focus projects row

                // Trigger animation
                if (timeout !== null)
                    clearTimeout(timeout);

                projectsWrapper.classList.add("animate-in");
                timeout = setTimeout(() => {
                    projectsWrapper.classList.remove("animate-in");
                    timeout = null;
                }, 150);
            } else {
                icon.classList.remove("active");
                
                // Trigger animation
                if (timeout !== null)
                    clearTimeout(timeout);
                
                projectsWrapper.classList.add("animate-out");
                timeout = setTimeout(() => {
                    projectsWrapper.classList.remove("animate-out");
                    projectsWrapper.classList.add("hidden"); // Hide projects row
                    timeout = null;
                }, 120); // Buffer to prevent clipping
            }
        };

        wrapper.addEventListener("click", toggleFocus);
        wrapper.children[2].addEventListener("keyup", (e) => (e.code === "Enter") ? toggleFocus.bind(wrapper)() : null);
    });
});
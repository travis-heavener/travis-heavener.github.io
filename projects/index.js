document.addEventListener("DOMContentLoaded", () => {
    [...document.getElementsByClassName("section-wrapper")].forEach((wrapper, i) => {
        // Hide projects row
        const projectsRow = wrapper.nextElementSibling;
        projectsRow.className = "projects-row hidden";

        // Bind click evts
        const ANIM_DURATION = 150; // In ms, duration of projects row animation
        let timeout = null;
        wrapper.addEventListener("click", function() {
            // Toggle class
            const icon = this.children[2];
            const isActive = !icon.className.includes("active");
            if (isActive) {
                icon.classList.add("active");
                projectsRow.classList.remove("hidden"); // Focus projects row

                // Trigger animation
                if (timeout !== null)
                    clearTimeout(timeout);

                projectsRow.classList.add("animate-in");
                timeout = setTimeout(() => {
                    projectsRow.classList.remove("animate-in");
                    timeout = null;
                }, ANIM_DURATION);
            } else {
                icon.classList.remove("active");
                
                // Trigger animation
                if (timeout !== null)
                    clearTimeout(timeout);
                
                projectsRow.classList.add("animate-out");
                timeout = setTimeout(() => {
                    projectsRow.classList.remove("animate-out");
                    projectsRow.classList.add("hidden"); // Hide projects row
                    timeout = null;
                }, ANIM_DURATION * 0.8); // Add buffer to prevent clipping
            }
        });

        // If first dropdown area, focus
        // if (i === 0) icon.click();
    });
});
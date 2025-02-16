document.addEventListener("DOMContentLoaded", () => {
    [...document.getElementsByClassName("section-wrapper")].forEach(wrapper => {
        // Bind click evts
        const projectsWrapper = wrapper.nextElementSibling;
        const ANIM_DURATION = 150; // In ms, duration of projects row animation
        let timeout = null;
        
        wrapper.addEventListener("click", function() {
            // Toggle class
            const icon = this.children[2];
            const isActive = !icon.className.includes("active");
            if (isActive) {
                icon.classList.add("active");
                projectsWrapper.classList.remove("hidden"); // Focus projects row

                // Trigger animation
                if (timeout !== null)
                    clearTimeout(timeout);

                projectsWrapper.classList.add("animate-in");
                timeout = setTimeout(() => {
                    projectsWrapper.classList.remove("animate-in");
                    timeout = null;
                }, ANIM_DURATION);
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
                }, ANIM_DURATION * 0.8); // Add buffer to prevent clipping
            }
        });
    });
});
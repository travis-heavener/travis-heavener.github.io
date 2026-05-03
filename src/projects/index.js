// Reopen whatever projects are in the hash
const refocusHash = () => {
    const btn = (location.hash == "") ? document.getElementById("featured")
        : document.getElementById(location.hash.substring(1));
    if (btn && btn.getAttribute("aria-expanded") === "false")
        btn.click();
};

// Bind event listeners
document.addEventListener("DOMContentLoaded", () => {
    for (const wrap of document.getElementsByTagName("section")) {
        // Bind click evts
        const projWrap = wrap.nextElementSibling;
        const btn = wrap.querySelector("button");
        let timeout = null;

        const toggleFocus = () => {
            // Skip if already animating
            if (timeout !== null) return;

            // Toggle class
            const icon = btn.lastElementChild;
            if (btn.getAttribute("aria-expanded") !== "true") {
                projWrap.classList.add("animate-in");
                btn.setAttribute("aria-expanded", "true");
                projWrap.hidden = false;

                // Trigger animation
                timeout = setTimeout(() => {
                    projWrap.classList.remove("animate-in");
                    projWrap.classList.add("active");

                    // Resize animation canvas
                    if (window.updateDims) window.updateDims();

                    timeout = null;
                }, 150);
            } else {
                projWrap.classList.remove("active");
                projWrap.classList.add("animate-out");
                btn.setAttribute("aria-expanded", "false");
                projWrap.hidden = true;

                // Trigger animation
                timeout = setTimeout(() => {
                    projWrap.classList.remove("animate-out");

                    // Resize animation canvas
                    if (window.updateDims) window.updateDims();

                    timeout = null;
                }, 120);
            }
        };

        // Bind event listeners
        btn.addEventListener("click", e => toggleFocus());
    }

    // Focus Featured content if nothing else is focused
    refocusHash();

    // Bind project open to hash change
    window.addEventListener("hashchange", () => refocusHash());
});

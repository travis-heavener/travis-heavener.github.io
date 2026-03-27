// If JS is enabled, remove location.hash when clicking on dropdown
// to allow it to be minimized (since :target pseudo-class is stubborn)
const catchHashChange = () => {
    // Clear hash when toggling checkbox
    if (location.hash) {
        const checkbox = document.getElementById(location.hash.substring(1)).parentElement.parentElement.nextSibling;
        checkbox.addEventListener("change", () => {
            // Force close the checkbox content & remove hash
            checkbox.checked = false;
            location.hash = "";
        }, { "once": true });
    }
};

// Bind event listeners
window.addEventListener("hashchange", catchHashChange);
document.addEventListener("DOMContentLoaded", catchHashChange);

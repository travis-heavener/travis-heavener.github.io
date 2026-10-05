// Flags JS support (for no-JS fallbacks) and grows the timeline bars once they scroll into view.
document.documentElement.classList.add("js");

document.addEventListener("DOMContentLoaded", () => {
    const timeline = document.querySelector("#activities-honors .timeline");
    if (!timeline) return;

    if (!("IntersectionObserver" in window)) return timeline.classList.add("in");

    const io = new IntersectionObserver(([entry]) => {
        if (!entry.isIntersecting) return;
        timeline.classList.add("in");
        io.disconnect();
    }, { threshold: 0.3 });
    io.observe(timeline);
});

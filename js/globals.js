document.addEventListener("DOMContentLoaded", () => {
    [...document.getElementsByTagName("a")].forEach(a => {
        // Ignore crossorigin prefetches
        if (!a.href.startsWith(location.origin)) return;

        // Prefetch links on hover
        let timeout = null;
        const offHandler = () => (timeout !== null) ? clearTimeout(timeout) : null;
        const onHandler = () => {
            timeout = setTimeout(() => {
                document.head.insertAdjacentHTML("beforeend", `<link rel="prefetch" href="${a.href}">`);

                // Unbind
                a.removeEventListener("mouseenter", onHandler);
                a.removeEventListener("mouseleave", offHandler);
                timeout = null;
            }, 100); 
        };

        // Bind events
        a.addEventListener("mouseenter", onHandler);
        a.addEventListener("mouseleave", offHandler);
    });
});
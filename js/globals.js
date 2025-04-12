document.addEventListener("DOMContentLoaded", () => {
    const prefetched = new Set();
    for (const a of document.getElementsByTagName("a")) {
        // Ignore crossorigin prefetches
        if (!a.href.startsWith(location.origin)) return;

        // Prefetch links on hover
        let timeout;
        const offHandler = () => clearTimeout(timeout);
        const onHandler = () => {
            timeout = setTimeout(() => {
                if (!prefetched.has(a.href)) {
                    const link = document.createElement("LINK");
                    link.rel = "prefetch";
                    link.href = a.href;
                    document.head.appendChild(link);
                    prefetched.add(a.href);
                }

                a.removeEventListener("mouseenter", onHandler);
                a.removeEventListener("mouseleave", offHandler);
            }, 100); 
        };

        // Bind events
        a.addEventListener("mouseenter", onHandler);
        a.addEventListener("mouseleave", offHandler);
    }
});
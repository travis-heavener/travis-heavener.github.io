document.addEventListener("DOMContentLoaded", () => {
    // Update aria-current in header nav
    document.querySelectorAll("nav a").forEach(link => {
        if (link.href === window.location.href)
            link.setAttribute("aria-current", "page");
    });

    // Prefetch internal links
    const prefetched = new Set();
    for (const a of document.getElementsByTagName("a")) {
        // Ignore crossorigin prefetches
        if (!a.href.startsWith(location.origin)) continue;

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

    // Trigger background animation
    startBackgroundAnimation();
});

// Starts the background canvas animation
const startBackgroundAnimation = () => {
    // Check for reduced motion
    const query = window.matchMedia("(prefers-reduced-motion: reduce)");
    if (query.matches) return;

    // Add background canvas
    const main = document.getElementById("main-content");
    const canvas = document.createElement("CANVAS");
    const ctx = canvas.getContext("2d");
    canvas.id = "background-canvas";
    main.insertBefore(canvas, main.firstElementChild);

    // Animation resetter
    const MAX_DIST = 120;
    let particles;
    let nextFrameID = null;
    const resetAnimation = () => {
        if (nextFrameID !== null) {
            cancelAnimationFrame(nextFrameID);
            nextFrameID = null;
        }

        // Reset particles
        const NUM_PARTICLES = Math.round(120 * window.innerHeight / 1080);
        particles = Array.from({ length: NUM_PARTICLES }, () => ({
            x: Math.random() * canvas.clientWidth,
            y: Math.random() * canvas.clientHeight,
            vx: (Math.random() - 0.5) * 0.3,
            vy: (Math.random() - 0.5) * 0.3
        }));

        // Start animation
        animate();
    };

    // Animation handler
    const animate = () => {
        // Clear canvas
        ctx.clearRect(0, 0, canvas.clientWidth, canvas.clientHeight);

        // Move particles
        for (let p of particles) {
            p.x += p.vx, p.y += p.vy;

            // Wrap edges
            if (p.x < 0) p.x += canvas.clientWidth;
            if (p.x > canvas.clientWidth) p.x -= canvas.clientWidth;
            if (p.y < 0) p.y += canvas.clientHeight;
            if (p.y > canvas.clientHeight) p.y -= canvas.clientHeight;
        }

        // Draw connections
        ctx.lineWidth = 1;
        for (let i = 0; i < particles.length; i++) {
            for (let j = i + 1; j < particles.length; j++) {
                const dx = particles[i].x - particles[j].x;
                const dy = particles[i].y - particles[j].y;
                const dist = Math.hypot(dx, dy);

                if (dist < MAX_DIST) {
                    const alpha = 1 - dist / MAX_DIST;
                    ctx.strokeStyle = `rgba(180, 180, 200, ${alpha * 0.15})`;
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(particles[j].x, particles[j].y);
                    ctx.stroke();
                }
            }
        }

        // Draw particles
        for (let p of particles) {
            ctx.fillStyle = "#c8c8dc40";
            ctx.beginPath();
            ctx.arc(p.x, p.y, 1.2, 0, Math.PI * 2);
            ctx.fill();
        }

        // Request next frame
        nextFrameID = requestAnimationFrame(animate);
    };

    // Update width/height on dimension change
    const updateDims = () => {
        // Force drawing in CSS pixels
        const dpr = window.devicePixelRatio || 1;
        canvas.width = canvas.clientWidth * dpr;
        canvas.height = canvas.clientHeight * dpr;
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

        // Restart animation
        resetAnimation();
    };
    window.addEventListener("resize", updateDims);

    // Start animation by updating dimensions
    updateDims();
};
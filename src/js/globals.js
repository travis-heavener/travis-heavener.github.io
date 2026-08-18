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
    // Add background canvas
    const main = document.getElementById("main-content");
    const wrapper = document.createElement("DIV");
    wrapper.id = "background-canvas-wrapper";
    main.insertBefore(wrapper, main.firstElementChild);

    const canvas = document.createElement("CANVAS");
    const ctx = canvas.getContext("2d");
    canvas.id = "background-canvas";
    wrapper.appendChild(canvas);

    // Update width/height on dimension change
    window.updateDims = () => {
        const dpr = window.devicePixelRatio || 1;
        // Use window inner dimensions instead of wrapper's scroll height
        canvas.width = window.innerWidth * dpr;
        canvas.height = window.innerHeight * dpr;
        canvas.style.width = window.innerWidth + "px";
        canvas.style.height = window.innerHeight + "px";
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    };
    window.updateDims();
    window.addEventListener("resize", window.updateDims);

    // Particle setup (produces ~100 particles on a 1920x1080 screen)
    const NUM_PARTICLES = Math.round((window.innerWidth * window.innerHeight) / 14576);
    const MAX_DIST = 120;

    const particles = Array.from({ length: NUM_PARTICLES }, () => ({
        x: Math.random() * window.innerWidth,
        y: Math.random() * window.innerHeight,
        vx: (Math.random() - 0.5) * 0.3,
        vy: (Math.random() - 0.5) * 0.3
    }));

    // Animation handler
    const animate = () => {
        // Clear canvas
        ctx.clearRect(0, 0, window.innerWidth, window.innerHeight);

        // Move particles
        for (let p of particles) {
            p.x += p.vx;
            p.y += p.vy;

            // Wrap edges
            if (p.x < 0) p.x += window.innerWidth;
            if (p.x > window.innerWidth) p.x -= window.innerWidth;
            if (p.y < 0) p.y += window.innerHeight;
            if (p.y > window.innerHeight) p.y -= window.innerHeight;
        }

        // Draw connections
        ctx.lineWidth = 1;
        for (let i = 0; i < particles.length; i++) {
            for (let j = i + 1; j < particles.length; j++) {
                const dx = particles[i].x - particles[j].x;
                const dy = particles[i].y - particles[j].y;
                const dist = Math.sqrt(dx * dx + dy * dy);

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
        requestAnimationFrame(animate);
    };

    // Start
    animate();
};
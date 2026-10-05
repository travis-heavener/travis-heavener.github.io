// Filters the project tiles by category or "featured". Without JS the page
// simply shows every group (the filter bar stays hidden).
(() => {
    const bar = document.getElementById("filters");
    if (!bar) return;

    const buttons = [...bar.querySelectorAll("button")];
    const groups = [...document.querySelectorAll(".group")];
    const status = document.getElementById("project-status");
    const valid = new Set(buttons.map(b => b.dataset.filter));

    // Old hash links (#infrastructure, #simulation-ai, #tools) still land somewhere sensible
    const ALIASES = { infrastructure: "web", "simulation-ai": "simulation", tools: "systems" };

    const fromHash = () => {
        const h = location.hash.slice(1);
        const f = ALIASES[h] ?? h;
        return valid.has(f) ? f : "all";
    };

    const apply = filter => {
        let shown = 0;

        for (const group of groups) {
            let any = false;
            for (const item of group.querySelectorAll(".project")) {
                const match = filter === "all"
                    || (filter === "featured" ? item.hasAttribute("data-featured") : group.id === filter);
                item.hidden = !match;
                if (match) { any = true; shown++; }
            }
            group.hidden = !any;
        }

        for (const b of buttons)
            b.setAttribute("aria-pressed", String(b.dataset.filter === filter));

        status.textContent = `Showing ${shown} project${shown === 1 ? "" : "s"}.`;
    };

    bar.addEventListener("click", e => {
        const btn = e.target.closest("button");
        if (!btn) return;
        const filter = btn.dataset.filter;
        apply(filter);
        // replaceState (not location.hash) so filtering doesn't jump-scroll or flood history
        history.replaceState(null, "", filter === "all" ? location.pathname : `#${filter}`);
    });

    window.addEventListener("hashchange", () => apply(fromHash()));

    bar.hidden = false;
    apply(fromHash());
})();

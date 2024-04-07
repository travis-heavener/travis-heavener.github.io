$("body").ready(() => {
    // bind events to social icons
    $("#contact-github-img").click(
        () => window.open("https://github.com/travis-heavener/", "_blank")
    );

    $("#contact-linkedin-img").click(
        () => window.open("https://www.linkedin.com/in/travis-heavener/", "_blank")
    );

    $("#contact-mail-img").click(
        () => window.open("mailto:travis.heavener@gmail.com", "_blank")
    );

    // bind scroll events
    $(document).on("scroll", () => {
        $("#scroll-top-btn").css("display", $(document).scrollTop() ? "flex" : "");
    });
    
    // UNUSED: locks scroll to top unless browser scroll event has ended
    // (fixes weird skipping when scroll to top)
    // let isScrolling = false;
    // $(document).on("scroll", () => isScrolling = true);
    // $(document).on("scrollend", () => isScrolling = false);
    $("#scroll-top-btn").click(() => {
        // if (!isScrolling)
        window.scrollTo({"top": 0, "left": 0, "behavior": "smooth"});
    });
});
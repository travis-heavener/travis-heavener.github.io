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
});
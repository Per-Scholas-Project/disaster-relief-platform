document.addEventListener("DOMContentLoaded", () => {
    fetch("./components/header.html")
        .then(res => res.text())
        .then(data => {
            document.getElementById("site-header").innerHTML = data;

            // Setup menu toggle functionality
            const toggleButton = document.querySelector(".header__toggle");
            const navList = document.querySelector(".header__nav-list");

            if (toggleButton && navList) {
                toggleButton.addEventListener("click", () => {
                    navList.classList.toggle("header__nav-list--visible");
                });
            }
        })
        .catch(err => console.error("Failed to load header:", err));
});

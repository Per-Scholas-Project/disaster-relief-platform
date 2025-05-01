document.addEventListener("DOMContentLoaded", () => {
    // Mobile menu toggle
    const toggleButton = document.querySelector(".header__toggle");
    const navList = document.querySelector(".header__nav-list");

    if (toggleButton && navList) {
        toggleButton.addEventListener("click", () => {
            navList.classList.toggle("header__nav-list--visible");
        });
    }

    // Anchor link scroll adjustment for sticky header
    const header = document.getElementById("site-header");
    const headerHeight = header ? header.offsetHeight : 0;

    const links = document.querySelectorAll('a[href^="#"]');

    links.forEach(link => {
        link.addEventListener("click", function (e) {
            const targetId = this.getAttribute("href").substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                e.preventDefault();
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.scrollY - headerHeight;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: "smooth"
                });

                // --- NEW PART: Close the mobile menu when a link is clicked ---
                if (navList.classList.contains("header__nav-list--visible")) {
                    navList.classList.remove("header__nav-list--visible");
                }
            }
        });
    });

    // Hide and show header on scroll
    let lastScrollY = window.scrollY;
    let isScrolling;

    window.addEventListener("scroll", () => {
        clearTimeout(isScrolling);

        if (window.scrollY <= 0) {
            header.style.transform = "translateY(0)";
        } else if (window.scrollY > lastScrollY) {
            header.style.transform = "translateY(-100%)";
        } else {
            header.style.transform = "translateY(0)";
        }

        lastScrollY = window.scrollY;

        isScrolling = setTimeout(() => {
            if (window.scrollY > 0) {
                header.style.transform = "translateY(-100%)";
            }
        }, 1500);
    });
});

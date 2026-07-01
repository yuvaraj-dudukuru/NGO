// Day 5 JavaScript: toggle the mobile menu open/closed.
const hamburger = document.getElementById("hamburger");
const navLinks = document.getElementById("navLinks");

hamburger.addEventListener("click", () => {
    const isOpen = navLinks.classList.toggle("open");  // show/hide the menu
    hamburger.classList.toggle("active");              // morph icon into an X
    hamburger.setAttribute("aria-expanded", isOpen);   // accessibility state
});

// Close the menu after clicking a link (nice on mobile)
navLinks.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
        navLinks.classList.remove("open");
        hamburger.classList.remove("active");
        hamburger.setAttribute("aria-expanded", "false");
    });
});

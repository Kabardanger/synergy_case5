const fontButtons = document.querySelectorAll(".font-button");
const currentFontName = document.getElementById("current-font-name");

const fontClasses = [
    "font-brand",
    "font-inter",
    "font-roboto",
    "font-open-sans",
    "font-montserrat",
    "font-pt-sans",
];

fontButtons.forEach((button) => {
    button.addEventListener("click", () => {
        document.body.classList.remove(...fontClasses);
        document.body.classList.add(`font-${button.dataset.font}`);

        fontButtons.forEach((item) => item.classList.remove("active"));
        button.classList.add("active");
        currentFontName.textContent = button.textContent;
    });
});

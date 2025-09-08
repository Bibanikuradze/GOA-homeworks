function greet() {
    const paragraph = document.getElementById("myParagraph");
    paragraph.textContent = "Welcome biba!";
}

document.addEventListener("DOMContentLoaded", function () {
    const paragraph = document.getElementById("myParagraph");
    paragraph.addEventListener("click", greet);
});
function modifyDiv() {
    const div = document.getElementById("myDiv");

    const button = document.getElementById("myButton");
    if (button) {
        div.removeChild(button);
    }

    const paragraph = document.getElementById("myParagraph");
    if (paragraph) {
        const italic = document.createElement("i");
        italic.textContent = "ეს არის ახალი ტექსტი i თეგში.";
        paragraph.replaceWith(italic);
    }
}

window.addEventListener("DOMContentLoaded", modifyDiv);
function addNewElement() {
    var div = document.getElementById("myDiv");

    var button = document.createElement("button");

    button.textContent = "click here";

    div.appendChild(button);
}

addNewElement();
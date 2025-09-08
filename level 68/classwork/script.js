function compareNums() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const resultElement = document.getElementById('result');

    if (num1 > num2) {
        resultElement.textContent = num1;
    } else if (num2 > num1) {
        resultElement.textContent = num2;
    } else {
        resultElement.textContent = "Numbers are equal";
    }
}
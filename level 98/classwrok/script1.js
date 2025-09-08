const numbers = [10, 25, 7, 42, 18];

function displayArrayWithIndex() {
    let resultHTML = '<h4>Array Elements with Index:</h4>';
    resultHTML += '<div class="code">const numbers = [10, 25, 7, 42, 18];</div>';
    resultHTML += '<h5>Using for loop:</h5>';
    
    for (let i = 0; i < numbers.length; i++) {
        const output = `Index: ${i}, Value: ${numbers[i]}`;
        resultHTML += `<div class="array-item">${output}</div>`;
        console.log(output);
    }
    
    document.getElementById('arrayResult').innerHTML = resultHTML;
}

function displayWithForEach() {
    let resultHTML = '<h5>Using forEach method:</h5>';
    
    numbers.forEach((value, index) => {
        const output = `Index: ${index}, Value: ${value}`;
        resultHTML += `<div class="array-item">${output}</div>`;
        console.log(output);
    });
    
    return resultHTML;
}

function displayWithForOf() {
    let resultHTML = '<h5>Using for...of with entries:</h5>';
    
    for (let [index, value] of numbers.entries()) {
        const output = `Index: ${index}, Value: ${value}`;
        resultHTML += `<div class="array-item">${output}</div>`;
        console.log(output);
    };
    
    return resultHTML;
}

function displayWithDifferentMethods() {
    let resultHTML = '<h4>Different Methods to Display Array Elements:</h4>';
    resultHTML += '<div class="code">const numbers = [10, 25, 7, 42, 18];</div>';
    
    resultHTML += displayWithForEach();
    resultHTML += displayWithForOf();
    
    document.getElementById('arrayResult').innerHTML = resultHTML;
}

function displayCustomArray() {
    const input = document.getElementById('customArray').value;
    const customNumbers = input.split(',').map(num => parseFloat(num.trim()));
    
    if (customNumbers.length !== 5 || customNumbers.some(isNaN)) {
        document.getElementById('customResult').innerHTML = `
            <div style="background-color: #f8d7da; color: #721c24; padding: 10px; border-radius: 5px;">
                <strong>Error:</strong> Please enter exactly 5 valid numbers separated by commas.
            </div>
        `;
        return;
    }
    
    let resultHTML = '<h4>Custom Array Elements:</h4>';
    resultHTML += `<div class="code">const customNumbers = [${customNumbers.join(', ')}];</div>`;
    
    for (let i = 0; i < customNumbers.length; i++) {
        const output = `Index: ${i}, Value: ${customNumbers[i]}`;
        resultHTML += `<div class="array-item">${output}</div>`;
        console.log(output);
    }
    
    document.getElementById('customResult').innerHTML = resultHTML;
}

// Function to convert all strings in an array to uppercase
function convertStringsToUppercase() {
    const strings = ['hello', 'world', 'javascript', 'programming', 'array'];
    
    let resultHTML = '<h4>Convert Strings to Uppercase:</h4>';
    resultHTML += '<div class="code">const strings = ["hello", "world", "javascript", "programming", "array"];</div>';
    
    // Method 1: Using map() method
    resultHTML += '<h5>Method 1: Using map() method</h5>';
    const uppercaseStrings = strings.map(str => str.toUpperCase());
    resultHTML += `<div class="code">const uppercaseStrings = strings.map(str => str.toUpperCase());</div>`;
    resultHTML += `<div class="code">Result: [${uppercaseStrings.map(str => `"${str}"`).join(', ')}]</div>`;
    
    // Method 2: Using for loop
    resultHTML += '<h5>Method 2: Using for loop</h5>';
    const uppercaseStrings2 = [];
    for (let i = 0; i < strings.length; i++) {
        uppercaseStrings2.push(strings[i].toUpperCase());
    }
    resultHTML += `<div class="code">for (let i = 0; i < strings.length; i++) {<br>
        &nbsp;&nbsp;&nbsp;&nbsp;uppercaseStrings2.push(strings[i].toUpperCase());<br>
    }</div>`;
    resultHTML += `<div class="code">Result: [${uppercaseStrings2.map(str => `"${str}"`).join(', ')}]</div>`;
    
    // Method 3: Using forEach
    resultHTML += '<h5>Method 3: Using forEach</h5>';
    const uppercaseStrings3 = [];
    strings.forEach(str => {
        uppercaseStrings3.push(str.toUpperCase());
    });
    resultHTML += `<div class="code">strings.forEach(str => {<br>
        &nbsp;&nbsp;&nbsp;&nbsp;uppercaseStrings3.push(str.toUpperCase());<br>
    });</div>`;
    resultHTML += `<div class="code">Result: [${uppercaseStrings3.map(str => `"${str}"`).join(', ')}]</div>`;
    
    // Method 4: Using for...of loop
    resultHTML += '<h5>Method 4: Using for...of loop</h5>';
    const uppercaseStrings4 = [];
    for (let str of strings) {
        uppercaseStrings4.push(str.toUpperCase());
    }
    resultHTML += `<div class="code">for (let str of strings) {<br>
        &nbsp;&nbsp;&nbsp;&nbsp;uppercaseStrings4.push(str.toUpperCase());<br>
    }</div>`;
    resultHTML += `<div class="code">Result: [${uppercaseStrings4.map(str => `"${str}"`).join(', ')}]</div>`;
    
    // Display original and converted arrays
    resultHTML += '<h5>Comparison:</h5>';
    resultHTML += `<div class="array-item"><strong>Original:</strong> [${strings.map(str => `"${str}"`).join(', ')}]</div>`;
    resultHTML += `<div class="array-item"><strong>Uppercase:</strong> [${uppercaseStrings.map(str => `"${str}"`).join(', ')}]</div>`;
    
    // Console output
    console.log('Original strings:', strings);
    console.log('Uppercase strings:', uppercaseStrings);
    
    return resultHTML;
}

// Function to handle custom string array input
function convertCustomStringsToUppercase() {
    const input = document.getElementById('customStringArray').value;
    const customStrings = input.split(',').map(str => str.trim());
    
    if (customStrings.length === 0 || customStrings.some(str => str === '')) {
        document.getElementById('customStringResult').innerHTML = `
            <div style="background-color: #f8d7da; color: #721c24; padding: 10px; border-radius: 5px;">
                <strong>Error:</strong> Please enter valid strings separated by commas.
            </div>
        `;
        return;
    }
    
    let resultHTML = '<h4>Custom String Array to Uppercase:</h4>';
    resultHTML += `<div class="code">const customStrings = [${customStrings.map(str => `"${str}"`).join(', ')}];</div>`;
    
    const uppercaseCustomStrings = customStrings.map(str => str.toUpperCase());
    resultHTML += `<div class="code">const uppercaseCustomStrings = customStrings.map(str => str.toUpperCase());</div>`;
    
    resultHTML += '<h5>Results:</h5>';
    resultHTML += `<div class="array-item"><strong>Original:</strong> [${customStrings.map(str => `"${str}"`).join(', ')}]</div>`;
    resultHTML += `<div class="array-item"><strong>Uppercase:</strong> [${uppercaseCustomStrings.map(str => `"${str}"`).join(', ')}]</div>`;
    
    // Console output
    console.log('Custom original strings:', customStrings);
    console.log('Custom uppercase strings:', uppercaseCustomStrings);
    
    document.getElementById('customStringResult').innerHTML = resultHTML;
}

document.addEventListener('DOMContentLoaded', function() {
    console.log('Array Index Display loaded successfully!');
    console.log('Available functions:');
    console.log('- displayArrayWithIndex(): Display array with for loop');
    console.log('- displayWithDifferentMethods(): Show different iteration methods');
    console.log('- displayCustomArray(): Display custom user input array');
    console.log('- convertStringsToUppercase(): Convert strings to uppercase');
    console.log('- convertCustomStringsToUppercase(): Convert custom strings to uppercase');
    
    displayArrayWithIndex();
});

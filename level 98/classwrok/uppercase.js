function showUppercaseConversion() {
    const strings = ['hello', 'world', 'javascript', 'programming', 'array'];
    const uppercaseStrings = strings.map(str => str.toUpperCase());
    
    let resultHTML = '<h4>Convert Strings to Uppercase:</h4>';
    resultHTML += '<div class="code">const strings = ["hello", "world", "javascript", "programming", "array"];</div>';
    resultHTML += '<div class="code">const uppercaseStrings = strings.map(str => str.toUpperCase());</div>';
    resultHTML += '<div class="comparison">';
    resultHTML += `<div class="original"><strong>Original:</strong><br>[${strings.map(str => `"${str}"`).join(', ')}]</div>`;
    resultHTML += `<div class="converted"><strong>Uppercase:</strong><br>[${uppercaseStrings.map(str => `"${str}"`).join(', ')}]</div>`;
    resultHTML += '</div>';
    
    console.log('Original:', strings);
    console.log('Uppercase:', uppercaseStrings);
    
    document.getElementById('uppercaseResult').innerHTML = resultHTML;
}

function convertCustomStringsToUppercase() {
    const input = document.getElementById('customStringArray').value;
    const customStrings = input.split(',').map(str => str.trim()).filter(str => str !== '');
    
    if (customStrings.length === 0) {
        document.getElementById('customStringResult').innerHTML = '<div style="color: red;">Error: Please enter valid strings.</div>';
        return;
    }
    
    const uppercaseStrings = customStrings.map(str => str.toUpperCase());
    
    let resultHTML = '<h4>Custom String Array to Uppercase:</h4>';
    resultHTML += `<div class="code">const customStrings = [${customStrings.map(str => `"${str}"`).join(', ')}];</div>`;
    resultHTML += '<div class="code">const uppercaseStrings = customStrings.map(str => str.toUpperCase());</div>';
    resultHTML += '<div class="comparison">';
    resultHTML += `<div class="original"><strong>Original:</strong><br>[${customStrings.map(str => `"${str}"`).join(', ')}]</div>`;
    resultHTML += `<div class="converted"><strong>Uppercase:</strong><br>[${uppercaseStrings.map(str => `"${str}"`).join(', ')}]</div>`;
    resultHTML += '</div>';
    
    console.log('Custom original:', customStrings);
    console.log('Custom uppercase:', uppercaseStrings);
    
    document.getElementById('customStringResult').innerHTML = resultHTML;
}

function showExample1() {
    const strings = ['python', 'javascript', 'java', 'c++', 'ruby'];
    const uppercaseStrings = strings.map(str => str.toUpperCase());
    
    let resultHTML = '<h4>Example: Programming Languages</h4>';
    resultHTML += `<div class="code">const strings = [${strings.map(str => `"${str}"`).join(', ')}];</div>`;
    resultHTML += '<div class="code">const uppercaseStrings = strings.map(str => str.toUpperCase());</div>';
    resultHTML += '<div class="comparison">';
    resultHTML += `<div class="original"><strong>Original:</strong><br>[${strings.map(str => `"${str}"`).join(', ')}]</div>`;
    resultHTML += `<div class="converted"><strong>Uppercase:</strong><br>[${uppercaseStrings.map(str => `"${str}"`).join(', ')}]</div>`;
    resultHTML += '</div>';
    
    console.log('Example original:', strings);
    console.log('Example uppercase:', uppercaseStrings);
    
    document.getElementById('exampleResult').innerHTML = resultHTML;
}

function showExample2() {
    const strings = ['georgia', 'france', 'germany', 'japan', 'brazil'];
    const uppercaseStrings = strings.map(str => str.toUpperCase());
    
    let resultHTML = '<h4>Example: Countries</h4>';
    resultHTML += `<div class="code">const strings = [${strings.map(str => `"${str}"`).join(', ')}];</div>`;
    resultHTML += '<div class="code">const uppercaseStrings = strings.map(str => str.toUpperCase());</div>';
    resultHTML += '<div class="comparison">';
    resultHTML += `<div class="original"><strong>Original:</strong><br>[${strings.map(str => `"${str}"`).join(', ')}]</div>`;
    resultHTML += `<div class="converted"><strong>Uppercase:</strong><br>[${uppercaseStrings.map(str => `"${str}"`).join(', ')}]</div>`;
    resultHTML += '</div>';
    
    document.getElementById('exampleResult').innerHTML = resultHTML;
}

function showExample3() {
    const strings = ['red', 'blue', 'green', 'yellow', 'purple'];
    const uppercaseStrings = strings.map(str => str.toUpperCase());
    
    let resultHTML = '<h4>Example: Colors</h4>';
    resultHTML += `<div class="code">const strings = [${strings.map(str => `"${str}"`).join(', ')}];</div>`;
    resultHTML += '<div class="code">const uppercaseStrings = strings.map(str => str.toUpperCase());</div>';
    resultHTML += '<div class="comparison">';
    resultHTML += `<div class="original"><strong>Original:</strong><br>[${strings.map(str => `"${str}"`).join(', ')}]</div>`;
    resultHTML += `<div class="converted"><strong>Uppercase:</strong><br>[${uppercaseStrings.map(str => `"${str}"`).join(', ')}]</div>`;
    resultHTML += '</div>';
    
    document.getElementById('exampleResult').innerHTML = resultHTML;
}

document.addEventListener('DOMContentLoaded', function() {
    console.log('String Uppercase Conversion loaded!');
});

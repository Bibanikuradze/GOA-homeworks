function findOccurrences() {
    const str = "banana";
    const searchChar = "a";
    
    const firstIndex = str.indexOf(searchChar);
    
    const secondIndex = str.indexOf(searchChar, firstIndex + 1);
    
    document.getElementById('firstA').textContent = firstIndex;
    document.getElementById('secondA').textContent = secondIndex;
    
    console.log(`String: "${str}"`);
    console.log(`First occurrence of "${searchChar}": ${firstIndex}`);
    console.log(`Second occurrence of "${searchChar}": ${secondIndex}`);
}

function checkWorld() {
    const str = "Hello world";
    const substring = "world";
    
    const index = str.indexOf(substring);
    const exists = index !== -1;
    
    if (exists) {
        document.getElementById('worldCheck').textContent = `"${substring}" found at index ${index}`;
    } else {
        document.getElementById('worldCheck').textContent = `"${substring}" not found`;
    }
    
    console.log(`String: "${str}"`);
    console.log(`Substring: "${substring}"`);
    console.log(`Result: ${exists ? `Found at index ${index}` : 'Not found'}`);
}

function runAll() {
    findOccurrences();
    checkWorld();
    
    const allResultsDiv = document.getElementById('allResults');
    allResultsDiv.innerHTML = `
        <div style="margin-top: 20px; padding: 15px; background-color: #d4edda; border-radius: 5px; border-left: 4px solid #28a745;">
            <h4>Summary of Results:</h4>
            <p><strong>Task 1:</strong> In "banana", first "a" is at index ${document.getElementById('firstA').textContent}, second "a" is at index ${document.getElementById('secondA').textContent}</p>
            <p><strong>Task 2:</strong> ${document.getElementById('worldCheck').textContent}</p>
        </div>
    `;
}

document.addEventListener('DOMContentLoaded', function() {
    console.log('String Operations Demo loaded successfully!');
    console.log('Use the buttons to run the string operations.');
});

function demonstrateStringMethods() {
    const str = "banana";
    const worldStr = "Hello world";
    
    console.log('\n=== String Method Demonstrations ===');
    console.log(`Original string: "${str}"`);
    console.log(`Length: ${str.length}`);
    console.log(`Character at index 1: "${str.charAt(1)}"`);
    console.log(`Character at index 1 (bracket notation): "${str[1]}"`);
    
    console.log(`\nWorld string: "${worldStr}"`);
    console.log(`Uppercase: "${worldStr.toUpperCase()}"`);
    console.log(`Lowercase: "${worldStr.toLowerCase()}"`);
    console.log(`Replace "world" with "JavaScript": "${worldStr.replace("world", "JavaScript")}"`);
}

if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        findOccurrences,
        checkWorld,
        runAll,
        demonstrateStringMethods
    };
}
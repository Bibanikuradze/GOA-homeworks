function findOccurrences() {
    const str = "banana";
    const searchChar = "a";
    
    console.log("=== Task 1: Finding 'a' in 'banana' ===");
    console.log(`String: "${str}"`);
    console.log(`Searching for: "${searchChar}"`);
    
    const firstIndex = str.indexOf(searchChar);
    console.log(`First occurrence of "${searchChar}": ${firstIndex}`);
    
    const secondIndex = str.indexOf(searchChar, firstIndex + 1);
    console.log(`Second occurrence of "${searchChar}": ${secondIndex}`);
    
    document.getElementById('firstA').textContent = firstIndex;
    document.getElementById('secondA').textContent = secondIndex;
    
    document.getElementById('firstA').style.backgroundColor = '#d4edda';
    document.getElementById('secondA').style.backgroundColor = '#d4edda';
    
    return { first: firstIndex, second: secondIndex };
}

function checkWorld() {
    const str = "Hello world";
    const substring = "world";
    
    console.log("\n=== Task 2: Checking 'world' in 'Hello world' ===");
    console.log(`String: "${str}"`);
    console.log(`Substring: "${substring}"`);
    
    const index = str.indexOf(substring);
    const exists = index !== -1;
    
    console.log(`indexOf result: ${index}`);
    console.log(`Substring exists: ${exists}`);
    
    if (exists) {
        document.getElementById('worldCheck').textContent = `"${substring}" found at index ${index}`;
        document.getElementById('worldCheck').style.backgroundColor = '#d4edda';
    } else {
        document.getElementById('worldCheck').textContent = `"${substring}" not found (indexOf returned -1)`;
        document.getElementById('worldCheck').style.backgroundColor = '#f8d7da';
    }
    
    return { exists, index };
}

function runAll() {
    console.log("🚀 Running all string operations...\n");
    
    const task1Result = findOccurrences();
    const task2Result = checkWorld();
    
    const allResultsDiv = document.getElementById('allResults');
    allResultsDiv.innerHTML = `
        <div style="margin-top: 20px; padding: 20px; background-color: #e8f5e8; border-radius: 8px; border-left: 5px solid #27ae60;">
            <h4>📊 Summary of Results:</h4>
            <div style="background-color: white; padding: 15px; border-radius: 5px; margin: 10px 0;">
                <p><strong>Task 1 - "banana":</strong></p>
                <ul>
                    <li>First "a" found at index: <span style="color: #e74c3c; font-weight: bold;">${task1Result.first}</span></li>
                    <li>Second "a" found at index: <span style="color: #e74c3c; font-weight: bold;">${task2Result.second}</span></li>
                </ul>
            </div>
            <div style="background-color: white; padding: 15px; border-radius: 5px; margin: 10px 0;">
                <p><strong>Task 2 - "Hello world":</strong></p>
                <ul>
                    <li>Substring "world": <span style="color: #27ae60; font-weight: bold;">${task2Result.exists ? 'Found' : 'Not found'}</span></li>
                    <li>Index position: <span style="color: #e74c3c; font-weight: bold;">${task2Result.index}</span></li>
                </ul>
            </div>
        </div>
    `;
    
    console.log("\n✅ All operations completed successfully!");
}

function demonstrateStringMethods() {
    console.log("\n=== Additional String Method Demonstrations ===");
    
    const str = "banana";
    const worldStr = "Hello world";
    
    console.log(`Original string: "${str}"`);
    console.log(`String length: ${str.length}`);
    console.log(`Character at index 1: "${str.charAt(1)}"`);
    console.log(`Character at index 1 (bracket notation): "${str[1]}"`);
    
    console.log(`\nWorld string: "${worldStr}"`);
    console.log(`Uppercase: "${worldStr.toUpperCase()}"`);
    console.log(`Lowercase: "${worldStr.toLowerCase()}"`);
    console.log(`Replace "world" with "JavaScript": "${worldStr.replace("world", "JavaScript")}"`);
}

function showStepByStep() {
    console.log("\n=== Step-by-Step Process ===");
    
    console.log("Task 1: Finding 'a' in 'banana'");
    const str = "banana";
    console.log(`1. Start with string: "${str}"`);
    console.log(`2. Use str.indexOf("a"): ${str.indexOf("a")}`);
    console.log(`3. For second occurrence, use str.indexOf("a", 2): ${str.indexOf("a", 2)}`);
    
    console.log("\nTask 2: Checking 'world' in 'Hello world'");
    const worldStr = "Hello world";
    console.log(`1. Start with string: "${worldStr}"`);
    console.log(`2. Use worldStr.indexOf("world"): ${worldStr.indexOf("world")}`);
    console.log(`3. Check if result !== -1: ${worldStr.indexOf("world") !== -1}`);
}

document.addEventListener('DOMContentLoaded', function() {
    console.log('🎓 String Operations Classwork loaded successfully!');
    console.log('📚 This demonstrates the use of indexOf() method for string searching');
    console.log('🔍 Use the buttons to run the string operations');
    console.log('💡 Check the console for detailed information');
    
    console.log('\n💡 Tips:');
    console.log('- indexOf() returns -1 if substring is not found');
    console.log('- Use the second parameter to search from a specific position');
    console.log('- String indices start from 0');
});

if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        findOccurrences,
        checkWorld,
        runAll,
        demonstrateStringMethods,
        showStepByStep
    };
}
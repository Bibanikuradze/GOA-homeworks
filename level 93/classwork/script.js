function testValues() {
    // Clear previous results
    document.getElementById('results').innerHTML = '';
    document.getElementById('console').innerHTML = '';
    
    // Prompt for first value
    const value1 = prompt("Enter the first value:");
    
    // Prompt for second value
    const value2 = prompt("Enter the second value:");
    
    // Test first value
    const isNumber1 = !isNaN(value1);
    const result1 = isNumber1 ? "Is number" : "Is not a number";
    
    // Test second value
    const isNumber2 = !isNaN(value2);
    const result2 = isNumber2 ? "Is number" : "Is not a number";
    
    // Display results on page
    document.getElementById('results').innerHTML = `
        <p><strong>Value 1:</strong> "${value1}" - ${result1}</p>
        <p><strong>Value 2:</strong> "${value2}" - ${result2}</p>
    `;
    
    // Log results to console (and display on page)
    console.log(`Value 1: "${value1}" - ${result1}`);
    console.log(`Value 2: "${value2}" - ${result2}`);
    
    // Display console output on page
    document.getElementById('console').innerHTML = `
        <div>> Value 1: "${value1}" - ${result1}</div>
        <div>> Value 2: "${value2}" - ${result2}</div>
    `;
}

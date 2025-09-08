function processNumbers() {
    // Clear previous results
    document.getElementById('results').innerHTML = '';
    document.getElementById('comparison').innerHTML = '';
    document.getElementById('console').innerHTML = '';
    
    // Prompt for first decimal number as string
    const num1String = prompt("Enter the first decimal number as a string (e.g., '12.5'):");
    
    // Prompt for second decimal number as string
    const num2String = prompt("Enter the second decimal number as a string (e.g., '7.9'):");
    
    // Convert with parseInt() and add
    const num1Int = parseInt(num1String);
    const num2Int = parseInt(num2String);
    const sumInt = num1Int + num2Int;
    
    // Convert with parseFloat() and add
    const num1Float = parseFloat(num1String);
    const num2Float = parseFloat(num2String);
    const sumFloat = num1Float + num2Float;
    
    // Compare the two sums using === operator
    const areEqual = sumInt === sumFloat;
    
    // Display results
    document.getElementById('results').innerHTML = `
        <div class="highlight">
            <h4>Input Values:</h4>
            <p><strong>First number (string):</strong> "${num1String}"</p>
            <p><strong>Second number (string):</strong> "${num2String}"</p>
        </div>
        
        <div class="highlight">
            <h4>parseInt() Conversion:</h4>
            <p><strong>First number:</strong> parseInt("${num1String}") = ${num1Int}</p>
            <p><strong>Second number:</strong> parseInt("${num2String}") = ${num2Int}</p>
            <p><strong>Sum:</strong> ${num1Int} + ${num2Int} = ${sumInt}</p>
        </div>
        
        <div class="highlight">
            <h4>parseFloat() Conversion:</h4>
            <p><strong>First number:</strong> parseFloat("${num1String}") = ${num1Float}</p>
            <p><strong>Second number:</strong> parseFloat("${num2String}") = ${num2Float}</p>
            <p><strong>Sum:</strong> ${num1Float} + ${num2Float} = ${sumFloat}</p>
        </div>
    `;
    
    // Display comparison
    document.getElementById('comparison').innerHTML = `
        <h4>Comparison using === operator:</h4>
        <p><strong>parseInt() sum:</strong> ${sumInt}</p>
        <p><strong>parseFloat() sum:</strong> ${sumFloat}</p>
        <p><strong>Are they equal?</strong> ${sumInt} === ${sumFloat} = ${areEqual}</p>
        <p><em>${areEqual ? 'The sums are equal!' : 'The sums are NOT equal!'}</em></p>
    `;
    
    // Log results to console
    console.log(`Input values: "${num1String}" and "${num2String}"`);
    console.log(`parseInt() conversion: ${num1Int} + ${num2Int} = ${sumInt}`);
    console.log(`parseFloat() conversion: ${num1Float} + ${num2Float} = ${sumFloat}`);
    console.log(`Comparison: ${sumInt} === ${sumFloat} = ${areEqual}`);
    
    // Display console output on page
    document.getElementById('console').innerHTML = `
        <div>> Input values: "${num1String}" and "${num2String}"</div>
        <div>> parseInt() conversion: ${num1Int} + ${num2Int} = ${sumInt}</div>
        <div>> parseFloat() conversion: ${num1Float} + ${num2Float} = ${sumFloat}</div>
        <div>> Comparison: ${sumInt} === ${sumFloat} = ${areEqual}</div>
    `;
}

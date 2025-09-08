// String Slicing Examples

// 1. Extract "world" from "Hello world"
function extractWorld() {
    const text = "Hello world";
    const result = text.slice(6); // "world"
    
    const resultDiv = document.getElementById('result1');
    resultDiv.innerHTML = `
        <strong>Original text:</strong> "${text}"<br>
        <strong>Slice operation:</strong> text.slice(6)<br>
        <strong>Result:</strong> "${result}"<br>
        <strong>Explanation:</strong> Starting from index 6 (after the space) to the end of the string
    `;
    resultDiv.style.display = 'block';
}

// 2. Get first 5 characters from "JavaScript is fun"
function getFirstFive() {
    const text = "JavaScript is fun";
    const result = text.slice(0, 5); // "JavaS"
    
    const resultDiv = document.getElementById('result2');
    resultDiv.innerHTML = `
        <strong>Original text:</strong> "${text}"<br>
        <strong>Slice operation:</strong> text.slice(0, 5)<br>
        <strong>Result:</strong> "${result}"<br>
        <strong>Explanation:</strong> From index 0 to index 5 (exclusive), giving us the first 5 characters
    `;
    resultDiv.style.display = 'block';
}

// 3. Remove first character from "Python"
function removeFirst() {
    const text = "Python";
    const result = text.slice(1); // "ython"
    
    const resultDiv = document.getElementById('result3');
    resultDiv.innerHTML = `
        <strong>Original text:</strong> "${text}"<br>
        <strong>Slice operation:</strong> text.slice(1)<br>
        <strong>Result:</strong> "${result}"<br>
        <strong>Explanation:</strong> Starting from index 1 (second character) to the end, effectively removing the first character
    `;
    resultDiv.style.display = 'block';
}

// 4. Interactive string slicing
function customSlice() {
    const text = document.getElementById('customText').value;
    const startIndex = parseInt(document.getElementById('startIndex').value) || 0;
    const endIndex = document.getElementById('endIndex').value;
    
    let result, operation;
    
    if (endIndex === '' || isNaN(endIndex)) {
        // No end index provided, slice to the end
        result = text.slice(startIndex);
        operation = `text.slice(${startIndex})`;
    } else {
        // Both start and end indices provided
        result = text.slice(startIndex, parseInt(endIndex));
        operation = `text.slice(${startIndex}, ${endIndex})`;
    }
    
    const resultDiv = document.getElementById('customResult');
    resultDiv.innerHTML = `
        <strong>Original text:</strong> "${text}"<br>
        <strong>Slice operation:</strong> ${operation}<br>
        <strong>Result:</strong> "${result}"<br>
        <strong>Text length:</strong> ${text.length}<br>
        <strong>Indices:</strong> ${startIndex}${endIndex !== '' ? ` to ${endIndex}` : ' to end'}
    `;
    resultDiv.style.display = 'block';
}

// 5. Run all examples at once
function runAllExamples() {
    const text1 = "Hello world";
    const result1 = text1.slice(6);
    
    const text2 = "JavaScript is fun";
    const result2 = text2.slice(0, 5);
    
    const text3 = "Python";
    const result3 = text3.slice(1);
    
    const resultDiv = document.getElementById('allResults');
    resultDiv.innerHTML = `
        <h4>All Examples Results:</h4>
        
        <strong>1. Extract "world":</strong><br>
        "${text1}".slice(6) = "${result1}"<br><br>
        
        <strong>2. First 5 characters:</strong><br>
        "${text2}".slice(0, 5) = "${result2}"<br><br>
        
        <strong>3. Remove first character:</strong><br>
        "${text3}".slice(1) = "${result3}"<br><br>
        
        <strong>Summary:</strong> The slice() method extracts a portion of a string based on start and end indices.
    `;
    resultDiv.style.display = 'block';
}

// Additional utility functions for demonstration
function showSliceInfo() {
    const info = `
        <strong>String.slice() Method:</strong><br>
        • Syntax: string.slice(startIndex, endIndex)<br>
        • startIndex: Starting position (0-based)<br>
        • endIndex: Ending position (optional, exclusive)<br>
        • Returns: New string with extracted portion<br>
        • Negative indices count from the end<br>
        • If endIndex is omitted, slices to the end
    `;
    
    // You can add this to any result div or create a new info section
    console.log(info);
}

// Initialize page with some helpful information
document.addEventListener('DOMContentLoaded', function() {
    console.log('String Slicing Examples loaded!');
    console.log('Use the buttons to see string slicing in action.');
    
    // Add some helpful tips
    const tips = [
        '💡 Remember: String indices start at 0, not 1',
        '💡 slice() returns a new string, it doesn\'t modify the original',
        '💡 Negative indices count from the end of the string',
        '💡 If endIndex is omitted, it slices to the end of the string'
    ];
    
    tips.forEach(tip => console.log(tip));
});

// Export functions for potential external use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        extractWorld,
        getFirstFive,
        removeFirst,
        customSlice,
        runAllExamples
    };
}


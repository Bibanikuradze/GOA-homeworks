function calculateExpression() {
    const expression = document.getElementById('expression').value.trim();
    const resultsDiv = document.getElementById('results');
    const errorDiv = document.getElementById('error');
    
    // Hide previous results and errors
    resultsDiv.style.display = 'none';
    errorDiv.style.display = 'none';
    
    if (!expression) {
        showError('Please enter a math expression');
        return;
    }
    
    try {
        // 1. Use eval() to calculate the result
        const result = eval(expression);
        
        // Check if result is a valid number
        if (typeof result !== 'number' || !isFinite(result)) {
            showError('Invalid math expression. Please enter a valid mathematical expression.');
            return;
        }
        
        // 2. Use parseInt() on the result to show the integer part
        const integerResult = parseInt(result);
        
        // 3. Use parseFloat() on the result to show the full decimal value
        const floatResult = parseFloat(result);
        
        // 4. Display all four results
        document.getElementById('original').textContent = expression;
        document.getElementById('evaluated').textContent = result;
        document.getElementById('integer').textContent = integerResult;
        document.getElementById('float').textContent = floatResult;
        
        resultsDiv.style.display = 'block';
        
    } catch (error) {
        showError('Invalid math expression. Please check your input and try again.');
    }
}

function showError(message) {
    const errorDiv = document.getElementById('error');
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
}

// Allow Enter key to trigger calculation
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('expression').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            calculateExpression();
        }
    });
    
    // Focus on input when page loads
    document.getElementById('expression').focus();
});

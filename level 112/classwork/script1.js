function findLargest(...numbers) {
    if (numbers.length === 0) {
        return undefined;
    }
    
    return Math.max(...numbers);
}

console.log("Test 1 - Multiple numbers:", findLargest(5, 2, 8, 1, 9));
console.log("Test 2 - Two numbers:", findLargest(10, 3));
console.log("Test 3 - Single number:", findLargest(42));
console.log("Test 4 - Negative numbers:", findLargest(-5, -2, -8, -1));
console.log("Test 5 - Mixed positive and negative:", findLargest(-10, 5, -3, 8));
console.log("Test 6 - No arguments:", findLargest());

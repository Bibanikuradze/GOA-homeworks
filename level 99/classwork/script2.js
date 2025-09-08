const numbers = [10, 20, 30, 40, 50];

console.log("Original array:", numbers);

const numbers1 = [...numbers];
numbers1.splice(2, 0, 99);

console.log("After inserting 99 at index 2 (Method 1 - splice):", numbers1);

const numbers2 = [...numbers.slice(0, 2), 99, ...numbers.slice(2)];

console.log("After inserting 99 at index 2 (Method 2 - spread):", numbers2);

function insertAt(array, index, value) {
    const newArray = [...array];
    newArray.splice(index, 0, value);
    return newArray;
}

const numbers3 = insertAt(numbers, 2, 99);

console.log("After inserting 99 at index 2 (Method 3 - function):", numbers3);

console.log("Original array (unchanged):", numbers);
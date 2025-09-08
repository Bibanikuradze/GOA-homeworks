const words = [
    "apple", "banana", "cherry", "blueberry", "grape", 
    "orange", "strawberry", "kiwi", "mango", "pineapple"
];

const firstWordWithB = words.find(word => word.startsWith("b"));

console.log("Array of words:", words);
console.log("First word that starts with 'b':", firstWordWithB);

function findFirstWordWithB(words) {
    for (let i = 0; i < words.length; i++) {
        if (words[i].startsWith("b")) {
            return words[i];
        }
    }
    return null;
}

const result = findFirstWordWithB(words);
console.log("Using for loop:", result);

function findFirstWordWithBForOf(words) {
    for (const word of words) {
        if (word.startsWith("b")) {
            return word;
        }
    }
    return null;
}

const resultForOf = findFirstWordWithBForOf(words);
console.log("Using for...of loop:", resultForOf);
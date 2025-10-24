const numbers = [1, 2, 3, 4, 5];
console.log("Original array:", numbers);

const modifiedNumbers = numbers.map(num => 
    num % 2 === 0 ? num + 10 : num - 10
);
console.log("Modified array:", modifiedNumbers);

function sumFiveNumbers(a, b, c, d, e) {
    const sum = a + b + c + d + e;
    console.log(`${a} + ${b} + ${c} + ${d} + ${e} = ${sum}`);
    return sum;
}

const result = sumFiveNumbers(...modifiedNumbers);
console.log("Sum:", result);
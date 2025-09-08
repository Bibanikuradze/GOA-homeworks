const products = [
    { name: "Laptop", price: 1200 },
    { name: "Mouse", price: 25 },
    { name: "Keyboard", price: 75 },
    { name: "Monitor", price: 300 },
    { name: "Headphones", price: 50 },
    { name: "Tablet", price: 150 },
    { name: "Phone", price: 800 },
    { name: "Charger", price: 15 },
    { name: "Cable", price: 8 },
    { name: "Speaker", price: 90 }
];

const affordableProducts = products.filter(product => product.price < 100);

console.log("All products:");
console.log(products);

console.log("\nProducts with price less than 100:");
console.log(affordableProducts);

console.log("\nAffordable products (detailed):");
affordableProducts.forEach(product => {
    console.log(`${product.name}: $${product.price}`);
});
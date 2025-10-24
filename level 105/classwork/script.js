function isOwnProperty(obj, key) {
    return Object.prototype.hasOwnProperty.call(obj, key);
}

const person = { name: "John", age: 30 };
console.log(isOwnProperty(person, 'name'));
console.log(isOwnProperty(person, 'toString'));

function Animal(name) { this.name = name; }
Animal.prototype.speak = function() { return "sound"; };
const dog = new Animal("Buddy");
console.log(isOwnProperty(dog, 'name'));
console.log(isOwnProperty(dog, 'speak'));

const empty = {};
console.log(isOwnProperty(empty, 'any z vali'));

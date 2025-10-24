class Car {
    constructor(brand, model) {
        this.brand = brand;
        this.model = model;
    }

    start() {
        console.log(`${this.brand} ${this.model} is running`);
    }
}

const myCar = new Car('BMW', 'M3');
myCar.start();
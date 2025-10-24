class Bank {
    constructor(username) {
        this.username = username;
        this.balance = 0;
    }

    deposit(amount) {
        this.balance += amount;
        return this.balance;
    }
}

const myBank = new Bank('Gio');
myBank.deposit(150);
console.log(myBank.username, myBank.balance);
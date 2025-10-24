function createPromise() {
    return Promise.resolve("resolved");
}

const promise1 = createPromise();
const promise2 = createPromise();
const promise3 = createPromise();

Promise.all([promise1, promise2, promise3])
    .then(result => console.log(result));
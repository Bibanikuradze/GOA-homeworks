function stringCheckAsync(str) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (str.length % 2 === 0) {
                resolve(str);
            } else {
                reject(str);
            }
        }, 2000);
    });
}

const p1 = stringCheckAsync("even");
const p2 = stringCheckAsync("odd");
const p3 = stringCheckAsync("test");

Promise.all([p1, p2, p3])
    .then(result => {
        console.log("then:", result);
    })
    .catch(error => {
        console.log("catch:", error);
    });
function workingOnPromise(str) {
    const promise = new Promise((resolve, reject) => {
        setTimeout(() => {
            if (str.length > 5) {
                resolve(`String "${str}" is longer than 5 characters`);
            } else {
                reject(`String "${str}" is not longer than 5 characters`);
            }
        }, 1000);
    });

    promise.then(result => {
        console.log("Success:", result);
    }).catch(error => {
        console.log("Error:", error);
    });
}

workingOnPromise("Hello World");
workingOnPromise("Hi");
workingOnPromise("JavaScript");
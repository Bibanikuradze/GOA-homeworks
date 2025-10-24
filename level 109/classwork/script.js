function checkNumber(number) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (number > 10) {
                resolve("resolve");
            } else {
                reject("reject");
            }
        }, 2000);
    });
}

async function handlePromise() {
    try {
        const result = await checkNumber(15);
        console.log(result);
    } catch (error) {
        console.log(error);
    }
}

handlePromise();
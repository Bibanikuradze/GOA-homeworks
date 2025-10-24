function createPromise() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const randomNumber = Math.random();
            if (randomNumber < 0.5) {
                resolve("success");
            } else {
                reject("fail");
            }
        }, 2000);
    });
}

async function handlePromise() {
    try {
        const result = await createPromise();
        console.log("Resolved:", result);
    } catch (error) {
        console.log("Rejected:", error);
    }
}


handlePromise();
function hasLongString(stringArray) {
    return stringArray.some(str => str.length > 10);
}

function hasLongStringForLoop(stringArray) {
    for (let i = 0; i < stringArray.length; i++) {
        if (stringArray[i].length > 10) return true;
    }
    return false;
}

const testArrays = {
    short: ["cat", "dog", "mouse", "tiger", "lion", "bear", "wolf", "fox", "deer", "bird"],
    long: ["elephant", "javascript", "programming", "computer", "science", "code", "web", "html", "css", "python"],
    mixed: ["hi", "supercalifragilisticexpialidocious", "bye", "ok", "yes", "no", "maybe", "sure", "fine", "good"]
};

function testArrays() {
    console.log("Short array:", hasLongString(testArrays.short)); // false
    console.log("Long array:", hasLongString(testArrays.long));   // true
    console.log("Mixed array:", hasLongString(testArrays.mixed)); // true
}

testArrays();
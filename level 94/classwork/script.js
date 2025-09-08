const str1 = "Hello";
const str2 = "World";
const twoJoined = str1.concat(str2);
document.getElementById("two-strings-result").textContent = twoJoined;

const a = "Good";
const b = "Morning";
const c = "Sunshine";
const threeJoined = a.concat(b, c);
document.getElementById("three-strings-result").textContent = threeJoined;

const word1 = "Hello";
const word2 = "World";
const withSpace = word1.concat(" ", word2);
document.getElementById("space-strings-result").textContent = withSpace;
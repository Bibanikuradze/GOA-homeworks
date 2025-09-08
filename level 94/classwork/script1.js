const url = "https://example.com/";
document.getElementById("url-value").textContent = url;
const endsWithSlash = url.endsWith("/");
document.getElementById("url-result").textContent = endsWithSlash ? "Yes" : "No";

function endsWithS(word) {
    if (typeof word !== "string") return false;
    return word.endsWith("s");
}

const word1 = "cats";
const word2 = "book";
document.getElementById("word1-value").textContent = word1;
document.getElementById("word2-value").textContent = word2;
document.getElementById("word1-result").textContent = endsWithS(word1) ? "Ends with 's'" : "Does not end with 's'";
document.getElementById("word2-result").textContent = endsWithS(word2) ? "Ends with 's'" : "Does not end with 's'";

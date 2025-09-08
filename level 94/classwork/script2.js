function endsWithPunctuation(sentence) {
    if (typeof sentence !== "string") return false;
    const trimmed = sentence.trim();
    if (trimmed.length === 0) return false;
    return trimmed.endsWith(".") || trimmed.endsWith("?") || trimmed.endsWith("!");
}

const s1 = "This ends with a period.";
const s2 = "Does this end with a question mark?  ";
const s3 = "This has no punctuation at the end";

document.getElementById("s1-value").textContent = s1;
document.getElementById("s2-value").textContent = s2;
document.getElementById("s3-value").textContent = s3;

document.getElementById("s1-result").textContent = endsWithPunctuation(s1);
document.getElementById("s2-result").textContent = endsWithPunctuation(s2);
document.getElementById("s3-result").textContent = endsWithPunctuation(s3);
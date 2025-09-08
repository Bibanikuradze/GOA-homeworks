const out = document.getElementById('output');
const write = (label, value) => {
    out.innerHTML = `<strong>${label}:</strong> ${value}`;
};

// 1-5) eval()
document.getElementById('t1').onclick = () => {
    const expr = prompt('Enter a math expression (e.g., 5+3):');
    if (expr === null) return;
    try {
    const result = eval(expr);
    write('Result', `${expr} = ${result}`);
    } catch (e) {
    write('Error', 'Invalid expression');
    }
};

document.getElementById('t2').onclick = () => {
    const expr = prompt('Enter an expression with parentheses (e.g., (8+2)*3):');
    if (expr === null) return;
    try {
    const result = eval(expr);
    write('Result', `${expr} = ${result}`);
    } catch (e) {
    write('Error', 'Invalid expression');
    }
};

document.getElementById('t3').onclick = () => {
    const expr = prompt('Enter a division (e.g., 100/4):');
    if (expr === null) return;
    try {
    const result = eval(expr);
    write('Result', `${expr} = ${result}`);
    } catch (e) {
    write('Error', 'Invalid expression');
    }
};

document.getElementById('t4').onclick = () => {
    const numStr = prompt('Enter a number to square:');
    if (numStr === null) return;
    const num = Number(numStr);
    if (Number.isNaN(num)) {
    write('Error', 'Not a valid number');
    return;
    }
    const result = eval('num*num');
    write('Square', `${num}^2 = ${result}`);
};

document.getElementById('t5').onclick = () => {
    let exp = prompt('Store a math expression in a variable (e.g., 20-7):');
    if (exp === null) return;
    try {
    const result = eval(exp);
    write('Eval variable', `${exp} = ${result}`);
    } catch (e) {
    write('Error', 'Invalid expression');
    }
};

// 7-11) isNaN()
document.getElementById('t6').onclick = () => {
    const val = prompt('Enter something (we will check if it is a number):');
    if (val === null) return;
    write('isNaN result', isNaN(val) ? 'Not a number' : 'Number');
};

document.getElementById('t7').onclick = () => {
    const age = prompt('Enter your age:');
    if (age === null) return;
    write('Age validation', isNaN(age) ? 'Invalid age' : 'Valid age');
};

document.getElementById('t8').onclick = () => {
    const v1 = prompt('Enter first value:');
    if (v1 === null) return;
    const v2 = prompt('Enter second value:');
    if (v2 === null) return;
    write('Check two values', `First: ${isNaN(v1) ? 'Not a number' : 'Number'}, Second: ${isNaN(v2) ? 'Not a number' : 'Number'}`);
};

document.getElementById('t9').onclick = () => {
    const any = prompt('Type anything:');
    if (any === null) return;
    write('Type detection', isNaN(any) ? 'Text' : 'Number');
};

document.getElementById('t10').onclick = () => {
    const n1 = prompt('Enter first number:');
    if (n1 === null) return;
    const n2 = prompt('Enter second number:');
    if (n2 === null) return;
    const op = prompt('Enter operator (+, -, *, /):');
    if (op === null) return;
    if (isNaN(n1) || isNaN(n2)) {
    write('Error', 'Both inputs must be valid numbers');
    return;
    }
    const a = parseFloat(n1);
    const b = parseFloat(n2);
    let result;
    switch (op) {
    case '+': result = a + b; break;
    case '-': result = a - b; break;
    case '*': result = a * b; break;
    case '/': result = b === 0 ? 'Infinity' : a / b; break;
    default: result = 'Unknown operator';
    }
    write('Calculator', `${a} ${op} ${b} = ${result}`);
};

// 12-16) parseInt()
document.getElementById('t11').onclick = () => {
    const s = prompt('Enter a whole number as string (e.g., "25"):');
    if (s === null) return;
    write('parseInt', parseInt(s, 10));
};

document.getElementById('t12').onclick = () => {
    const s1 = prompt('Enter first whole number (string):');
    if (s1 === null) return;
    const s2 = prompt('Enter second whole number (string):');
    if (s2 === null) return;
    const sum = parseInt(s1, 10) + parseInt(s2, 10);
    write('Sum', sum);
};

document.getElementById('t13').onclick = () => {
    const s = prompt('Enter "55px" (or similar):');
    if (s === null) return;
    write('parseInt("55px")', parseInt(s, 10));
};

document.getElementById('t14').onclick = () => {
    const a = prompt('Enter a value like "20px":');
    if (a === null) return;
    const b = prompt('Enter a value like "15.9":');
    if (b === null) return;
    const sum = parseInt(a, 10) + parseInt(b, 10);
    write('parseInt sum', sum);
};

document.getElementById('t15').onclick = () => {
    const s = prompt('Enter hexadecimal like "0xF":');
    if (s === null) return;
    write('Hex parsed', parseInt(s, 16));
};

// 17-21) parseFloat()
document.getElementById('t16').onclick = () => {
    const p1 = prompt('Enter first price (e.g., 19.99):');
    if (p1 === null) return;
    const p2 = prompt('Enter second price (e.g., 5.50):');
    if (p2 === null) return;
    const total = parseFloat(p1) + parseFloat(p2);
    write('Total price', total.toFixed(2));
};

document.getElementById('t17').onclick = () => {
    const bill = prompt('Bill amount (e.g., 45.75):');
    if (bill === null) return;
    const tipPct = prompt('Tip percentage (e.g., 15):');
    if (tipPct === null) return;
    const b = parseFloat(bill);
    const t = (b * parseFloat(tipPct)) / 100;
    write('Tip and total', `Tip: ${t.toFixed(2)}, Total: ${(b + t).toFixed(2)}`);
};

document.getElementById('t18').onclick = () => {
    const c = prompt('Temperature in Celsius (e.g., 36.6):');
    if (c === null) return;
    const f = (parseFloat(c) * 9) / 5 + 32;
    write('Celsius to Fahrenheit', `${f.toFixed(2)} °F`);
};

document.getElementById('t19').onclick = () => {
    const w = prompt('Weight in kg (e.g., 70.5):');
    if (w === null) return;
    const h = prompt('Height in meters (e.g., 1.75):');
    if (h === null) return;
    const bmi = parseFloat(w) / (parseFloat(h) ** 2);
    write('BMI', bmi.toFixed(2));
};

document.getElementById('t20').onclick = () => {
    const d = prompt('Distance traveled in km (e.g., 350.7):');
    if (d === null) return;
    const f = prompt('Fuel used in liters (e.g., 28.5):');
    if (f === null) return;
    const kpl = parseFloat(d) / parseFloat(f);
    write('Km per liter', kpl.toFixed(2));
};

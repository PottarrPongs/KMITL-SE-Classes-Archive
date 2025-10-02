let result;
let reset = true;
let operatorPressed = false;
let text = "0";
let numbers = ["0"];
let operator = "";
let memory = 0;

document.addEventListener("DOMContentLoaded", () => {
    result = document.getElementById("result");
});

document.addEventListener("keypress", (event) => {
    const key = String.fromCharCode(event.charCode);

    if (key >= "0" && key <= "9") {
        if (operatorPressed) {
            numbers.push("");
            text = "";
            operatorPressed = false;
        }

        if (reset) {
            text = key;
            reset = false;
        } else {
            text += key;
        }
        numbers[numbers.length - 1] = text;
    } else if (key == "+" || key == "-" || key == "*" || key == "/") {
        if (numbers.length == 2) {
            calculate();
        }
        operatorPressed = true;
        operator = key;
    } else if (key == "<") {
        text = text.slice(0, -1);
        if (text == "") {
            if (numbers.length > 1) {
                numbers.pop();
                operatorPressed = false;
                operator = "";
                text = numbers[numbers.length - 1];
            } else {
                text = "0";
                reset = true;
            }
        }
        numbers[numbers.length - 1] = text;

    } else if (key == "=") {
        calculate();
    } else if (key == "c") {
        reset = true;
        operatorPressed = false;
        text = "0";
        numbers = ["0"];
        operator = "";
    }

    result.innerHTML = text;
})

function calculate() {
    if (numbers.length == 2) {
        let ans;
        const b = parseFloat(numbers.pop());
        const a = parseFloat(numbers.pop());
        switch (operator) {
            case "+":
                ans = a + b;
                break;
            case "-":
                ans = a - b;
                break;
            case "*":
                ans = a * b;
                break;
            case "/":
                ans = a / b;
                break;
        }
        numbers = [ans];
        text = "" + ans;
        operatorPressed = false;
        operator = "";
    }
}

document.getElementById("sin").addEventListener("click", () => {
    let num = parseFloat(text);
    num = Math.sin(num);
    text = num.toFixed(2);
    numbers[numbers.length - 1] = text;
    result.innerHTML = text;
});
document.getElementById("cos").addEventListener("click", () => {
    let num = parseFloat(text);
    num = Math.cos(num);
    text = num.toFixed(2);
    numbers[numbers.length - 1] = text;
    result.innerHTML = text;
});
document.getElementById("tan").addEventListener("click", () => {
    let num = parseFloat(text);
    num = Math.tan(num);
    text = num.toFixed(2);
    numbers[numbers.length - 1] = text;
    result.innerHTML = text;
});
document.getElementById("pi").addEventListener("click", () => {
    text = Math.PI.toFixed(2);
    numbers[numbers.length - 1] = text;
    result.innerHTML = text;
});
document.getElementById("sqrt").addEventListener("click", () => {
    let num = parseFloat(text);
    num = Math.sqrt(num);
    text = num.toFixed(2);
    numbers[numbers.length - 1] = text;
    result.innerHTML = text;
});
document.getElementById("square").addEventListener("click", () => {
    let num = parseFloat(text);
    num = Math.pow(num, 2);
    text = num.toFixed(2);
    numbers[numbers.length - 1] = text;
    result.innerHTML = text;
});
document.getElementById("1/x").addEventListener("click", () => {
    let num = parseFloat(text);
    num = 1.0 / num;
    text = num.toFixed(2);
    numbers[numbers.length - 1] = text;
    result.innerHTML = text;
});
document.getElementById("factorial").addEventListener("click", () => {
    let num = parseFloat(text);
    if (num - Math.floor(num) == 0.0) {
        num = factorial(num);
        text = "" + num;
        numbers[numbers.length - 1] = text;
        result.innerHTML = text;
    }
});

function factorial(n) {
    if (n < 2) return 1;
    return n * (factorial(n - 1));
}

document.getElementById("mc").addEventListener("click", () => {
    memory = 0;
});
document.getElementById("m+").addEventListener("click", () => {
    memory += parseFloat(text);
});
document.getElementById("m-").addEventListener("click", () => {
    let num = parseFloat(text);
    num -= memory;
    memory = num;
});
document.getElementById("mr").addEventListener("click", () => {
    text = "" + memory;
    numbers[numbers.length - 1] = text;
    result.innerHTML = text;
});

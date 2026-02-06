const display = document.getElementById('display');
const numberButtons = document.querySelectorAll('.number');
const operatorButtons = document.querySelectorAll('.operator');
const equalsButton = document.getElementById('equals');
const clearButton = document.getElementById('clear');
const backspaceButton = document.getElementById('backspace');

let expression = '';

// Number button click handler
numberButtons.forEach(button => {
    button.addEventListener('click', () => {
        expression += button.dataset.value;
        display.value = expression;
    });
});

// Operator button click handler
operatorButtons.forEach(button => {
    button.addEventListener('click', () => {
        if (expression && !isLastCharOperator()) {
            expression += button.dataset.value;
            display.value = expression;
        }
    });
});

// Equals button click handler
equalsButton.addEventListener('click', () => {
    if (expression) {
        fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ expression: expression })
        })
        .then(response => response.json())
        .then(data => {
            if (!data.error) {
                display.value = data.result;
                expression = data.result;
            } else {
                display.value = 'Error';
                expression = '';
            }
        });
    }
});

// Clear button click handler
clearButton.addEventListener('click', () => {
    expression = '';
    display.value = '';
});

// Backspace button click handler
backspaceButton.addEventListener('click', () => {
    expression = expression.slice(0, -1);
    display.value = expression;
});

// Check if last character is an operator
function isLastCharOperator() {
    const lastChar = expression[expression.length - 1];
    return ['+', '-', '*', '/'].includes(lastChar);
}

// Keyboard support
document.addEventListener('keydown', (event) => {
    if (event.key >= '0' && event.key <= '9') {
        expression += event.key;
        display.value = expression;
    } else if (['+', '-', '*', '/'].includes(event.key)) {
        if (expression && !isLastCharOperator()) {
            expression += event.key;
            display.value = expression;
        }
    } else if (event.key === '.') {
        expression += event.key;
        display.value = expression;
    } else if (event.key === 'Enter') {
        equalsButton.click();
    } else if (event.key === 'Backspace') {
        expression = expression.slice(0, -1);
        display.value = expression;
    } else if (event.key === 'c' || event.key === 'C') {
        expression = '';
        display.value = '';
    }
});

function calculate() {
  var num1 = parseFloat(document.getElementById("num1").value);
  var num2 = parseFloat(document.getElementById("num2").value);

  var sum = num1 + num2;
  var subtract = num1 - num2;
  var multiply = num1 * num2;

  var divide = "Cannot divide by zero";
  if (num2 !== 0) {
    divide = num1 / num2;
  }

  document.getElementById("sum").textContent = sum;
  document.getElementById("subtract").textContent = subtract;
  document.getElementById("multiply").textContent = multiply;
  document.getElementById("divide").textContent = divide;
}

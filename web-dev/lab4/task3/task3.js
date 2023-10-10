function calculate() {
  // Get the input values
  var num1 = parseFloat(document.getElementById("num1").value);
  var num2 = parseFloat(document.getElementById("num2").value);
  var num3 = parseFloat(document.getElementById("num3").value);
  var num4 = parseFloat(document.getElementById("num4").value);
  var num5 = parseFloat(document.getElementById("num5").value);

  const numArr = [num1, num2, num3, num4, num5];

  var minimum = Math.min(num1, num2, num3, num4, num5);
  var maximum = Math.max(num1, num2, num3, num4, num5);

  document.getElementById("min").textContent = minimum;
  document.getElementById("max").textContent = maximum;

  // Generate a random index between 0 and the length of the array minus 1
  var randomIndex = Math.floor(Math.random() * numArr.length);
  var randomNum = numArr[randomIndex];

  document.getElementById("randomNumber").textContent = randomNum;
}

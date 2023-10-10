function boldText() {
  var elements = document.querySelectorAll(".bold-text");
  elements.forEach(function (element) {
    element.innerHTML = "<strong>" + element.innerHTML + "</strong>";
  });
}

function applyAllCapsStyle() {
  var elements = document.querySelectorAll(".all-caps");
  elements.forEach(function (element) {
    element.textContent = element.textContent.toUpperCase();
  });
}

function fontSize(size) {
  var elements = document.querySelectorAll(".big-font");
  elements.forEach(function (element) {
    element.style.fontSize = size;
  });
}

function italicsText() {
  var elements = document.querySelectorAll(".italics");
  elements.forEach(function (element) {
    element.innerHTML = "<em>" + element.innerHTML + "</em>";
  });
}

function strikeText() {
  var elements = document.querySelectorAll(".strikethrough");
  elements.forEach(function (element) {
    element.innerHTML = "<s>" + element.innerHTML + "</s>";
  });
}

function linkText(url) {
  var elements = document.querySelectorAll(".link-text");
  elements.forEach(function (element) {
    var anchor = document.createElement("a");
    anchor.href = url;
    anchor.textContent = element.textContent;
    element.textContent = "";
    element.appendChild(anchor);
  });
}

fontSize("25px");
italicsText();
strikeText();
linkText("");
applyAllCapsStyle();
boldText();

const questions = [
  {
    question: "Who is the best teacher this semester?",
    options: ["Sir Jawad", "Sir Akheem", "Johnny Depp", "Johnny Bravo"],
    correctAnswer: "Sir Akheem",
  },
  {
    question: "Who will get an A grade in Web Dev regardless of marks?",
    options: ["Random Student", "Backbencher", "Daim", "No one"],
    correctAnswer: "Daim",
  },
  {
    question:
      "In the Assassin's Creed series, what is the name of the device that allows characters to relive the memories of their ancestors?",
    options: ["Animus", "Helix", "Nexus", "The Matrix"],
    correctAnswer: "Animus",
  },
  {
    question:
      "Which actor played the character, Johnny Silverhand, in the game Cyberpunk 2077?",
    options: [
      "Norman Reedus",
      "Michael Fassbender",
      "Tom Hardy",
      "Keanu Reeves",
    ],
    correctAnswer: "Keanu Reeves",
  },
];

let currentQuestionIndex = 0;
let score = 0;

const questionElement = document.getElementById("question");
const optionsElement = document.getElementById("options");
const nextBtn = document.getElementById("next-btn");
const restartBtn = document.getElementById("restart-btn");
const scoreElement = document.getElementById("score");

function showQuestion() {
  const currentQuestion = questions[currentQuestionIndex];
  questionElement.textContent = currentQuestion.question;

  optionsElement.innerHTML = "";
  currentQuestion.options.forEach((option, index) => {
    const optionElement = document.createElement("div");
    optionElement.classList.add("option");
    optionElement.textContent = option;
    optionElement.onclick = () => checkAnswer(index);
    optionsElement.appendChild(optionElement);
  });

  updateScore();
}

function checkAnswer(selectedIndex) {
  const currentQuestion = questions[currentQuestionIndex];
  if (
    currentQuestion.options[selectedIndex] === currentQuestion.correctAnswer
  ) {
    score++;
  }

  currentQuestionIndex++;
  if (currentQuestionIndex < questions.length) {
    showQuestion();
  } else {
    showFinalScore();
  }
}

function showFinalScore() {
  questionElement.textContent = `Your Final Score: ${score} out of ${questions.length}`;
  optionsElement.innerHTML = "";
  nextBtn.style.display = "none";
  restartBtn.style.display = "block";
  updateScore();
}

function nextQuestion() {
  showQuestion();
}

function restartQuiz() {
  currentQuestionIndex = 0;
  score = 0;
  nextBtn.style.display = "block";
  restartBtn.style.display = "none";
  showQuestion();
}

function updateScore() {
  scoreElement.textContent = `Score: ${score}`;
}

showQuestion();

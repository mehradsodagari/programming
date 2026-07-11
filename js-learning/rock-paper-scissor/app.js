const options = {
  1: "rock",
  2: "paper",
  3: "scissor",
};
let paragraph = document.querySelector(".result");
let userScore = 0;
let computerScore = 0;
function reset() {
  location.reload();
}
function pc() {
  let choosed = Math.floor(Math.random() * 3 + 1);
  return options[choosed];
}
function win() {
  if (userScore === 3) {
    paragraph.textContent = "user won";
    setTimeout(() => {
      reset();
    }, 1500);
    return true;
  }
  if (computerScore === 3) {
    paragraph.textContent = "computer won";
    setTimeout(() => {
      reset();
    }, 1500);
    return true;
  }
  return false;
}
function game(option) {
  let roundWinner = "";
  let computer = pc();
  if (option === "rock") {
    if (computer === "paper") {
      computerScore += 1;
      roundWinner = "Computer won this round";
      paragraph.textContent = `You chose ${option}, computer chose ${computer}. ${roundWinner}`;
    } else if (computer === "scissor") {
      userScore += 1;
      roundWinner = "User won this round";
      paragraph.textContent = `You chose ${option}, computer chose ${computer}. ${roundWinner}`;
    } else {
      paragraph.textContent = `Draw! You both chose ${option}`;
    }
  } else if (option === "paper") {
    if (computer === "rock") {
      userScore += 1;
      roundWinner = "User won this round";
      paragraph.textContent = `You chose ${option}, computer chose ${computer}. ${roundWinner}`;
    } else if (computer === "scissor") {
      computerScore += 1;
      roundWinner = "Computer won this round";
      paragraph.textContent = `You chose ${option}, computer chose ${computer}. ${roundWinner}`;
    } else {
      paragraph.textContent = `Draw! You both chose ${option}`;
    }
  } else if (option === "scissor") {
    if (computer === "paper") {
      userScore += 1;
      roundWinner = "User won this round";
      paragraph.textContent = `You chose ${option}, computer chose ${computer}. ${roundWinner}`;
    } else if (computer === "rock") {
      computerScore += 1;
      roundWinner = "Computer won this round";
      paragraph.textContent = `You chose ${option}, computer chose ${computer}. ${roundWinner}`;
    } else {
      paragraph.textContent = `Draw! You both chose ${option}`;
    }
  }
  document.getElementById("user-score").textContent = `user : ${userScore}`;
  document.getElementById("pc-score").textContent =
    `computer : ${computerScore}`;
  win();
}
let choose;
document.getElementById("rock").addEventListener("click", () => {
  choose = "rock";
  game(choose);
});
document.getElementById("paper").addEventListener("click", () => {
  choose = "paper";
  game(choose);
});
document.getElementById("scissor").addEventListener("click", () => {
  choose = "scissor";
  game(choose);
});

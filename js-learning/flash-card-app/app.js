let countID = 1;
let cards = [];
function saveCard(event) {
  event.preventDefault();
  let question = document.getElementById("q").value.trim();
  let answer = document.getElementById("a").value.trim();
  let category = document.getElementById("cat").value.trim();
  if (question.length === 0) {
    alert("Fill the question");
  } else if (answer.length === 0) {
    alert("Fill the answer");
  } else if (category === "") {
    alert("Choose the category");
  } else {
    let card = {
      ID: countID++,
      Question: question,
      Answer: answer,
      Category: category,
      Favorite: false,
      CreatedAt: new Date(),
    };
    cards.push(card);
    console.log(card);
    document.querySelector("form").reset();
    render();
    return card;
  }
}
function render() {
  let container = document.getElementById("container");
  while (container.firstChild) {
    container.removeChild(container.firstChild);
  }
  for (let card of cards) {
    let section = document.createElement("section");
    section.classList.add("card");
    section.setAttribute("data-id", card.ID);
    if (card.Favorite) {
      section.classList.add("is-fav");
    }
    let questionParagraph = document.createElement("p");
    let answerParagraph = document.createElement("p");
    let categoryTitle = document.createElement("h3");
    let showAnswer = document.createElement("button");
    let favoriteBTN = document.createElement("button");
    let deleteBTN = document.createElement("button");
    questionParagraph.textContent = `Question: ${card.Question}`;
    questionParagraph.classList.add("question");
    answerParagraph.textContent = `Answer: ${card.Answer}`;
    answerParagraph.classList.add("answer");
    categoryTitle.textContent = `Category: ${card.Category}`;
    categoryTitle.classList.add("category");
    showAnswer.textContent = "Show the answer";
    showAnswer.classList.add("show-btn");
    favoriteBTN.textContent = card.Favorite
      ? "⭐ Favorited"
      : "Add to favorite";
    favoriteBTN.classList.add("fav-btn");
    deleteBTN.textContent = "Delete";
    deleteBTN.classList.add("del-btn");
    showAnswer.addEventListener("click", function () {
      section.classList.toggle("flipped");
      section.style.backgroundColor = section.classList.contains("flipped")
        ? "#eef"
        : "#fff";
    });
    favoriteBTN.addEventListener("click", (e) => {
      e.stopPropagation();
      card.Favorite = !card.Favorite;
      render();
    });
    deleteBTN.addEventListener("click", (e) => {
      e.stopPropagation();
      let idRemove = Number(section.getAttribute("data-id"));
      cards = cards.filter((c) => c.ID !== idRemove);
      render();
    });
    section.append(questionParagraph);
    section.append(answerParagraph);
    section.append(categoryTitle);
    section.append(showAnswer);
    section.append(favoriteBTN);
    section.append(deleteBTN);
    container.append(section);
  }
}
document.querySelector("form").addEventListener("submit", saveCard);

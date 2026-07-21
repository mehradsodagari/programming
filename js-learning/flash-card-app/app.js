let countID = JSON.parse(localStorage.getItem("count")) || 1;
saveInStorage("count", countID);
let cards = JSON.parse(localStorage.getItem("cards")) || [];
let studyCards = [];
let currentCardIndex = 0;
let timer;
let time = 5 * 60;
function saveCard(event) {
  event.preventDefault();
  let question = document.getElementById("q").value.trim();
  let answer = document.getElementById("a").value.trim();
  let category = document.getElementById("cat").value.trim();
  let editingID = document.getElementById("editing-id").value;
  if (question.length === 0) {
    alert("Fill the question");
    return;
  } else if (answer.length === 0) {
    alert("Fill the answer");
    return;
  } else if (category === "") {
    alert("Choose the category");
    return;
  }
  if (editingID !== "") {
    let id = Number(editingID);
    let index = cards.findIndex((card) => card.ID === id);
    if (index !== -1) {
      cards[index] = {
        ...cards[index],
        Question: question,
        Answer: answer,
        Category: category,
      };
    }
    saveInStorage("cards", cards);
    document.querySelector("form").reset();
    document.getElementById("editing-id").value = "";
    document.getElementById("enter-btn").textContent = "Enter";
    render();
    return;
  }
  countID = JSON.parse(localStorage.getItem("count")) || countID;
  let card = {
    ID: countID++,
    Question: question,
    Answer: answer,
    Category: category,
    Favorite: false,
    CreatedAt: new Date(),
  };

  saveInStorage("count", countID);
  cards.push(card);
  saveInStorage("cards", cards);
  document.querySelector("form").reset();
  document.getElementById("editing-id").value = "";
  document.getElementById("enter-btn").textContent = "Enter";
  render();
}
function render() {
  let list = filterSearch();
  let container = document.getElementById("container");
  container.innerHTML = "";
  for (let card of list) {
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
    let editBTN = document.createElement("button");
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
    editBTN.textContent = "Edit";
    editBTN.classList.add("edit-btn");
    showAnswer.addEventListener("click", function () {
      section.classList.toggle("flipped");
      section.style.backgroundColor = section.classList.contains("flipped")
        ? "#eef"
        : "grey";
    });
    favoriteBTN.addEventListener("click", (e) => {
      e.stopPropagation();
      card.Favorite = !card.Favorite;
      saveInStorage("cards", cards);
      render();
    });
    deleteBTN.addEventListener("click", (e) => {
      e.stopPropagation();
      let idRemove = Number(section.getAttribute("data-id"));
      cards = cards.filter((c) => c.ID !== idRemove);
      saveInStorage("cards", cards);
      if (Number(document.getElementById("editing-id").value) === idRemove) {
        document.querySelector("form").reset();
        document.getElementById("editing-id").value = "";
        document.getElementById("enter-btn").textContent = "Enter";
      }
      render();
    });
    editBTN.addEventListener("click", function (e) {
      e.stopPropagation();
      document.getElementById("q").value = card.Question;
      document.getElementById("a").value = card.Answer;
      document.getElementById("cat").value = card.Category;
      document.getElementById("editing-id").value = card.ID;
      document.getElementById("enter-btn").textContent = "Update";
    });
    section.append(questionParagraph);
    section.append(answerParagraph);
    section.append(categoryTitle);
    section.append(showAnswer);
    section.append(favoriteBTN);
    section.append(deleteBTN);
    section.append(editBTN);
    container.append(section);
  }
}
function saveInStorage(name, list) {
  localStorage.setItem(name, JSON.stringify(list));
}
function filterSearch() {
  let list = [];
  let search = String(document.getElementById("search").value);
  search = search.toLowerCase();
  let topic = String(document.getElementById("topic").value);
  topic = topic.toLowerCase();
  if (topic !== "all") {
    if (topic !== "favorite") {
      list = cards.filter((card) =>
        card.Category.toLowerCase().includes(topic),
      );
      if (search) {
        list = cards.filter(
          (card) =>
            card.Category.toLowerCase().includes(topic) &&
            card.Question.toLowerCase().includes(search),
        );
      }
    } else {
      list = cards.filter((card) => card.Favorite);
      if (search) {
        list = cards.filter(
          (card) =>
            card.Favorite && card.Question.toLowerCase().includes(search),
        );
      }
    }
  } else {
    list = cards;
    if (search) {
      list = cards.filter((card) =>
        card.Question.toLowerCase().includes(search),
      );
    }
  }
  return list;
}
function renderStudyZone() {
  let studyCardContainer = document.getElementById("study-zone-div");
  let emptyMessage = document.getElementById("study-zone-paragraph");
  let counter = document.getElementById("which-card");
  let nextButton = document.getElementById("next");
  let previousButton = document.getElementById("previous");
  studyCardContainer.innerHTML = "";
  if (studyCards.length === 0) {
    studyCardContainer.style.display = "none";
    emptyMessage.style.display = "block";
    emptyMessage.textContent = "There is no card to study";
    counter.textContent = "0 of 0";
    nextButton.disabled = true;
    previousButton.disabled = true;
    return;
  }
  if (currentCardIndex >= studyCards.length) {
    currentCardIndex = studyCards.length - 1;
  }
  if (currentCardIndex < 0) {
    currentCardIndex = 0;
  }
  counter.textContent = `${currentCardIndex + 1} of ${studyCards.length}`;
  nextButton.disabled = currentCardIndex === studyCards.length - 1;
  previousButton.disabled = currentCardIndex === 0;
  let card = studyCards[currentCardIndex];
  emptyMessage.style.display = "none";
  studyCardContainer.style.display = "block";
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
  let editBTN = document.createElement("button");
  questionParagraph.textContent = `Question: ${card.Question}`;
  questionParagraph.classList.add("question");
  answerParagraph.textContent = `Answer: ${card.Answer}`;
  answerParagraph.classList.add("answer");
  categoryTitle.textContent = `Category: ${card.Category}`;
  categoryTitle.classList.add("category");
  showAnswer.textContent = "Show the answer";
  showAnswer.classList.add("show-btn");
  favoriteBTN.textContent = card.Favorite ? "⭐ Favorited" : "Add to favorite";
  favoriteBTN.classList.add("fav-btn");
  deleteBTN.textContent = "Delete";
  deleteBTN.classList.add("del-btn");
  editBTN.textContent = "Edit";
  editBTN.classList.add("edit-btn");
  showAnswer.addEventListener("click", function () {
    section.classList.toggle("flipped");
    section.style.backgroundColor = section.classList.contains("flipped")
      ? "#eef"
      : "grey";
  });
  favoriteBTN.addEventListener("click", (e) => {
    e.stopPropagation();
    card.Favorite = !card.Favorite;
    saveInStorage("cards", cards);
    let checkBox = document.getElementById("fav-cards");
    if (checkBox && checkBox.checked) {
      studyCards = cards.filter((c) => c.Favorite);
      if (currentCardIndex >= studyCards.length) {
        currentCardIndex = Math.max(0, studyCards.length - 1);
      }
    }
    renderStudyZone();
    render();
  });
  deleteBTN.addEventListener("click", (e) => {
    e.stopPropagation();
    let idRemove = Number(section.getAttribute("data-id"));
    cards = cards.filter((c) => c.ID !== idRemove);
    studyCards = studyCards.filter((c) => c.ID !== idRemove);
    saveInStorage("cards", cards);
    if (Number(document.getElementById("editing-id").value) === idRemove) {
      document.querySelector("form").reset();
      document.getElementById("editing-id").value = "";
      document.getElementById("enter-btn").textContent = "Enter";
    }
    if (currentCardIndex >= studyCards.length) {
      currentCardIndex = Math.max(0, studyCards.length - 1);
    }
    renderStudyZone();
    render();
  });
  editBTN.addEventListener("click", function (e) {
    e.stopPropagation();
    document.getElementById("q").value = card.Question;
    document.getElementById("a").value = card.Answer;
    document.getElementById("cat").value = card.Category;
    document.getElementById("editing-id").value = card.ID;
    document.getElementById("enter-btn").textContent = "Update";
    backToPanel();
  });
  section.append(
    questionParagraph,
    answerParagraph,
    categoryTitle,
    showAnswer,
    favoriteBTN,
    deleteBTN,
    editBTN,
  );
  studyCardContainer.append(section);
}
function study() {
  time = 5 * 60;
  document.getElementById("panel").disabled = false;
  document.getElementById("next").disabled = false;
  document.getElementById("previous").disabled = false;
  let studyZone = document.querySelector(".study-zone");
  let main = document.getElementById("main");
  let ShowTime = document.getElementById("show-time");
  document.getElementById("show-message").textContent = "";
  clearInterval(timer);
  let minutes = Math.floor(time / 60);
  let seconds = time % 60;
  minutes = String(minutes);
  seconds = String(seconds);
  minutes = minutes.padStart(2, "0");
  seconds = seconds.padStart(2, "0");
  ShowTime.textContent = `${minutes}:${seconds}`;
  minutes = Number(minutes);
  seconds = Number(seconds);
  timer = setInterval(() => {
    minutes = Math.floor(time / 60);
    seconds = time % 60;
    minutes = String(minutes);
    seconds = String(seconds);
    minutes = minutes.padStart(2, "0");
    seconds = seconds.padStart(2, "0");
    ShowTime.textContent = `${minutes}:${seconds}`;
    minutes = Number(minutes);
    seconds = Number(seconds);
    time -= 1;
    if (time === -1) {
      document.getElementById("panel").disabled = true;
      document.getElementById("next").disabled = true;
      document.getElementById("previous").disabled = true;
      clearInterval(timer);
      document.getElementById("show-message").textContent =
        "The study time for this course is over. Well done";
      setTimeout(() => {
        main.classList.remove("hidden");
        studyZone.classList.add("hidden");
      }, 1000);
      time = 5 * 60;
    }
  }, 1000);
  currentCardIndex = 0;
  let checkbox = document.getElementById("fav-cards");
  if (checkbox && checkbox.checked) {
    studyCards = cards.filter((card) => card.Favorite);
  } else {
    studyCards = [...cards];
  }
  main.classList.add("hidden");
  studyZone.classList.remove("hidden");
  document.getElementById("start-controls").classList.add("hidden");

  renderStudyZone();
}
function backToPanel() {
  let studyZone = document.querySelector(".study-zone");
  clearInterval(timer);
  document.getElementById("show-time").textContent = "";
  document.getElementById("show-message").textContent = "";
  time = 5 * 60;
  let main = document.getElementById("main");
  main.classList.remove("hidden");
  studyZone.classList.add("hidden");
  document.getElementById("start-controls").classList.remove("hidden");
}

document.addEventListener("DOMContentLoaded", () => {
  render();
  document.getElementById("search").addEventListener("input", render);
  document.getElementById("topic").addEventListener("change", render);
  document.getElementById("start").addEventListener("click", study);
  document.getElementById("panel").addEventListener("click", backToPanel);
  document.getElementById("next").addEventListener("click", () => {
    if (currentCardIndex < studyCards.length - 1) {
      currentCardIndex += 1;
      renderStudyZone();
    }
  });
  document.getElementById("previous").addEventListener("click", () => {
    if (currentCardIndex > 0) {
      currentCardIndex -= 1;
      renderStudyZone();
    }
  });
  document.querySelector("form").addEventListener("submit", saveCard);
});

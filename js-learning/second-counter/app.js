let count = 0;
let counter;
function save() {
  count = Number(document.cookie.split("=")[1]);
  document.querySelector("h3").textContent = count;
}
function start() {
  counter = setInterval(() => {
    count++;
    document.querySelector("h3").textContent = count;
    document.cookie = "count=" + count;
    document.querySelector(".start").disabled = true;
    document.querySelector(".pause").disabled = false;
    document.querySelector(".reset").disabled = false;
    if (count === 0) {
    document.querySelector(".reset").disabled = true;
    document.querySelector(".pause").disabled = true;
  }
  }, 1000);
}
function pause() {
  clearInterval(counter);
  document.querySelector(".start").disabled = false;
  document.querySelector(".pause").disabled = true;
  if (count === 0) {
    document.querySelector(".reset").disabled = true;
    document.querySelector(".pause").disabled = true;
  }
}
function reset() {
  count = 0;
  document.cookie = "count=" + count;
  pause()
  document.querySelector("h3").textContent = count;
  document.querySelector(".start").disabled = false;
  document.querySelector(".pause").disabled = false;
  if (count === 0) {
    document.querySelector(".reset").disabled = true;
    document.querySelector(".pause").disabled = true;
  }
}

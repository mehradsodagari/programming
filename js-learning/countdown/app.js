let count
let counter;
function set() {
    count = Number(document.querySelector("#count").value);
    if(count<0) {
        document.querySelector("p").textContent = "❌seonds cannot be negative❌"
    }
}
document.querySelector("#reset").disabled = true;
function start() {
  counter = setInterval(() => {
    let paragraph = document.querySelector("p");
    let minutes = 0;
    while (count >= 60) {
      count -= 60;
      minutes++;
    }
    let seconds = count;
    paragraph.textContent = `${minutes}:${seconds}`;
    count = minutes * 60 + seconds - 1;
    if (count === -1) {
      clearInterval(counter);
      document.querySelector("#start").disabled = true;
      document.querySelector("#pause").disabled = true;
      document.querySelector("#reset").disabled = false;
    }
  }, 1000);
  document.querySelector("#start").disabled = true;
  document.querySelector("#pause").disabled = false;
  document.querySelector("#reset").disabled = false;
}
function pause() {
  clearInterval(counter);
  document.querySelector("#start").disabled = false;
  document.querySelector("#pause").disabled = true;
  document.querySelector("#reset").disabled = false;
}
function reset() {
  document.location.reload();
}

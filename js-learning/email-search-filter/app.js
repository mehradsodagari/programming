const emails = [
  "ali@gmail.com",
  "sara@yahoo.com",
  "test@gmail.com",
  "hello@company.com",
  "admin@gmail.com",
];
function find() {
  document.querySelector(".result").innerHTML=""
  const include = [];
  const start = [];
  const end = [];
  const input = document.querySelector("input").value.trim();
  for (let email of emails) {
    if (email.startsWith(input)) {
      start.push(email);
    } 
     if (email.endsWith(input)) {
      end.push(email);
    } 
     if (email.includes(input)) {
      include.push(email);
    }
  }
  if (include.length === 0 && start.length === 0 && end.length === 0) {
    let paragraph = document.createElement("p");
    paragraph.textContent = "ey baba";
    document.querySelector(".result").appendChild(paragraph);
    return
  }
  if (start.length !== 0) {
    let div = document.createElement("div");
    div.classList.add("blue")
    document.querySelector(".result").appendChild(div)
    let hTwo = document.createElement("h2");
    hTwo.textContent = "start";
    div.appendChild(hTwo);
    let ul = document.createElement("ul");
    ul.classList.add("start")
    div.appendChild(ul)
    for (let st of start) {
      let li = document.createElement("li");
      li.textContent = st;
      ul.appendChild(li);
    }
  }
  if (end.length !== 0) {
    let div = document.createElement("div");
    div.classList.add("purple")
    document.querySelector(".result").appendChild(div)
    let hTwo = document.createElement("h2");
    hTwo.textContent = "end";
    div.appendChild(hTwo);
    let ul = document.createElement("ul");
    ul.classList.add("end")
    div.appendChild(ul)
    for (let en of end) {
      let li = document.createElement("li");
      li.textContent = en;
      ul.appendChild(li);
    }
  }
 if (include.length !== 0) {
    let div = document.createElement("div");
    div.classList.add("pink")
    document.querySelector(".result").appendChild(div)
    let hTwo = document.createElement("h2");
    hTwo.textContent = "include";
    div.appendChild(hTwo);
    let ul = document.createElement("ul");
    ul.classList.add("include")
    div.appendChild(ul)
    for (let inc of include) {
      let li = document.createElement("li");
      li.textContent = inc;
      ul.appendChild(li);
    }
  }
};

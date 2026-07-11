let userSetting = {
  theme: "light",
};
let count = 0;
const store = {
  electronics: {
    name: "Electronics",
    products: [
      { name: "Laptop", price: 1200 },
      { name: "Phone", price: 800 },
    ],
  },
  clothing: {
    name: "Clothing",
    products: [
      { name: "T-Shirt", price: 25 },
      { name: "Jeans", price: 60 },
    ],
  },
};
function counter() {
  let addBtn = document.getElementById("add-product");
  count += 1;
  if (count >= 3) {
    addBtn.removeEventListener("click", counter);
    addBtn.disabled = true;
    console.log("deleted");
  }
}
function getUserName(event) {
  event.preventDefault();
  let username = document.getElementById("username").value;
  document.cookie = `username=${username}; expires=Tue , 7 July 2030 12:00:00 UTC; path=/`;
  localStorage.setItem("user-setting", JSON.stringify(userSetting));
  let headingOne = document.getElementById("greeting");
  headingOne.textContent = `welcome ${username}`;
}
function smooth() {
  return Object.values(store).flatMap((cat) => cat.products);
}
function getAllPrices() {
  let products = smooth();
  return products.map((product) => product.price);
}
function calculateTotal(...prices) {
  try {
    return prices.reduce((total, price) => total + price, 0);
  } catch (e) {
    console.log(e);
  }
}
function getLastProduct() {
  let products = smooth();
  return products.at(-1);
}
document.addEventListener("DOMContentLoaded", () => {
  let userInfo = document.cookie.split(";");
  let username = "";
  for (let info of userInfo) {
    info = info.trim();
    if (info.startsWith("username=")) {
      username = info.split("=")[1];
    }
  }
  let headingOne = document.getElementById("greeting");
  headingOne.textContent = `welcome ${username}`;
  let products = smooth();
  let list = document.querySelector("ul");
  for (let product of products) {
    let li = document.createElement("li");
    let btn = document.createElement("button");
    li.textContent = `${product.name}: ${product.price}`;
    btn.textContent = `Delete ${product.name}`;
    li.append(btn);
    list.append(li);
  }
  document.body.addEventListener("click", (event) => {
    console.log(event.target);
  });
  list.addEventListener("click", function (event) {
    if (event.target.tagName === "BUTTON") {
      event.target.parentElement.remove();
    } else if (event.target.tagName === "LI") {
      event.target.classList.toggle("green");
    }
  });
  let discountTimer = setTimeout(() => {
    let discount = document.querySelector("#discount");
    discount.textContent = "there is 15% discount on all of products";
  }, 10000);
  let supportTimer = setInterval(() => {
    let admin = document.querySelector("#admin");
    admin.textContent = "پشتیبان سایت آنلاین است";
  }, 300000);
  document.getElementById("del-admin").addEventListener("click", () => {
    clearInterval(supportTimer);
    document.getElementById("admin").textContent = "پشتیبانی متوقف شد";
  });
  document.getElementById("exit").addEventListener("click", () => {
    let products = localStorage.removeItem("user-setting");
    document.cookie = `username=; expires=Tue , 7 July 2000 12:00:00 UTC; path=/`;
    location.reload();
  });
  document.getElementById("add-product").addEventListener("click", counter);
});

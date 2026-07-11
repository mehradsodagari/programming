let container = document.querySelector(".container");
let products;
try {
  products = JSON.parse(localStorage.getItem("products") || "[]");
} catch {
  product = [];
}
function renderProducts(list) {
  container.innerHTML = "";
  if (list.length === 0) {
    container.textContent = "No products found";
    return;
  }
  for (let p of list) {
    let section = document.createElement("section");
    let nameElement = document.createElement("h3");
    nameElement.textContent = p.name;
    section.append(nameElement);
    let priceElement = document.createElement("h4");
    priceElement.textContent = p.price.toLocaleString();
    section.append(priceElement);
    let categoryElement = document.createElement("h4");
    categoryElement.textContent = p.category;
    section.append(categoryElement);
    let dateElement = document.createElement("h4");
    dateElement.textContent = p.createdAtDisplay;
    section.append(dateElement);
    let deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.dataset.id = p.id;
    section.append(deleteButton);
    container.append(section);
  }
}
function searchItem() {
  let search = document.querySelector("#search").value.toLowerCase().trim();
  let items = products.filter((p) => {
    return p.name.toLowerCase().includes(search);
  });
  return items;
}
function sortProducts(productsList) {
  let whichSort = document.querySelector("#sort").value;
  let sorted_products = [...productsList];
  if (whichSort === "lth") {
    sorted_products.sort((a, b) => a.price - b.price);
  } else if (whichSort === "htl") {
    sorted_products.sort((a, b) => b.price - a.price);
  } else if (whichSort === "newest") {
    sorted_products.sort((a, b) => b.createdAt - a.createdAt);
  }
  renderProducts(sorted_products);
}
function handleDelete(event) {
  console.log("target:", event.target);
  console.log("currentTarget:", event.currentTarget);
  if (event.target.dataset.id) {
    let id = event.target.dataset.id;
    products = products.filter((p) => {
      return p.id !== id;
    });
    localStorage.setItem("products", JSON.stringify(products));
    updateView();
  }
}
function deleteItem() {
  container.addEventListener("click", handleDelete);
}
function disabledDelete() {
  container.removeEventListener("click", handleDelete);
  alert("Delete disabled");
}
function updateStats() {
  let product_count = products.length;
  let total_price = products.reduce(
    (total, product) => total + Number(product.price),
    0,
  );
  let average_price =
    product_count !== 0 ? (total_price / product_count).toFixed(2) : 0;
  let prices = [];
  for (let p of products) {
    prices.push(p.price);
  }
  let most_expensive = prices.length > 0 ? Math.max(...prices) : 0;
  let cheapest = prices.length > 0 ? Math.min(...prices) : 0;
  document.querySelector(".total-products").textContent = product_count;
  document.querySelector(".total-price").textContent =
    total_price.toLocaleString();
  document.querySelector(".average-price").textContent = average_price;
  document.querySelector(".most-expensive").textContent = most_expensive;
  document.querySelector(".cheapest").textContent = cheapest;
  return [product_count, total_price, average_price, most_expensive, cheapest];
}
function organize() {
  let electronics = [];
  let books = [];
  let clothes = [];
  let other = [];
  for (let item of products) {
    if (item.category.toLowerCase() === "electronics") {
      electronics.push(item.name);
    } else if (item.category.toLowerCase() === "books") {
      books.push(item.name);
    } else if (item.category.toLowerCase() === "clothes") {
      clothes.push(item.name);
    } else {
      other.push(item.name);
    }
  }
  return { electronics, books, clothes, other };
}
function createIDGenerator() {
  return () => {
    let id = "";
    for (let i = 0; i < 8; i++) {
      let chars = "abcdefghijklmnopqrstuvwxyz0123456789";
      id += chars[Math.floor(Math.random() * chars.length)];
    }
    return id;
  };
}
let generateID = createIDGenerator();
function updateView() {
  let filtered = searchItem();
  sortProducts(filtered);
  updateStats();
}
let form = document.querySelector("form");
form.addEventListener("submit", (event) => {
  let product = {
    id: "",
    name: "",
    price: "",
    category: "",
    description: "",
    createdAt: new Date().getTime(),
    createdAtDisplay: new Intl.DateTimeFormat("fa-IR-u-ca-persian", {
      year: "numeric",
      month: "numeric",
      day: "numeric",
      hour: "numeric",
      minute: "numeric",
      second: "numeric",
    }).format(new Date()),
  };
  event.preventDefault();
  let product_name = document.querySelector("#name").value.trim();
  product.name = product_name;
  let product_price = Number(document.querySelector("#price").value);
  product.price = product_price;
  let product_category = document.querySelector("#category").value.trim();
  product.category = product_category;
  let product_description = document.querySelector("#describe").value;
  product.description = product_description;
  if (
    !product_name ||
    product_price <= 0 ||
    isNaN(product_price) ||
    !product_category
  ) {
    alert("name and price and category required");
    return;
  }
  let newID;
  do {
    newID = generateID();
  } while (products.some((p) => p.id === newID));
  product.id = newID;
  products.push(product);
  localStorage.setItem("products", JSON.stringify(products));
  console.log(product);
  console.log(products);
  console.log(organize());
  updateView();
  event.target.reset();
});
document.querySelector("#search").addEventListener("keyup", () => {
  updateView();
});
deleteItem();
document.querySelector("#sort").addEventListener("change", () => {
  updateView();
});
document.querySelector("#reload-page").addEventListener("click", () => {
  location.reload();
});
document.querySelector("#disabled-delete").addEventListener("click", () => {
  disabledDelete();
});
updateView();

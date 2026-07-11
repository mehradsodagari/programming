const orders = [
  "Ali,coffee,2,250",
  "Sara,tea,1,100",
  "Reza,cake,3,180",
  "Mina,coffee,1,250",
  " ,tea,2,100",
  "Nima,juice,two,120",
  "Parsa,sandwich,1,300",
  "Elham,coffee,4,250",
  "Roya,cake,0,180",
  "Amir,tea,2,100",
  "Hani,water,1,50",
  "Sam,coffee,3,250",
];
function parseOrder(order) {
  let order_details = order.split(",");
  let name = order_details[0].trim();
  let item = order_details[1].trim();
  let count = order_details[2].trim();
  count = Number(count);
  let price = order_details[3].trim();
  price = Number(price);
  const data = {
    Name: name,
    Item: item,
    Count: count,
    Price: price,
  };
  return data;
}
function isValidorder(order_data) {
  if (
    order_data.Name !== "" &&
    order_data.Item &&
    !isNaN(order_data.Count) &&
    !isNaN(order_data.Price) &&
    order_data.Count > 0 &&
    order_data.Price > 0
  ) {
    return true;
  }
  return false;
}
function validOrInvalid(orders_list) {
  let validOrders = [];
  let invalidOrders = [];
  for (let i = 0; i < orders_list.length; i++) {
    let data = parseOrder(orders_list[i]);
    isValidorder(data)
      ? validOrders.push(orders_list[i])
      : invalidOrders.push(orders_list[i]);
  }
  return {
    Valid: validOrders,
    Invalid: invalidOrders,
  };
}
const valid_orders_list = validOrInvalid(orders).Valid;
const invalid_orders_list = validOrInvalid(orders).Invalid;
// const result = validOrInvalid(orders);
// const valid_orders_list = result.Valid;
// const invalid_orders_list = result.Invalid;
function calcTotal(list) {
  return list.map(function (order) {
    let data = parseOrder(order);
    order = order + "," + Number(data.Count * data.Price);
    return order;
  });
}
function makeReport(order) {
  let data = parseOrder(order);
  return `${data.Name} ordered ${data.Count} ${data.Item}(s). Total : ${data.Count * data.Price}`;
}
const reports = valid_orders_list.map(function (order) {
  let data = parseOrder(order);
  return `${data.Name} ordered ${data.Count} ${data.Item}(s). Total : ${data.Count * data.Price}`;
});
const coffeeOrders = valid_orders_list.filter(function (order) {
  return parseOrder(order).Item.toLowerCase() === "coffee";
});
const expensiveOrders = valid_orders_list.filter(function (order) {
  return parseOrder(order).Count * parseOrder(order).Price > 500;
});
const firstTea = orders.find((item) => item.toLowerCase().includes("tea"));
const firstMina = orders.find((name) => name.includes("Mina"));
function totalRevenue(orders_list) {
  let sum = 0;
  for (i in orders_list) {
    sum += parseOrder(orders_list[i]).Count * parseOrder(orders_list[i]).Price;
  }
  return sum;
}
function getDiscountTotal(order) {
  let data = parseOrder(order);
  if (data.Item === "coffee" && data.Count > 3) {
    return data.Count * data.Price * 0.9;
  } else if (data.Item === "tea" && data.Count >= 2) {
    return data.Count * data.Price * 0.95;
  } else {
    return data.Count * data.Price;
  }
}
function calcOrderTotal(order) {
  let data = parseOrder(order);
  return data.Count * data.Price;
}
const status = calcOrderTotal(orders[0]) > 500 ? "expensive" : "normal";
console.log(Boolean(""));
console.log(Boolean("Ali"));
console.log(Boolean(0));
console.log(Boolean(10));
console.log(Boolean([]));
console.log(Boolean({}));
console.log(Boolean(NaN));

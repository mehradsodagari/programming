class Plant {
  constructor(id, name, Type, WateringIntervalDays, LastWateredDate) {
    this.id = id;
      this.name = name;
      this.type = Type;
      this.wateringIntervalDays = Number(WateringIntervalDays);
      this.lastWateredDate = new Date(LastWateredDate);
  }
  water() {
    this.lastWateredDate = new Date();
  }
  get getDaysUntilNextWatering() {
    let lastWateredDateMS = this.wateringIntervalDays*24*60*60*1000
    let nextWatering = lastWateredDateMS + this.lastWateredDate.getTime();
    let today = new Date()
    let differenceMS = nextWatering - today.getTime();
    let getDaysBetween = Math.floor(differenceMS / (24 * 60 * 60 * 1000));
    return getDaysBetween;
  }
  get isThirsty() {
    let differenceDays = this.getDaysUntilNextWatering;
    if (differenceDays <= 0) {
      return true;
    }
    return false;
  }
  get name() {
    return this._name
  }
  set name(newName) {
    if(newName && newName.trim().length>0) {
      this._name = newName
    }
    else {
      throw new Error("name cannot be empty")
    }
  }
}
let plants = (JSON.parse(localStorage.getItem("plants")) || []).map(item => new Plant(item.id,item.name,item.type,item.wateringIntervalDays,item.lastWateredDate))
let idCounter = JSON.parse(localStorage.getItem("id-counter")) || 0
function getInformation(event) {
    event.preventDefault()
    let formData = new FormData(event.target)
    let name = formData.get("name")
    let type = formData.get("type")
    let wateringIntervalDays = formData.get("day")
    let lastWateredDate = formData.get("last")
    let interval = Number(wateringIntervalDays)
    try {
      if(isNaN(interval) || interval<=0) {
        throw new Error("range of watering must be positive")
      }
      interval = Math.trunc(interval)
      let plant = new Plant(idCounter,name,type,interval,lastWateredDate)
      plants.push(plant)
      idCounter++
      event.target.reset()
      localStorage.setItem("plants",JSON.stringify(plants))
      localStorage.setItem("id-counter",JSON.stringify(idCounter))
      hydrate()
    }
    catch (error) {
      alert(error.message)
    }
}
function hydrate() {
    let container = document.getElementById("container")
    container.innerHTML = ""
    for(let plant of plants) {
        let plantID = plant.id
        let plantName = plant.name
        let plantType = plant.type
        let plantWateringIntervalDays = plant.wateringIntervalDays
        let plantLastWateredDate = plant.lastWateredDate
        let card = document.createElement("div")
        let name = document.createElement("p")
        let type = document.createElement("p")
        let wateringIntervalDays = document.createElement("p")
        let lastWateredDate = document.createElement("p")
        let id = document.createElement("p")
        let howManyDays = document.createElement("p")
        let watered = document.createElement("button")
        name.textContent = plant.name
        type.textContent = plant.type
        id.textContent = plant.id
        wateringIntervalDays.textContent = plant.wateringIntervalDays
        lastWateredDate.textContent = plant.lastWateredDate.toDateString()
        howManyDays.textContent = plant.getDaysUntilNextWatering
        watered.textContent = "Water"
        watered.onclick = function() {
            plant.water(); 
            localStorage.setItem("plants", JSON.stringify(plants)); 
            hydrate(); 
        };
        card.append(name,type,wateringIntervalDays,lastWateredDate,id,howManyDays,watered)
        container.appendChild(card)
        if(plant.isThirsty) {
            card.classList.add("thirsty")
        }
    }
}
document.addEventListener("DOMContentLoaded",() => {
  let form = document.querySelector("form")
  if(form) {
    form.addEventListener("submit",getInformation)
  }
  hydrate()
})
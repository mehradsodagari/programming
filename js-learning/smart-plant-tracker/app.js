let plants = JSON.parse(localStorage.getItem("plants")) || []
let idCounter = JSON.parse(localStorage.getItem("id-counter")) || 0
class Plant {
  constructor(id, Name, Type, WateringIntervalDays, LastWateredDate) {
    this.id = id;
      this.name = Name;
      this.type = Type;
      this.wateringIntervalDays = Number(WateringIntervalDays);
      this.lastWateredDate = new Date(LastWateredDate);
  }
  water() {
    this.lastWateredDate = new Date();
  }
  getDaysUntilNextWatering() {
    let lastWateredDateMS = this.wateringIntervalDays*24*60*60*1000
    let nextWatering = lastWateredDateMS + this.lastWateredDate.getTime();
    let today = new Date()
    let differenceMS = nextWatering - today.getTime();
    let getDaysBetween = Math.floor(differenceMS / (24 * 60 * 60 * 1000));
    return getDaysBetween;
  }
  isThirsty() {
    let differenceDays = this.getDaysUntilNextWatering();
    if (differenceDays <= 0) {
      return true;
    }
    return false;
  }
}
function getInformation(event) {
    event.preventDefault()
    let name = document.getElementById("name").value
    let type = document.getElementById("type").value
    let wateringIntervalDays = document.getElementById("day").value
    let lastWateredDate = document.getElementById("last").value
    let plant = new Plant(idCounter,name,type,wateringIntervalDays,lastWateredDate)
    plants.push(plant)
    idCounter++
    event.target.reset()
    localStorage.setItem("plants",JSON.stringify(plants))
    localStorage.setItem("id-counter",JSON.stringify(idCounter))
    hydrate()
}
function hydrate() {
    let newPlants = []
    let container = document.getElementById("container")
    container.innerHTML = ""
    for(let plant of plants) {
        let plantID = plant.id
        let plantName = plant.name
        let plantType = plant.type
        let plantWateringIntervalDays = plant.wateringIntervalDays
        let plantLastWateredDate = plant.lastWateredDate
        plant = new Plant(plantID,plantName,plantType,plantWateringIntervalDays,plantLastWateredDate)
        let card = document.createElement("div")
        let name = document.createElement("p")
        let type = document.createElement("p")
        let wateringIntervalDays = document.createElement("p")
        let lastWateredDate = document.createElement("p")
        let id = document.createElement("p")
        let howManyDays = document.createElement("p")
        let watered = document.createElement("button")
        newPlants.push(plant)
        name.textContent = plant.name
        type.textContent = plant.type
        wateringIntervalDays.textContent = plant.name
        lastWateredDate.textContent = plant.lastWateredDate.toDateString()
        howManyDays.textContent = plant.getDaysUntilNextWatering()
        watered.textContent = "Water"
        watered.onclick = function() {
            plant.water(); 
            localStorage.setItem("plants", JSON.stringify(newPlants)); 
            hydrate(); 
        };
        card.append(name,type,wateringIntervalDays,lastWateredDate,id,howManyDays,watered)
        container.appendChild(card)
        if(plant.isThirsty()) {
            card.classList.add("thirsty")
        }
    }
    plants = [...newPlants]
}
hydrate()
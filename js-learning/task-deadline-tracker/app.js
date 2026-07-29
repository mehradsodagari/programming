class Task {
  constructor(id, title, createdAt, deadline) {
    this.id = id;
      this.title = title;
      this.createdAt = new Date(createdAt);
      this.deadline = new Date(deadline);
  }
  set title(Title) {
    if (Title.trim().length < 3) {
      throw new Error("The title should be at least three characters");
    }
    this._title = Title.trim();
  }
  get title() {
    return this._title
  }
  get remainingDays() {
    let now = new Date().getTime();
    let deadlineMS = this.deadline.getTime();
    let differenceDays = (deadlineMS - now) / (24 * 60 * 60 * 1000);
    return Math.ceil(differenceDays);
  }
  get isOverdue() {
    return this.remainingDays < 0;
  }
  extendDeadline(extendDays) {
    this.deadline.setDate(this.deadline.getDate() + Number(extendDays));
  }
}
let tasks = (JSON.parse(localStorage.getItem("tasks")) || []).map(task => new Task(task.id,task.title,task.createdAt,task.deadline))
let idCounter = JSON.parse(localStorage.getItem("id-counter")) || 0
idCounter = Math.max(0, ...tasks.map(t => t.id)) + 1;
function createTask(event) {
    event.preventDefault()
    try{
    let titleValue = document.getElementById("title").value
    let deadlineValue = document.getElementById("deadline").value
    if(!deadlineValue) {
        throw new Error("please select a deadline date")
    }
    let task = new Task(idCounter++,titleValue,new Date(),deadlineValue)
    tasks.push(task)
    localStorage.setItem("tasks",JSON.stringify(tasks))
    localStorage.setItem("id-counter",JSON.stringify(idCounter))
    event.target.reset()
    render()} catch(error) {
        alert(error.message)
    }
}
function render() {
    let container = document.getElementById("container")
    container.innerHTML = ""
    for(let task of tasks) {
        let taskContainer = document.createElement("div")
        let taskID = document.createElement("p")
        let taskTitle = document.createElement("p")
        let taskCreatedAt = document.createElement("p")
        let taskDeadline = document.createElement("p")
        let buttonThreeDays = document.createElement("button")
        let buttonWeek = document.createElement("button")
        let buttonFortnight = document.createElement("button")
        taskID.textContent = task.id
        taskTitle.textContent = task.title
        taskCreatedAt.textContent = task.createdAt.toDateString()
        taskDeadline.textContent = task.deadline.toDateString()
        buttonThreeDays.textContent = "Add Three Days"
        buttonWeek.textContent = "Add a Week"
        buttonFortnight.textContent = "Add Two Weeks"
        taskContainer.classList.add("task-item")
        taskContainer.dataset.id = task.id
        buttonThreeDays.dataset.action = "extend-3"
        buttonWeek.dataset.action = "extend-7"
        buttonFortnight.dataset.action = "extend-14"
        taskContainer.appendChild(taskID)
        taskContainer.appendChild(taskTitle)
        taskContainer.appendChild(taskCreatedAt)
        taskContainer.appendChild(taskDeadline)
        taskContainer.appendChild(buttonThreeDays)
        taskContainer.appendChild(buttonWeek)
        taskContainer.appendChild(buttonFortnight)
        container.append(taskContainer)
    }
}
document.addEventListener("DOMContentLoaded",() => {
    render()
    document.querySelector("form").addEventListener("submit",createTask)
    document.getElementById("container").addEventListener("click",(event) => {
        let card = event.target.closest(".task-item")
        if(!card) return
        let taskId = Number(card.dataset.id)
        let action = event.target.dataset.action
        if(!action) return
        let task = tasks.find(t => t.id===taskId)
        if (task && action) {
            if (action === "extend-3") task.extendDeadline(3)
            if (action === "extend-7") task.extendDeadline(7)
            if (action === "extend-14") task.extendDeadline(14)
            localStorage.setItem("tasks",JSON.stringify(tasks))
            render()
        }
    })
})

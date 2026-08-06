let idCount = JSON.parse(localStorage.getItem("id-count")) || 0
class Task {
    constructor(id,title,status="todo",priority="medium",createdAt = new Date()) {
        this.id = id;
        this.title = title;
        this.status = status;
        this.priority = priority;
        this.createdAt = new Date(createdAt)
    }
    updateStatus(newStatus) {
        this.status = newStatus
    }
    updateTitle(newTitle) {
        if(newTitle.trim().length>0) {
            this.title = newTitle.trim()
            return
        }
        throw new Error("Title is empty")
    }
}
class TaskManager{
    constructor() {
        this.tasks = (this.loadFromLocalStorage() || []).map(task => new Task(task.id,task.title,task.status,task.priority,task.createdAt))
    }
    addTask(title,status="todo",priority="medium") {
        const task = new Task(idCount++,title,status,priority)
        localStorage.setItem("id-count",JSON.stringify(idCount))
        this.tasks.push(task)
        this.saveToLocalStorage()
        return
    }
    deleteTask(id) {
        this.tasks = this.tasks.filter(task => task.id!==id)
        this.saveToLocalStorage()
    }
    getTaskById(id) {
        for(let task of this.tasks) {
            if(task.id===id) {
                return task
            }
        }
        return 
    }
    saveToLocalStorage() {
        try {
            localStorage.setItem("tasks",JSON.stringify(this.tasks))
        }
        catch(error) {
            alert(error.message)
        }
    }
    loadFromLocalStorage() {
        try{
            return JSON.parse(localStorage.getItem("tasks"))
        }
        catch(error) {
            alert(error.message)
        }
    }
    updateTaskStatus(id,newStatus) {
        const task = this.getTaskById(id)
        if(task) {
            task.updateStatus(newStatus)
            this.saveToLocalStorage()
        }
    }
    updateTaskTitle(id,newTitle) {
        const task = this.getTaskById(id)
        if(task) {
            task.updateTitle(newTitle)
            this.saveToLocalStorage()
        }
    }
}
class UIManager {
    constructor() {
        this.manager = new TaskManager()
    }
    render() {
        const todo = document.querySelector(".todo-column-container")
        const progress = document.querySelector(".in-progress-column-container")
        const done = document.querySelector(".done-column-container")
        todo.innerHTML = ""
        progress.innerHTML = ""
        done.innerHTML = ""
        for(let task of this.manager.tasks) {
            const container = document.createElement("div")
            const title = document.createElement("p")
            const delBtn = document.createElement("button")
            delBtn.textContent = "Delete"
            delBtn.dataset.id = task.id
            delBtn.classList.add("delete-btn")
            const editBtn = document.createElement("button")
            editBtn.textContent = "Edit"
            editBtn.dataset.id = task.id
            editBtn.classList.add("edit-btn")
            const priority = document.createElement("p")
            const date = document.createElement("p")
            title.textContent = `Title : ${task.title}`
            priority.textContent = `Priority : ${task.priority}`
            date.textContent = `Created At : ${task.createdAt.toDateString()}`
            container.appendChild(title)
            container.appendChild(priority)
            container.appendChild(date)
            container.appendChild(delBtn)
            container.appendChild(editBtn)
            if(task.status === "todo") {
                const moveNext = document.createElement("button")
                moveNext.textContent = "Move to Progress"
                moveNext.dataset.id = task.id
                moveNext.dataset.targetStatus = "progress"
                moveNext.classList.add("move-btn")
                container.appendChild(moveNext)
                todo.appendChild(container)
            }
            else if(task.status === "progress") {
                const moveNext = document.createElement("button")
                moveNext.textContent = "Move to Done"
                moveNext.dataset.id = task.id
                moveNext.dataset.targetStatus = "done"
                moveNext.classList.add("move-btn")
                const movePrevious = document.createElement("button")
                movePrevious.textContent = "Move to ToDo"
                movePrevious.dataset.id = task.id
                movePrevious.dataset.targetStatus = "todo"
                movePrevious.classList.add("move-btn")
                container.appendChild(moveNext)
                container.appendChild(movePrevious)
                progress.appendChild(container)
            }
            else if(task.status === "done") {
                const movePrevious = document.createElement("button")
                movePrevious.textContent = "Move to Progress"
                movePrevious.dataset.id = task.id
                movePrevious.dataset.targetStatus = "progress"
                movePrevious.classList.add("move-btn")
                container.appendChild(movePrevious)
                done.appendChild(container)
            }
        }
    }
    createTask() {
        const title = document.getElementById("title").value.trim()
        if(title.length===0) {
            alert("title is empty")
            return false
        }
        const status = document.getElementById("stat").value
        if(status==="status") {
            alert("choose status")
            return false
        }
        const priority = document.getElementById("pri").value
        if(priority==="priority") {
            alert("choose priority")
            return false
        }
        this.manager.addTask(title,status,priority)
        this.render()
        return true
    }
}
document.addEventListener("DOMContentLoaded",() => {
    const view = new UIManager() 
    view.render()
    document.querySelector("form").addEventListener("submit",(event) => {
        event.preventDefault()
        const isCreated = view.createTask()
        if(isCreated) {
            event.currentTarget.reset()
        }
    })
    document.querySelector(".board").addEventListener("click",(event) => {
        if(event.target.classList.contains("delete-btn")) {
            const taskId = Number(event.target.dataset.id)
            view.manager.deleteTask(taskId)
            view.render()
            return 
        }
         if(event.target.classList.contains("move-btn")) {
             const taskId = Number(event.target.dataset.id)
             const taskStatus = event.target.dataset.targetStatus
             view.manager.updateTaskStatus(taskId,taskStatus)
             view.render()
             return
            }
            if(event.target.classList.contains("edit-btn")) {
                const taskId = Number(event.target.dataset.id)
                const task = view.manager.getTaskById(taskId)
                if(!task) {
                    return
                }
                const newTitle = prompt("Enter new title:",task.title)
                if(newTitle===null) {
                    return
                }
                try {
                    view.manager.updateTaskTitle(taskId,newTitle)
                    view.render()
                }
                catch(error) {
                    alert(error.message)
                }
            return
        }
    })
})

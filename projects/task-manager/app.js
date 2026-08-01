let idCount = JSON.parse(localStorage.getItem("id-count")) || 0
class Task {
    constructor(id,title,status="todo",priority="medium",createdAt = new Date()) {
        this.id = id;
        this.title = title;
        this.status = status;
        this.priority = priority;
        this.createdAt = new Date(createdAt)
    }
    toggleStatus(newStatus) {
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
    addTask(title,status="todo",priority) {
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
        localStorage.setItem("tasks",JSON.stringify(this.tasks))
    }
    loadFromLocalStorage() {
        return JSON.parse(localStorage.getItem("tasks"))
    }
}

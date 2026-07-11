let testArray = ["mehrad",1,4,32,45,"hi"]
const push = (list,item) => {
    let newArray = [item]
    for (let i=0;i<list.length;i++) {
        newArray[i+1]=list[i]
    }
    return newArray
}
const pull = (list) => {
    let newArray = []
    for (let i=0;i<list.length-1;i++) {
        newArray[i]=list[i]
    }
    return newArray
}
console.log(push(testArray,"koori"))
console.log(pull(testArray))
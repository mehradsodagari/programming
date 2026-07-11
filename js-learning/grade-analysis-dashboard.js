var rowData = [18, "15", "absent", 11, 20, "9", 14, "fail", 19, "12"]
function cleanData(scores) {
    var new_scores = []
    for (index in scores) {
        if (scores[index]!="fail" && scores[index]!="absent") {
            new_scores.push(Number(scores[index]))
        }
    }
    return new_scores
}
var new_scores_array = cleanData(rowData)
console.log(new_scores_array)
function analizeData(grades) {
    var count=0
    var sum = 0
    var max = grades[0]
    var min = grades[0]
    var pass = 0
    for(grade in grades) {
        sum+=Number(grades[grade])
        if (grades[grade]>max) {
            max = grades[grade]
        }
        if (grades[grade]<min) {
            min = grades[grade]
        }
        if (grades[grade]>=10) {
            pass+=1
        }
        count+=1
    }
    average = sum/count
    return [sum,average,max,min,pass]
}
function classifyGrades(grades) {
    var organized = {
        excellent:[],
        good:[],
        pass:[],
        fail:[]
    }
    for (grade in grades) {
        if (18<=Number(grades[grade]) && Number(grades[grade])<=20) {
            organized["excellent"].push(Number(grades[grade]))
        }
        else if (15<=Number(grades[grade]) && Number(grades[grade])<=17) {
            organized["good"].push(Number(grades[grade]))
        }
        else if (10<=Number(grades[grade]) && Number(grades[grade])<=14) {
            organized["pass"].push(Number(grades[grade]))
        }
        else {
            organized["fail"].push(grades[grade])
        }
    }
    return organized
}
function print(data) {
    console.log(" --- Students Report --- ")
    console.log("-------------------")
    console.log(`Excellent count : ${data["excellent"].length}`)
    var stats = analizeData(data["excellent"]);
    console.log(`Average : ${stats[1]}`);
    console.log("-------------------")
    console.log(`Good count : ${data["good"].length}`)
    var stats = analizeData(data["good"]);
    console.log(`Average : ${stats[1]}`);
    console.log("-------------------")
    console.log(`pass count : ${data["pass"].length}`)
    var stats = analizeData(data["pass"]);
    console.log(`Average : ${stats[1]}`);
    console.log("-------------------")
    console.log(`Fail count : ${data["fail"].length}`)
    var stats = analizeData(data["fail"]);
    console.log(`Average : ${stats[1]}`);
}
print(classifyGrades(new_scores_array))
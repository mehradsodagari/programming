const students = [
  "  ali, 18, javascript  ",
  "sara,17,python",
  "  reza, twenty, Java ",
  "mina, 19, javascript",
  " , 20, c++ ",
  "nima,16,python",
  "elham, 21, JavaScript ",
  "parsa,NaN,go",
  "roya, 18,  javascript",
  "amir,15,python"
]
function parseStudent(info) {
    info=info.trim()
    let parts=info.split(",")
    let name=parts[0].trim().toLowerCase()
    let age=Number(parts[1].trim())
    let course=parts[2].trim().toLowerCase()
    let data = {
        Name: name,
        Age: age,
        Course: course
    }
    return data
}
function isValidStudent(student) {
    return student.Name.length > 0 && !isNaN(student.Age) && student.Course.length > 0
}
console.log(`student 1 is valid : ${isValidStudent(parseStudent(students[0]))}`)
console.log(`student 2 is valid : ${isValidStudent(parseStudent(students[1]))}`)
console.log(`student 3 is valid : ${isValidStudent(parseStudent(students[2]))}`)
console.log(`student 4 is valid : ${isValidStudent(parseStudent(students[3]))}`)
console.log(`student 5 is valid : ${isValidStudent(parseStudent(students[4]))}`)
console.log(`student 6 is valid : ${isValidStudent(parseStudent(students[5]))}`)
console.log(`student 7 is valid : ${isValidStudent(parseStudent(students[6]))}`)
console.log(`student 8 is valid : ${isValidStudent(parseStudent(students[7]))}`)
console.log(`student 9 is valid : ${isValidStudent(parseStudent(students[8]))}`)
console.log(`student 10 is valid : ${isValidStudent(parseStudent(students[9]))}`)
function countValidStudent(list) {
    let situations = []
    situations.push(isValidStudent(parseStudent(list[0])))
    situations.push(isValidStudent(parseStudent(list[1])))
    situations.push(isValidStudent(parseStudent(list[2])))
    situations.push(isValidStudent(parseStudent(list[3])))
    situations.push(isValidStudent(parseStudent(list[4])))
    situations.push(isValidStudent(parseStudent(list[5])))
    situations.push(isValidStudent(parseStudent(list[6])))
    situations.push(isValidStudent(parseStudent(list[7])))
    situations.push(isValidStudent(parseStudent(list[8])))
    situations.push(isValidStudent(parseStudent(list[9])))
    return situations
}
console.log(countValidStudent(students))
function studentReport(students_list) {
    console.log(`${parseStudent(students_list[0]).Name} is ${parseStudent(students_list[0]).Age}  years old and studies ${parseStudent(students_list[0]).Course} .`)
    console.log(`${parseStudent(students_list[1]).Name} is ${parseStudent(students_list[1]).Age}  years old and studies ${parseStudent(students_list[1]).Course} .`)
    console.log(`${parseStudent(students_list[2]).Name} is ${parseStudent(students_list[2]).Age}  years old and studies ${parseStudent(students_list[2]).Course} .`)
    console.log(`${parseStudent(students_list[3]).Name} is ${parseStudent(students_list[3]).Age}  years old and studies ${parseStudent(students_list[3]).Course} .`)
    console.log(`${parseStudent(students_list[4]).Name} is ${parseStudent(students_list[4]).Age}  years old and studies ${parseStudent(students_list[4]).Course} .`)
    console.log(`${parseStudent(students_list[5]).Name} is ${parseStudent(students_list[5]).Age}  years old and studies ${parseStudent(students_list[5]).Course} .`)
    console.log(`${parseStudent(students_list[6]).Name} is ${parseStudent(students_list[6]).Age}  years old and studies ${parseStudent(students_list[6]).Course} .`)
    console.log(`${parseStudent(students_list[7]).Name} is ${parseStudent(students_list[7]).Age}  years old and studies ${parseStudent(students_list[7]).Course} .`)
    console.log(`${parseStudent(students_list[8]).Name} is ${parseStudent(students_list[8]).Age}  years old and studies ${parseStudent(students_list[8]).Course} .`)
    console.log(`${parseStudent(students_list[9]).Name} is ${parseStudent(students_list[9]).Age}  years old and studies ${parseStudent(students_list[9]).Course} .`)
}
studentReport(students)
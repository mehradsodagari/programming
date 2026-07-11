const students = [
  "Ali,Math,18",
  "Sara,Math,15",
  "Reza,Math,9",
  "Mina,Math,20",
  "Nima,Math,12",
  "Parsa,Math,7",
  "Elham,Math,17",
  "Roya,Math,14",
  "Amir,Math,19",
  "Hani,Math,11",
];
const parseStudent = (student) => {
  let data = student.split(",");
  let name = data[0];
  let course = data[1];
  let grade = data[2];
  grade = Number(grade);
  return {
    Name: name,
    Course: course,
    Grade: grade,
  };
};
const makeReport = (list) => {
  for (student in list) {
    let data = parseStudent(list[student]);
    console.log(`${data.Name} got ${data.Grade} in ${data.Course}`);
  }
};
let fails = students.filter(function (student) {
  return parseStudent(student).Grade < 10;
});
let excellent = students.filter(function (student) {
  return parseStudent(student).Grade >= 18;
});
const separate = (list) => {
  let new_list = [];
  for (let item of list) {
    let student = parseStudent(item);
    new_list.push(student.Name);
  }
  return new_list;
};
let first_twenty = students.find(
  (student) => parseStudent(student).Grade === 20,
);
makeReport(students);
function averageGrade(list) {
  let sum = 0;
  list.forEach((student) => {
    sum += parseStudent(student).Grade;
  });
  return sum / list.length;
}
let grades = students.map((student) => parseStudent(student).Grade);
grades = grades.sort((a, b) => b - a);
const gradeStatus = function (list) {
  for (let i = 0; i < list.length; i++) {
    let student = parseStudent(list[i]);
    let grade = student.Grade;
    let name = student.Name;
    switch (true) {
      case grade >= 18:
        console.log(`${name} got excellent grade`);
        break;
      case grade >= 15:
        console.log(`${name} got good grade`);
        break;
      case grade >= 12:
        console.log(`${name} got normal grade`);
        break;
      case grade >= 10:
        console.log(`${name} got pass grade`);
        break;
      default:
        console.log(`${name} got fail grade`);
        break;
    }
  }
};
const under_five = (list) => {
  for (let grade of list) {
    if (grade < 5) {
      return true;
    }
  }
  return false;
};
const every_pass = (list) => {
  for (let grade of list) {
    if (grade < 10) {
      return false;
    }
  }
  return true;
};
console.log("-------------");
console.log("failed students : ", separate(fails));
console.log("-------------");
console.log("how many students failed : ", fails.length);
console.log("-------------");
console.log("excellent students : ", separate(excellent));
console.log("-------------");
console.log("how many students excellent : ", excellent.length);
console.log("-------------");
console.log("first student with 20 : ", parseStudent(first_twenty).Name);
console.log("-------------");
console.log("average grade : ", averageGrade(students));
console.log("-------------");
console.log("lowest grade : ", grades[grades.length - 1]);
console.log("-------------");
console.log("highest grade : ", grades[0]);
console.log("-------------");
console.log(grades);
console.log("-------------");
console.log("status of each student :");
gradeStatus(students);
console.log("are there grade under 5 : ", under_five(grades));
console.log("do every one passed  : ", every_pass(grades));

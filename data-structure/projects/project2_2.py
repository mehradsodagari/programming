from project2_1 import Doubly_linkedList


class Student:
    def __init__(self, name, lastname, id, student_number, field_of_study, gpa):
        self.name = name
        self.lastname = lastname
        self.id = id
        self.student_number = student_number
        self.field_of_study = field_of_study
        self.gpa = gpa


class Major:
    def __init__(self, name, professor_count, physical_space):
        self.name = name
        self.professor_count = professor_count
        self.physical_space = physical_space
        self.students = Doubly_linkedList()


class University:
    def __init__(self):
        self.majors = Doubly_linkedList()
        self.major_dict = {}

    def add_major(self, field_name, professor_count, physical_space):
        new_major = Major(field_name, professor_count, physical_space)
        self.major_dict[field_name] = new_major
        return self.majors.inserting_at_the_end(new_major)

    def find_major(self, field_name):
        return self.major_dict.get(field_name)

    def _is_student_number_duplicate(self, student_number):
        current_major = self.majors.head
        while current_major is not None:
            current_student = current_major.data.students.head
            while current_student is not None:
                if current_student.data.student_number == student_number:
                    return True
                current_student = current_student.next
            current_major = current_major.next
        return False

    def add_student(self, name, lastname, id, student_number, field_of_study, gpa):
        major = self.find_major(field_of_study)
        if major is not None:
            if self._is_student_number_duplicate(student_number):
                print(f"Student number {student_number} already exists")
                return None
            new_student = Student(
                name, lastname, id, student_number, field_of_study, gpa
            )
            return major.students.inserting_at_the_end(new_student)
        print(f"Field of study {field_of_study} not found")
        return None

    def total_student(self):
        total = 0
        current_major = self.majors.head
        while current_major is not None:
            current_student = current_major.data.students.head
            while current_student is not None:
                total += 1
                current_student = current_student.next
            current_major = current_major.next
        return total

    def top_three_student_per_major(self):
        result = {}
        current_major = self.majors.head
        while current_major is not None:
            current_student = current_major.data.students.head
            students = []
            while current_student is not None:
                students.append(current_student.data)
                current_student = current_student.next
            top_three_students = sorted(
                students, key=lambda student: student.gpa, reverse=True
            )[:3]
            result[current_major.data.name] = top_three_students
            current_major = current_major.next
        return result

    def average_gpa_per_major(self):
        result = {}
        current_major = self.majors.head
        while current_major is not None:
            total_gpa = 0
            count = 0
            current_student = current_major.data.students.head
            while current_student is not None:
                total_gpa += current_student.data.gpa
                count += 1
                current_student = current_student.next
            if count == 0:
                average_gpa = 0
            else:
                average_gpa = total_gpa / count
            result[current_major.data.name] = round(average_gpa, 2)
            current_major = current_major.next
        return result

    def professor_to_student_ratio(self):
        result = {}
        current_major = self.majors.head
        while current_major is not None:
            count = 0
            current_student = current_major.data.students.head
            while current_student is not None:
                count += 1
                current_student = current_student.next
            if count == 0:
                rate = 0
            else:
                rate = current_major.data.professor_count / count
            result[current_major.data.name] = round(rate, 2)
            current_major = current_major.next
        return result

    def space_to_student_ratio(self):
        result = {}
        current_major = self.majors.head
        while current_major is not None:
            count = 0
            current_student = current_major.data.students.head
            while current_student is not None:
                count += 1
                current_student = current_student.next
            if count == 0:
                rate = 0
            else:
                rate = current_major.data.physical_space / count
            result[current_major.data.name] = round(rate, 2)
            current_major = current_major.next
        return result

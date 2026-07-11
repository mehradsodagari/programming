import csv
from project2_2 import University
from project2_1 import Doubly_linkedList


class FileManager:
    def __init__(self, university):
        self.university = university

    def load_students_from_csv(self, file_name):
        try:
            current_major = self.university.majors.head
            while current_major is not None:
                current_major.data.students = Doubly_linkedList()
                current_major = current_major.next
            with open(file_name, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    if len(row) < 6:
                        continue
                    name = row[0]
                    lastname = row[1]
                    id = row[2]
                    student_number = row[3]
                    field_of_study = row[4]
                    gpa = float(row[5])
                    self.university.add_student(
                        name, lastname, id, student_number, field_of_study, gpa
                    )
        except FileNotFoundError:
            print(f"Error: File {file_name} not found")
        except Exception as e:
            print(f"Error reading file: {e}")

    def save_students_to_csv(self, file_name):
        with open(file_name, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(
                ["name", "lastname", "id", "student number", "field of study", "gpa"]
            )
            current_major = self.university.majors.head
            while current_major is not None:
                current_student = current_major.data.students.head
                while current_student is not None:
                    student = current_student.data
                    writer.writerow(
                        [
                            student.name,
                            student.lastname,
                            student.id,
                            student.student_number,
                            student.field_of_study,
                            student.gpa,
                        ]
                    )
                    current_student = current_student.next
                current_major = current_major.next

    def add_student_to_file(
        self, name, lastname, id, student_number, field_of_study, gpa, file_address
    ):
        new_student = {
            "name": name,
            "lastname": lastname,
            "id": id,
            "student number": student_number,
            "field of study": field_of_study,
            "gpa": float(gpa),
        }
        with open(file_address, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(new_student.values())

    def remove_student_from_file(self, student_number, file_address):
        with open(file_address, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            lines = list(reader)
        header = lines[0]
        data_lines = lines[1:]
        new_lines = [header]
        for line in data_lines:
            if line[3] != student_number:
                new_lines.append(line)
        with open(file_address, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(new_lines)

    def update_student_in_file(self, student_number, new_data, file_address):
        with open(file_address, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            lines = list(reader)
        header = lines[0]
        data_lines = lines[1:]
        new_lines = [header]
        for line in data_lines:
            if line[3] == student_number:
                line[0] = new_data["name"]
                line[1] = new_data["lastname"]
                line[2] = new_data["id"]
                line[4] = new_data["field_of_study"]
                line[5] = new_data["gpa"]
            new_lines.append(line)
        with open(file_address, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(new_lines)

    def load_majors_from_csv(self, file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                field_name = row[0]
                professor_count = int(row[1])
                physical_space = float(row[2])
                self.university.add_major(field_name, professor_count, physical_space)

    def save_majors_to_csv(self, file_name):
        with open(file_name, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["field name", "professor count", "physical space"])
            current = self.university.majors.head
            while current is not None:
                major = current.data
                writer.writerow(
                    [major.name, major.professor_count, major.physical_space]
                )
                current = current.next

    def add_major_to_file(
        self, field_name, professor_count, physical_space, file_address
    ):
        new_major = {
            "field name": field_name,
            "professor count": professor_count,
            "physical space": physical_space,
        }
        with open(file_address, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(new_major.values())

    def remove_major_from_file(self, field_name, file_address, file_address_student):
        with open(file_address, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            lines = list(reader)
        header = lines[0]
        data_lines = lines[1:]
        new_lines = [header]
        for line in data_lines:
            if line[0] != field_name:
                new_lines.append(line)
        with open(file_address, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(new_lines)
        with open(file_address_student, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            lines = list(reader)
        header = lines[0]
        data_lines = lines[1:]
        new_lines = [header]
        for line in data_lines:
            if line[4] != field_name:
                new_lines.append(line)
        with open(file_address_student, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(new_lines)

    def update_major_in_file(self, field_name, new_data, file_address):
        with open(file_address, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            lines = list(reader)
        header = lines[0]
        data_lines = lines[1:]
        new_lines = [header]
        for line in data_lines:
            if line[0] == field_name:
                line[1] = new_data["professor count"]
                line[2] = new_data["physical space"]
            new_lines.append(line)
        with open(file_address, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(new_lines)

    def remove_student(self, student_number, file_address):
        current_major = self.university.majors.head
        while current_major is not None:
            current_student = current_major.data.students.head
            index = 0
            while current_student is not None:
                if current_student.data.student_number == student_number:
                    current_major.data.students.removing_at_any_position(index)
                    break
                current_student = current_student.next
                index += 1
            current_major = current_major.next
        self.remove_student_from_file(student_number, file_address)

    def update_student(self, student_number, new_data, file_address):
        current_major = self.university.majors.head
        while current_major is not None:
            current_student = current_major.data.students.head
            while current_student is not None:
                if current_student.data.student_number == student_number:
                    current_student.data.name = new_data["name"]
                    current_student.data.lastname = new_data["lastname"]
                    current_student.data.id = new_data["id"]
                    current_student.data.field_of_study = new_data["field_of_study"]
                    current_student.data.gpa = new_data["gpa"]
                    break
                current_student = current_student.next
            current_major = current_major.next
        self.update_student_in_file(student_number, new_data, file_address)

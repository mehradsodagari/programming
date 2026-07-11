from project2_2 import University
from project2_3 import FileManager


def main():
    uni = University()

    file_manager = FileManager(uni)

    try:

        print(" Loading majors from file...")
        file_manager.load_majors_from_csv("majors.csv")

        print(" Loading students from file...")
        file_manager.load_students_from_csv("students.csv")

    except Exception as e:
        print(f" Error loading files: {e}")
        print(" Creating sample data instead...")

        create_sample_data(uni, file_manager)

    print("\n" + "=" * 50)
    print("UNIVERSITY MANAGEMENT SYSTEM")
    print("=" * 50)

    print(f" Total students: {uni.total_student()}")

    print("\n Top 3 students per major:")
    top_students = uni.top_three_student_per_major()
    for major, students in top_students.items():
        print(f"   {major}:")
        for student in students:
            print(f"     - {student.name} {student.lastname} (GPA: {student.gpa})")

    print("\n Average GPA per major:")
    avg_gpa = uni.average_gpa_per_major()
    for major, gpa in avg_gpa.items():
        print(f"   {major}: {gpa}")

    print("\n Professor to student ratio:")
    prof_ratio = uni.professor_to_student_ratio()
    for major, ratio in prof_ratio.items():
        print(f"   {major}: {ratio}")

    print("\n Physical space to student ratio:")
    space_ratio = uni.space_to_student_ratio()
    for major, ratio in space_ratio.items():
        print(f"   {major}: {ratio}")

    print("\n" + "=" * 50)
    print(" Program executed successfully!")


def create_sample_data(uni, file_manager):
    uni.add_major("Computer Science", 15, 2000)
    uni.add_major("Electrical Engineering", 12, 1500)
    uni.add_major("Mechanical Engineering", 10, 1800)

    uni.add_student("Ali", "Ahmadi", "001", "1001", "Computer Science", 18.5)
    uni.add_student("Sara", "Mohammadi", "002", "1002", "Computer Science", 19.2)
    uni.add_student("Reza", "Alavi", "003", "1003", "Electrical Engineering", 17.8)
    uni.add_student("Maryam", "Hosseini", "004", "1004", "Mechanical Engineering", 16.9)
    uni.add_student("Nima", "Karimi", "005", "1005", "Computer Science", 17.5)

    file_manager.save_majors_to_csv("majors.csv")
    file_manager.save_students_to_csv("students.csv")
    print(" Sample data saved to CSV files")


if __name__ == "__main__":
    main()

import json


class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def __str__(self):
        return (
            f"Name: {self.name}, Roll Number: {self.roll_number}, Grade: {self.grade}"
        )


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_number, grade):
        try:
            grade = int(grade)
            if grade < 0 or grade > 100:
                raise ValueError("Grade must be between 0 and 100")
        except ValueError as e:
            print(f"Invalid input: {e}")
            return

        student = Student(name, roll_number, grade)
        self.students.append(student)
        self.save_to_file()

    def save_to_file(self):
        data = []
        try:
            with open("students.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            pass

        data.extend(
            [
                {
                    "name": student.name,
                    "roll_number": student.roll_number,
                    "grade": student.grade,
                }
                for student in self.students
            ]
        )

        with open("students.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_from_file(self):
        try:
            with open("students.json", "r") as file:
                self.students = [
                    Student(student["name"], student["roll_number"], student["grade"])
                    for student in json.load(file)
                ]
        except FileNotFoundError:
            pass

    def view_all_students(self):
        self.load_from_file()
        for student in self.students:
            print(student)

    def search_student_by_roll_number(self, roll_number):
        self.load_from_file()
        for student in self.students:
            if student.roll_number == roll_number:
                print(student)
                return
        print("Student not found.")

    def update_student_grade(self, roll_number, new_grade):
        self.load_from_file()
        for student in self.students:
            if student.roll_number == roll_number:
                student.grade = new_grade
                print("Grade updated successfully.")
                self.save_to_file()
                return
        print("Student not found.")


def display_menu():
    print("\nMenu:")
    print("1. Add a new student")
    print("2. View all students")
    print("3. Search for a student by roll number")
    print("4. Update a student's grade")
    print("5. Exit")


def main():
    sms = StudentManagementSystem()
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student's name: ")
            roll_number = input("Enter student's roll number: ")
            grade = input("Enter student's grade: ")
            sms.add_student(name, roll_number, grade)
        elif choice == "2":
            sms.view_all_students()
        elif choice == "3":
            roll_number = input("Enter student's roll number to search: ")
            sms.search_student_by_roll_number(roll_number)
        elif choice == "4":
            roll_number = input("Enter student's roll number to update grade: ")
            new_grade = input("Enter student's new grade: ")
            sms.update_student_grade(roll_number, new_grade)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

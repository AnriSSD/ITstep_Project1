import json


# Class
class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def __str__(self):
        return (
            f"Name: {self.name}, Roll Number: {self.roll_number}, Grade: {self.grade}"
        )


# Class for managing students
class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.load_from_file()

    # Method for adding a student
    def add_student(self, name, roll_number, grade):
        try:
            # Check if grade is a valid integer between 0 and 100
            grade = int(grade)
            if grade < 0 or grade > 100:
                raise ValueError("Grade must be between 0 and 100")
        except ValueError as e:
            print(f"Invalid input: {e}")
            return

        # Check if a student with the same roll number already exists
        for student in self.students:
            if student.roll_number == roll_number:
                print("Student with the same roll number already exists.")
                return

        # Check if name contains only letters
        if not name.isalpha():
            print("Invalid input: Name must contain only letters.")
            return

        # Check if roll number contains only digits
        if not roll_number.isdigit():
            print("Invalid input: Roll number must contain only digits.")
            return

        student = Student(name, roll_number, grade)
        self.students.append(student)
        self.save_to_file()

    # Method for saving students to a file
    def save_to_file(self):
        data = [
            {
                "name": student.name,
                "roll_number": student.roll_number,
                "grade": student.grade,
            }
            for student in self.students
        ]

        with open("students.json", "w") as file:
            json.dump(data, file, indent=4)

    # Method for loading students from a file
    def load_from_file(self):
        try:
            with open("students.json", "r") as file:
                data = json.load(file)
                self.students = [
                    Student(student["name"], student["roll_number"], student["grade"])
                    for student in data
                ]
        except FileNotFoundError:
            pass

    # Method for displaying all students
    def view_all_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students:
                print(student)

    # Method for searching for a student by roll number
    def search_student_by_roll_number(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                print(student)
                return
        print("Student not found.")

    # Method for updating a student's grade
    def update_student_grade(self, roll_number, new_grade):
        for student in self.students:
            if student.roll_number == roll_number:
                student.grade = new_grade
                print("Grade updated successfully.")
                self.save_to_file()
                return
        print("Student not found.")


# Function for displaying the menu
def display_menu():
    print("\nMenu:")
    print("1. Add a new student")
    print("2. View all students")
    print("3. Search for a student by roll number")
    print("4. Update a student's grade")
    print("5. Exit")


# Main function for interacting with the program
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


# Run the main function
if __name__ == "__main__":
    main()

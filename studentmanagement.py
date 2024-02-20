class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, Grade: {self.grade}"

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_number, grade):
        student = Student(name, roll_number, grade)
        self.students.append(student)

    def view_all_students(self):
        for student in self.students:
            print(student)

    def search_student_by_roll_number(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                print(student)
                return
        print("Student not found.")

    def update_student_grade(self, roll_number, new_grade):
        for student in self.students:
            if student.roll_number == roll_number:
                student.grade = new_grade
                print("Grade updated successfully.")
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
            roll_number = int(input("Enter student's roll number: "))
            grade = input("Enter student's grade: ")
            sms.add_student(name, roll_number, grade)
        elif choice == "2":
            sms.view_all_students()
        elif choice == "3":
            roll_number = int(input("Enter student's roll number to search: "))
            sms.search_student_by_roll_number(roll_number)
        elif choice == "4":
            roll_number = int(input("Enter student's roll number to update grade: "))
            new_grade = input("Enter student's new grade: ")
            sms.update_student_grade(roll_number, new_grade)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

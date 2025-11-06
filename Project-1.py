"<main.py>"
import datetime

# Student structure
class Student:
    def _init_(self, roll, name, course, year, dob):
        self.roll = roll
        self.name = name
        self.course = course
        self.year = year
        self.dob = dob  # date of birth in DD-MM format

students = []

# Function to register new student
def register_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    year = input("Enter Year: ")
    dob = input("Enter Date of Birth (DD-MM-YYYY): ")
    students.append(Student(roll, name, course, year, dob))
    print("Student Registered Successfully!\n")

# Function to display students with birthday today
def birthday_today():
    today = datetime.datetime.now().strftime("%d-%m")
    found = False
    print("\nToday's Birthdays:")
    for s in students:
        if s.dob == today:
            print(f"Roll: {s.roll}, Name: {s.name}, Course: {s.course}, Year: {s.year}")
            found = True
    if not found:
        print("No birthdays today.\n")

# Menu-driven program
def main():
    while True:
        print("\n===== Student Birthday Management System =====")
        print("1. Register New Student")
        print("2. Show Today's Birthdays")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            register_student()
        elif choice == '2':
            birthday_today()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.\n")

# Run the program
main()

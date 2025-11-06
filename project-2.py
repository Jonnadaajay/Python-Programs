import datetime
import json
import os

STUDENT_FILE = "Students.txt"  # To store student data in this file

while True:
    print("Student Birthday Management System")
    print("1. Register New Student")
    print("2. List of Students celebrating Birthdays Today")
    print("3. Exit")
    choice = input("Enter your choice(Option-1,2,3): ")

    if choice == "1":
        student = {}
        student["name"] = input("Enter Name: ")
        student["rollno"] = input("Enter Roll Number: ")
        student["course"] = input("Enter Course: ")
        student["year"] = input("Enter Year: ")
        student["section"] = input("Enter Section: ")
        student["dob"] = input("Enter Date of Birth (dd-mm-yyyy): ")
        student["promise"] = input("Enter Promise Distribution Note: ")

        # To Save student record
        with open(STUDENT_FILE, "a") as f:
            f.write(json.dumps(student) + "\n")
        print(f"Student {student['name']} registered successfully!\n")

    elif choice == "2":
        today = datetime.datetime.now().strftime("%d-%m")
        birthday_students = []

        if not os.path.exists(STUDENT_FILE):
            print("No student records found!\n")
            continue

        with open(STUDENT_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if not line:  # It skips empty lines
                    continue
                student = json.loads(line)
                if student["dob"][:5] == today:
                    birthday_students.append(student)

        if birthday_students:
            print(f"Students celebrating their birthdays on ({today}):\n")
            for stu in birthday_students:
                print(f"Name: {stu['name']}, Roll No: {stu['rollno']}, Course: {stu['course']}, "
                      f"Year: {stu['year']}, Section: {stu['section']}, DOB: {stu['dob']}, "
                      f"Promise: {stu['promise']}")
            
            # Save today's birthday students in a new text file
            file_name = f"{today}.txt"
            with open(file_name, "w") as f:
                for stu in birthday_students:
                    f.write(json.dumps(stu) + "\n")
            print(f"\nDetails saved to file: {file_name}\n")
        else:
            print("No Birthdays Today!\n")

    elif choice == "3":
        print("Exiting program!!!")
        break

    else:
        print("Invalid choice! Please enter valid option!!!\n")

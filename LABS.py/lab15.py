students = {
    101: {"Name": "Aman", "Branch": "CSE", "Sem": 2, "Marks": [85, 90, 78]},
    102: {"Name": "Riya", "Branch": "IT", "Sem": 1, "Marks": [92, 88, 95]},
    104: {"Name": "Karan", "Branch": "ECE", "Sem": 1, "Marks": [88, 91, 84]}
}

def display_menu():
    print("Select an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")

while True:
    display_menu()
    choice = input("Enter your choice (1-7): ").strip()

    if choice == "1":
        print(" Enrolled Student Records ")
        if not students:
            print("No student records found.")
        else:
            for roll, info in students.items():
                print(f"Roll No: {roll} | Name: {info['Name']} | Branch: {info['Branch']} | Sem: {info['Sem']} | Marks: {info['Marks']}")
            print(f"Total Enrolled Students: {len(students)}")

    elif choice == "2":
        roll_input = input("Enter Roll Number to search: ").strip()
        if not roll_input.isdigit():
            print("[ERROR] Roll number must be an integer.")
            continue
        roll = int(roll_input)
        student = students.get(roll)
        if student:
            print(f"Student Found:")
            print(f"Roll No: {roll} | Name: {student['Name']} | Branch: {student['Branch']} | Sem: {student['Sem']} | Marks: {student['Marks']}")
        else:
            print(f"[ERROR] Student with Roll Number {roll} not found.")

    elif choice == "3":
        roll_input = input("Enter Roll Number: ").strip()
        if not roll_input.isdigit():
            print("[ERROR] Roll number must be an integer.")
            continue
        roll = int(roll_input)

        if roll in students:
            print(f"[ERROR] Roll Number {roll} already exists.")
        else:
            name = input("Enter Name: ").strip()
            branch = input("Enter Branch: ").strip()
            sem_input = input("Enter Semester: ").strip()
            sem = int(sem_input) if sem_input.isdigit() else 1

            marks_input = input("Enter subject marks separated by spaces: ").strip()
            marks = [int(m) for m in marks_input.split() if m.isdigit()]

            students[roll] = {
                "Name": name,
                "Branch": branch,
                "Sem": sem,
                "Marks": marks
            }
            print(f"[SUCCESS] Student '{name}' registered successfully.")

    elif choice == "4":
        roll_input = input("Enter Roll Number: ").strip()
        if not roll_input.isdigit():
            print("[ERROR] Roll number must be an integer.")
            continue
        roll = int(roll_input)

        if roll not in students:
            print(f"[ERROR] Student with Roll Number {roll} does not exist.")
        else:
            field = input("Select field to update (Branch or Semester): ").strip().capitalize()
            if field in ["Branch", "Sem", "Semester"]:
                key = "Branch" if field == "Branch" else "Sem"
                new_val = input(f"Enter new value for {field}: ").strip()
                if key == "Sem":
                    new_val = int(new_val) if new_val.isdigit() else students[roll]["Sem"]
                students[roll][key] = new_val
                print(f"[SUCCESS] Updated {field} for Roll Number {roll}.")
            else:
                print("[ERROR] Invalid field selected.")

    elif choice == "5":
        roll_input = input("Enter Roll Number for Academic Performance: ").strip()
        if not roll_input.isdigit():
            print("[ERROR] Roll number must be an integer.")
            continue
        roll = int(roll_input)

        student = students.get(roll)
        if not student:
            print(f"[ERROR] Student with Roll Number {roll} not found.")
        else:
            marks = student.get("Marks", [])
            total = sum(marks)
            num_subjects = len(marks)
            max_marks = num_subjects * 100
            average = (total / num_subjects) if num_subjects > 0 else 0.0
            status = "PASS" if average >= 40.0 else "FAIL"

            print(" ACADEMIC REPORT ")
            print(f"Student Name : {student['Name']} (Roll: {roll})")
            print(f"Subject Marks: {marks}")
            print(f"Total Marks  : {total} / {max_marks}")
            print(f"Average Marks: {average:.2f}%")
            print(f"Final Result : {status}")

    elif choice == "6":
        roll_input = input("Enter Roll Number to delete: ").strip()
        if not roll_input.isdigit():
            print("[ERROR] Roll number must be an integer.")
            continue
        roll = int(roll_input)

        removed_student = students.pop(roll, None)
        if removed_student:
            print(f"[SUCCESS] Record for '{removed_student['Name']}' (Roll No: {roll}) deleted successfully.")
        else:
            print(f"[ERROR] Student with Roll Number {roll} does not exist.")

    elif choice == "7":
        print("Thank you for using the Student Information Management System. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number between 1 and 7.")
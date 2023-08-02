# User Authentication
import csv
'''
def create_user_database():
    users = {}
    try:
        with open("users.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                users[username] = password
    except FileNotFoundError:
        pass
    return users'''
def create_user_database():
    users = {}
    try:
        with open("users.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 2:  # Ensure the line has exactly two parts.
                    username, password = data
                    users[username] = password
                else:
                    print(f"Skipped line with unexpected format: {line.strip()}")
    except FileNotFoundError:
        pass
    return users


def login(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("Login successful.")
        return True
    else:
        print("Invalid username or password.")
        return False
    
def register(users):
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists.")
        return False

    password = input("Enter a password: ")
    users[username] = password

    with open("users.txt", "a") as file:
        file.write("{},{}\n".format(username, password))

    print("Registration successful.")
    return True


# Student Information Management
students = {}  # Database to store student information

def add_student():
    student_id = input("Enter student ID: ")
    
    # Check if the student ID already exists
    if student_id in students:
        print("Student ID already exists.")
        return

    name = input("Enter student name: ")
    # Add more information as needed

    students[student_id] = {"name": name}
    print("Student added successfully.")


def view_student(student_id):
    if student_id in students:
        print("Student ID:", student_id)
        print("Name:", students[student_id]["name"])
        # Print more information as needed
    else:
        print("Student not found.")

def update_student(student_id):
    if student_id in students:
        print("Current Name:", students[student_id]["name"])
        new_name = input("Enter new name: ")
        students[student_id]["name"] = new_name
        save_data()
        print("Update successful.")
    else:
        print("Student not found.")

def delete_student(student_id):
    if student_id in students:
        del students[student_id]
        save_data()
        print("Student deleted.")
    else:
        print("Student not found.")

# Marking Attendance
attendance = {}  # Database to store attendance records

def mark_attendance():
    date = input("Enter date (YYYY-MM-DD): ")
    student_id = input("Enter student ID: ")

    if date not in attendance:
        attendance[date] = []

    if student_id in students:
        if student_id not in attendance[date]:
            attendance[date].append(student_id)
            save_data()
            print("Attendance marked.")
        else:
            print("Attendance already marked for this student on this date.")
    else:
        print("Student not found.")

# Viewing Attendance Records
def view_attendance(date):
    if date in attendance:
        print("Attendance on", date)
        for student_id in attendance[date]:
            view_student(student_id)
        print()
    else:
        print("No attendance records found for this date.")

# Generating Reports
        
def generate_report(date):
    if date in attendance:
        report_file = "attendance_report_" + date + ".txt"
        with open(report_file, "w") as file:
            file.write("Attendance Report for " + date + "\n")
            for student_id in attendance[date]:
                student_data = students.get(student_id, {})
                name = student_data.get("name", "Unknown")
                file.write("Student ID: " + student_id + ", Name: " + name + "\n")
        print("Attendance report generated in", report_file)
    else:
        print("No attendance records found for this date.")

# Main program
users = create_user_database()

# Function to save data
def save_data():
    with open("students.txt", "w") as file:
        for student_id, student_data in students.items():
            file.write("{},{}\n".format(student_id, student_data["name"]))

    with open("attendance.txt", "w") as file:
        for date, attendance_list in attendance.items():
            file.write("{},{}\n".format(date, ",".join(attendance_list)))

# Load existing data from files
try:
    with open("students.txt", "r") as file:
        for line in file:
            student_id, name = line.strip().split(",")
            students[student_id] = {"name": name}
except FileNotFoundError:
    pass

try:
    with open("attendance.txt", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            if len(line) >= 2:
                date = line[0]
                attendance_list = line[1:]
                attendance[date] = attendance_list
except FileNotFoundError:
    pass

while True:
    print("\nEnter the Following choice what you want to do: ")
    print("\n1. Login")
    print("2. Register")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if login(users):
            # Allow further actions after login
            while True:
                print("\n1. Add Student")
                print("2. View Student Details")
                print("3. Update Student")
                print("4. Delete Student")
                print("5. Mark Attendance")
                print("6. View Attendance")
                print("7. Generate Report")
                print("8. Logout")

                user_choice = int(input("Enter your choice: "))

                if user_choice == 1:
                    add_student()
                elif user_choice == 2:
                    student_id = input("Enter the student ID: ")
                    view_student(student_id)
                elif user_choice == 3:
                    student_id = input("Enter the student ID: ")
                    update_student(student_id)
                elif user_choice == 4:
                    student_id = input("Enter the student ID: ")
                    delete_student(student_id)
                elif user_choice == 5:
                    mark_attendance()
                elif user_choice == 6:
                    date = input("Enter date (YYYY-MM-DD): ")
                    view_attendance(date)
                elif user_choice == 7:
                    date = input("Enter date (YYYY-MM-DD): ")
                    generate_report(date)
                elif user_choice == 8:
                    print("Logged out.")
                    break
                else:
                    print("Invalid choice. Please try again.")
    elif choice == 2:
        register(users)
    elif choice == 3:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

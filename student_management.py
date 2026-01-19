print("===================================")
print("  Student Management System (SMS)  ")
print("===================================")

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")

    with open("students.txt", "a") as file:
        file.write(roll + "," + name + "," + course + "\n")

    print("Student added successfully!")


def view_students():
    print("\n--- Student List ---")
    try:
        with open("students.txt", "r") as file:
            for line in file:
                roll, name, course = line.strip().split(",")
                print("Roll:", roll, "| Name:", name, "| Course:", course)
    except FileNotFoundError:
        print("No student records found.")

def search_student():
    roll_to_search = input("Enter Roll No to search: ")
    found = False
    try:
        with open("students.txt", "r") as file:
            for line in file:
                roll, name, course = line.strip().split(",")
                if roll == roll_to_search:
                    print("Student Found - Roll:", roll, "| Name:", name, "| Course:", course)
                    found = True
                    break
        if not found:
            print("Student with Roll No", roll_to_search, "not found.")
    except FileNotFoundError:
        print("No student records found.")

def delete_student():
    roll_to_delete = input("Enter Roll No to delete: ")
    lines = []
    found = False
    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()
        
        with open("students.txt", "w") as file:
            for line in lines:
                roll, name, course = line.strip().split(",")
                if roll != roll_to_delete:
                    file.write(line)
                else:
                    found = True
        
        if found:
            print("Student with Roll No", roll_to_delete, "deleted successfully.")
        else:
            print("Student with Roll No", roll_to_delete, "not found.")
    except FileNotFoundError:
        print("No student records found.")


while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()
    
    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you! Program exited.")
        break  
    

    else:
        print("Invalid choice, try again.")


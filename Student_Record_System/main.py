def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    with open("students.txt", "a") as file:
        file.write(f"{name},{age},{course}\n")

    print("Student Added Successfully!\n")


def view_students():
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

            if not students:
                print("No records found.\n")
                return

            print("\n----- Student Records -----")

            for student in students:
                name, age, course = student.strip().split(",")
                print(f"Name: {name}")
                print(f"Age: {age}")
                print(f"Course: {course}")
                print("------------------------")

    except FileNotFoundError:
        print("No records found.\n")


def search_student():
    search = input("Enter student name: ")

    found = False

    with open("students.txt", "r") as file:
        for student in file:
            name, age, course = student.strip().split(",")

            if name.lower() == search.lower():
                print("\nStudent Found")
                print("Name:", name)
                print("Age:", age)
                print("Course:", course)
                found = True

    if not found:
        print("Student not found.\n")


def delete_student():
    delete_name = input("Enter student name to delete: ")

    with open("students.txt", "r") as file:
        students = file.readlines()

    with open("students.txt", "w") as file:
        found = False

        for student in students:
            name, age, course = student.strip().split(",")

            if name.lower() != delete_name.lower():
                file.write(student)
            else:
                found = True

    if found:
        print("Student deleted successfully.\n")
    else:
        print("Student not found.\n")


while True:

    print("\n===== Student Record System =====")
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
        print("Thank you!")
        break

    else:
        print("Invalid Choice")

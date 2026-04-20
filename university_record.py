courses_available = {
    "math", "physics", "computer science", "biology", "chemistry",
    "statistics", "english", "economics", "history", "philosophy",
    "sociology", "political Science", "geography", "psychology", "art",
    "music", "engineering", "law", "medicine", "business"
}

students = {}
def create_student_info():
    username = input("Enter unique username: ")

    if username in students:
        print("Username already exists!")
        return

    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    city = input("Enter city: ")
    zip_code = input("Enter zip code: ")
    courses = set()
    number_of_courses = int(input("How many courses? "))
    for index in range(number_of_courses):
        course = input(f"Enter course {index + 1}: ").lower()
        if course in courses_available:
            courses.add(course)
        else:
            print(course, "is not offered.")
            course = input(f"Enter course {index + 1}: ").lower()
            courses.add(course)
    students[username] = {
        "name": name,
        "age": age,
        "courses": courses,
        "address": {
            "city": city,
            "zip_code": zip_code
        }
    }
    print("Student added successfully!")

def display_student_record(username):
    if username in students:
        print(students[username])
    else:
        print("Student not found")



def display_student_courses(username):
    if username in students:
        print("Courses:", students[username]["courses"])
    else:
        print("Student not found")

def display_student_zip_code(username):
    if username in students:
        print("Zip code:", students[username]["address"]["zip_code"])
    else:
        print("Student not found")

def display_student_city(username):
    if username in students:
        print("City:", students[username]["address"]["city"])

def add_new_course(username):
    if username in students:
        course = input("Enter a new course: ")
        if course not in courses_available:
            print("Course not offered")
        elif course in students[username]["courses"]:
            print("Course already added")
        else:
            students[username]["courses"].add(course)
            print("Course added successfully")
    else:
        print("Student not found")

def update_student_course(username):
    if username in students:
        old_course = input("Enter old course to remove/update: ").lower()

        if old_course in students[username]["courses"]:
            choice = int(input("Type 1 to remove or  2 to update: "))

            if choice == 1:
                students[username]["courses"].remove(old_course)
                print("Course removed")
            elif choice == 2:
                new_course = input("Enter new course: ").lower()

                if new_course in courses_available:
                    students[username]["courses"].remove(old_course)
                    students[username]["courses"].add(new_course)
                    print("Course updated")
                else:
                    print("Course not offered")

        else:
            print("Course not found")
    else:
        print("Student not found")

def update_student_record(username):
    if username in students:
        students[username]["name"] = input("Enter new name: ")
        students[username]["age"] = int(input("Enter new age: "))
        students[username]["address"]["city"] = input("Enter new city: ")
        students[username]["address"]["zip_code"] = input("Enter new zip code: ")

        print("Student updated successfully")
    else:
        print("Student not found")



def total_number_of_students():
    print("Overall number of  Students:", len(students))

choice = 0

while choice != 10:
    print("\n--- UNIVERSITY RECORD SYSTEM ---")
    print("1. Create Student Information Record")
    print("2. Display Student Record")
    print("3. Display Courses")
    print("4. Display Zip Code")
    print("5. Display City")
    print("6. Add Course")
    print("7. Remove/Update Course")
    print("8. Update Student")
    print("9. Total Students")
    print("10. Exit")

    choice = int(input("Enter choice: "))
    if choice == 1:
        create_student_info()

    elif choice == 2:
        username = input("Enter username: ")
        display_student_record(username)

    elif choice == 3:
        username = input("Enter username: ")
        display_student_record(username)

    elif choice == 4:
        username = input("Enter username: ")
        display_student_zip_code(username)

    elif choice == 5:
        username = input("Enter username: ")
        display_student_city(username)

    elif choice == 6:
        username = input("Enter username: ")
        add_new_course(username)

    elif choice == 7:
        username = input("Enter username: ")
        update_student_course(username)

    elif choice == 8:
        username = input("Enter username: ")
        update_student_record(username)

    elif choice == 9:
        total_number_of_students()

    elif choice == 10:
        print("bye!")

    else:
        print("Invalid choice")


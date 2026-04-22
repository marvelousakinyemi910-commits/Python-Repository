courses_available = {
    "maths", "physics", "computer science", "biology", "chemistry",
    "statistics", "english", "economics", "history", "philosophy",
    "sociology", "political science", "geography", "psychology", "art",
    "music", "engineering", "law", "medicine", "business"
}

students = {}

def create_student_info():
    username = input("Enter unique username: ")

    if username in students:
        return "Username already exists!"

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
             print("Course not offered. Try again.")

    students[username] = {
        "name": name,
        "age": age,
        "courses": courses,
        "address": {
            "city": city,
            "zip_code": zip_code
        }
    }

    return "Student added successfully!"


def display_student_record(username):
    return students.get(username, "Student not found")


def display_student_courses(username):
    if username in students:
        return students[username]["courses"]
    return "Student not found"


def display_student_zip_code(username):
    if username in students:
        return students[username]["address"]["zip_code"]
    return "Student not found"


def display_student_city(username):
    if username in students:
        return students[username]["address"]["city"]
    return "Student not found"


def add_new_course(username,course):
    if username not in students:
        return "Student not found"

    course = course.lower()

    if course not in courses_available:
        return "Course not offered"

    if course in students[username]["courses"]:
        return "Course already added"

    students[username]["courses"].add(course)
    return "Course added successfully"


def update_student_course(username):
    if username not in students:
        return "Student not found"

    old_course = input("Enter old course to remove/update: ").lower()

    if old_course not in students[username]["courses"]:
        return "Course not found"

    choice = int(input("Type 1 to remove or 2 to update: "))

    if choice == 1:
        students[username]["courses"].remove(old_course)
        return "Course removed"

    elif choice == 2:
        new_course = input("Enter new course: ").lower()

        if new_course not in courses_available:
            return "Course not offered"

        students[username]["courses"].remove(old_course)
        students[username]["courses"].add(new_course)
        return "Course updated"

    return "Invalid choice"


def update_student_record(username):
    if username not in students:
        return "Student not found"

    students[username]["name"] = input("Enter new name: ")
    students[username]["age"] = int(input("Enter new age: "))
    students[username]["address"]["city"] = input("Enter new city: ")
    students[username]["address"]["zip_code"] = input("Enter new zip code: ")

    return "Student updated successfully"


def total_number_of_students():
    return len(students)


def main():
    choice = 0

    while choice != 10:
        print("\n--- BRIGHT UNIVERSITY RECORD SYSTEM ---")
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
            print(create_student_info())

        elif choice == 2:
            username = input("Enter username: ")
            print(display_student_record(username))

        elif choice == 3:
            username = input("Enter username: ")
            print(display_student_courses(username))

        elif choice == 4:
            username = input("Enter username: ")
            print(display_student_zip_code(username))

        elif choice == 5:
            username = input("Enter username: ")
            print(display_student_city(username))

        elif choice == 6:
            username = input("Enter username: ")
            course = input("Enter new course: ")

            print(add_new_course(username,course))

        elif choice == 7:
            username = input("Enter username: ")
            print(update_student_course(username))

        elif choice == 8:
            username = input("Enter username: ")
            print(update_student_record(username))

        elif choice == 9:
            print("Total students:", total_number_of_students())

        elif choice == 10:
            print("Bye!")

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
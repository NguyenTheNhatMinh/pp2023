# Student information
def input_student_info():
    num_students = int(input("Enter the number of students in the class: "))
    students = []
    for i in range(num_students):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student date of birth (dd-mm-yyyy): ")
        student = (student_id, student_name, student_dob)
        students.append(student)
    return students

# Course information
def input_course():
    num_courses = int(input("Enter the number of courses: "))
    courses = []
    for i in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        course = (course_id, course_name)
        courses.append(course)
    return courses

# Function to input marks for a selected course and student
def input_marks(students, courses):
    course_id = input("Enter course ID to input marks for: ")
    course_students = []
    for student in students:
        marks = input(f"Enter marks for {student[1]} in {course_id}: ")
        course_student = {'id': student[0], 'name': student[1], 'marks': marks}
        course_students.append(course_student)
    return course_id, course_students

# Function to list all courses
def list_courses(courses):
    print("Courses:")
    for course in courses:
        print(f"{course[0]} - {course[1]}")

# Function to list all students
def list_students(students):
    print("Students:")
    for student in students:
        print(f"{student[0]} - {student[1]}")

# Function to show student marks for a given course
def show_student_marks(course_id, course_students):
    print(f"Course: {course_id}")
    for course_student in course_students:
        print(f"{course_student['id']} - {course_student['name']}: {course_student['marks']}")

# Main function to run the program
def main():
    # Input student and course information
    students = input_student_info()
    courses = input_course()

    # Input marks for a selected course and student
    course_id, course_students = input_marks(students, courses)

    # List all courses and students
    list_courses(courses)
    list_students(students)

    # Show student marks for a given course
    show_student_marks(course_id, course_students)

# Compiling:
if __name__ == '__main__':
    main()




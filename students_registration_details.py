# Student's registration APP (InProgress)
# need to define "Class" instead of Dictionary
# Tasks need to be complete - Implement Grade system (Merit, Non-mertic), Scholarshiop facilties

# hands on nested Dictionary
# student = {"name": "John",
#            "mark": [70, 80, 90, 99],
#            "exams": {
#                 "final": 70,
#                 "midterm": 80
#             },
#            "module": {
#                "math": "Mathematics",
#                "bio": "Biology",
#                "phy": "Physics"
#            },
#            "grades": {
#                "p": "pass",
#                "f": "fail"
#            },
#            }
#
# print(student["grades"]["p"])


student_list = [] # empty student's list

class Student:
    def __init__(self, name):
        self.name = name
        # self.module = module
        self.marks = []

    def calculate_average_mark(self):
        number = len(self.marks)
        if number == 0:
            return 0

        total = sum(self.marks)
        return total / number


def create_student():
    name = input("Please enter the new student's name: ")
    student_data = Student(name)

    return student_data


def add_marks(student, mark):
    student.marks.append(mark)

# s = create_student()
# print(calculate_average_mark(s))
# add_marks(s, 5)
# print(calculate_average_mark(s))
# add_marks(s, 10)
# print(calculate_average_mark(s))


# iterating over a list and using dictionaries inside it
def print_student_details(student):
    # print out important information about the students
    print("{}, average mark: {}.".format(student.name, student.calculate_average_mark()))


def print_student_list(students):
    for i, student in enumerate(students):  # iterating over student list
        print("ID: {}".format(i))
        print_student_details(student)


def menu():
    user_selection = input("Enter 'p' to print the student list, "
                           "'s' to add a new student, "
                           # "'m' to add a module, "
                           "'a' to add a mark to student, "
                           "or 'q' to quit. "
                           "Enter your Selection: ")
    while user_selection != 'q':
        if user_selection == 'p':
            print_student_list(student_list)
        elif user_selection == 's':
            student_list.append(create_student())
        elif user_selection == 'a':
            student_id = int(input("Enter the student ID to add a mark to: "))
            student = student_list[student_id]
            new_mark = int(input("Enter the new mark to the added: "))
            add_marks(student, new_mark)

        user_selection = input("Enter 'p' to print the student list, "
                               "'s' to add a new student, "
                               "'a' to add a mark to student, "
                               "or 'q' to quit. "
                               "Enter your Selection: ")


menu()

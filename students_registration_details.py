## Student's registration APP (Working Process)
# Tasks needed to be Complete - Implement Grade system (Merit, Non-mertic), Scholarshiop facilties

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
module_list = [] # empty module's list


def create_students():
    """method to create student's data."""
    name = input("Please enter the new student's name: ")
    # name_string = name.split(",")
    student_data = {
        "name": name,
        "marks": []}

    return student_data


def create_modules():
    """Creating module's data that are listed to student's name. """
    module = input("Please enter the module's name: ")
    # module_string = module.split(",")
    module_data = {
        "name": module,
        "marks": []}

    return module_data


# print(create_students())


def adding_mark(student, mark):
    student["marks"].append(mark)
    # student["module"].append(mark)


def adding_module_mark(module, mark):
    module["marks"].append(mark)


def calculating_average_marks(student):
    """Calculate average marks per student."""
    number = len(student["marks"])
    if number == 0:
        return 0
    else:
        total = sum(student["marks"])
        return total / number


def calculating_module_average_marks(module):
    """Calculating average marks per Module."""
    module_number = len(module["marks"])
    if module_number == 0:
        return 0
    else:
        total = sum(module["marks"])
        return total / module_number


# s = create_students()
# print(calculating_average_marks(s))
# adding_mark(s, 10)

# Iterating over student list also using Dictionary inside it
def student_details(student):
    # printing out student's info
    print("{}, average marks: {}.".format(student["name"],
                                          calculating_average_marks(student)))


# Iterating over Modules list also using Dictionary inside it
def module_details(module):
    # Printing out student's info by modules.
    print("{}, average marks: ".format(module["module"],
                                       calculating_average_marks(module)))


# Printing out student list
def print_student_list(students):
    for i, student in enumerate(students):  # iterating over student list
        print("ID: {}".format(i))
        student_details(student)


# Printing out Module list
def print_modules_list(modules):
    for i, student in enumerate(modules):  # iterating over module list
        print("ID: {}".format(i))
        module_details(student)


def student_menu():
    """Adding students and modules into list and implementing execution for application."""
    global module_mark
    user_selection = input("Enter 'p' to print the student list, "
                           "'m' to print out module list, "
                           "'ms' to add a new module, "
                           "'s' to add a new student, "
                           "'a' to add a mark to student, "
                           "'ma' to add a mark into module, "
                           "or 'q' to quit. "
                           "Enter your Selection: ")
    while user_selection != 'q':
        if user_selection == 'p':
            print_student_list(student_list)
        elif user_selection == 'm':
            print_modules_list(module_list)
        elif user_selection == 's':
            student_list.append(create_students())
        elif user_selection == 'ms':
            module_list.append(create_students())
        elif user_selection == 'a':
            student_id = int(input("Enter the student ID to add a mark to: "))
            student = student_list[student_id]
            new_mark = int(input("Enter the new mark to the added: "))
            adding_mark(student, new_mark)
        elif user_selection == 'ma':
            module_id = int(input("Enter the module ID to add a mark into Module: "))
            module = module_list[module_id]
            module_mark = int(input("Enter the new mark to the added module: "))
            adding_module_mark(module, module_mark)

        user_selection = input("Enter 'p' to print the student list, "
                               "'m' to print the module list, "
                               "'s' to add a new student, "
                               "'ms' to add a new module, "
                               "'a' to add a mark to student, "
                               "'ma' to add a mark into module, "
                               "or 'q' to quit. "
                               "Enter your Selection: ")


student_menu()

# List to store students' information
students_info = []

# menu1


def Menu1():
    """Store student's information"""
    try:
        # Accept student's info as a list ['name','mid','final']
        student_input = input(
            "Enter name | mid-term_score | final_score (with a space in between): ").split()

        # Exception Handling for data input count
        if len(student_input) != 3:
            raise ValueError(
                "Invalid input format. There must be 3 types of data(name, mid-term_score, final_score)")
        # Unpacking student's info
        name, mid_score, final_score = student_input
        # Exception Handling for existing names
        for student_info in students_info:
            if name == student_info['name']:
                raise ValueError(
                    f"Student with the name {name} already exists.")
        # Exception Handling for positive integer scores
        # int(mid_score) -> checking if it is integer or not
        # < 0 -> checking if it is positive or not
        if int(mid_score) < 0 or int(final_score) < 0:
            raise ValueError("Scores must be positive integers.")
        # Exception handling for scores greater than 100
        if int(mid_score) > 100 or int(final_score) > 100:
            raise ValueError("Scores out of range (must between 0~100).")
    except ValueError as ve:
        print(ve)
    else:
        # Add student's info to the list
        student_info = {'name': name,
                        'mid_term_score': int(mid_score), 'final_score': int(final_score)}
        students_info.append(student_info)
        print("Student information added successfully.")

# menu2


def Menu2():
    """Grading ungraded students."""
    try:
        if not students_info:
            raise ValueError("There is no student data")
    except ValueError as ve:
        print(ve)
    else:
        for student_info in students_info:
            if 'grade' not in student_info:
                avg = (student_info['mid_term_score'] +
                       student_info['final_score']) / 2
                if avg >= 90:
                    grade = 'A'
                elif avg >= 80:
                    grade = 'B'
                elif avg >= 70:
                    grade = 'C'
                else:
                    grade = 'D'
                student_info['grade'] = grade
        print('Graded all students.')


def Menu3():
    """Print students' information."""
    try:
        if not students_info:
            raise ValueError("There is no student data.")
        for student_info in students_info:
            if 'grade' not in student_info:
                raise ValueError("There is an ungraded student.")
    except ValueError as ve:
        print(ve)
    else:
        print('----------------------------------------------------------')
        # Creating a visually appealing table
        # Print the header
        print(f"{'Name':<15}{'Mid-term':<15}{'Final':<15}{'Grade'}")
        # Print data rows
        for student_info in students_info:
            print(
                f"{student_info['name']:<15}{student_info['mid_term_score']:<15}{student_info['final_score']:<15}{student_info['grade']}")
        print('----------------------------------------------------------')


def Menu4():
    """Delete student's information."""
    try:
        if not students_info:
            raise ValueError("There is no student data.")
    except ValueError as ve:
        print(ve)
    else:
        name_to_delete = input(
            "Enter student's name that you want to delete: ")
        exist = False
        for student_info in students_info:
            if student_info['name'] == name_to_delete:
                students_info.remove(student_info)
                print(f"{name_to_delete}'s information is deleted.")
                exist = True
                break
        if not exist:
            print(f"The student with name {name_to_delete} does not exist.")


# Main
print("----------------------Menu----------------------")
print("Choose 1 for Inserting student's information. (name, mid-term_score, final_score)")
print("Choose 2 for Grading students.")
print("Choose 3 for Printing students' information.")
print("Choose 4 for Deleting student's information.")
print("Choose 5 to Exit Program.")
print("-------------------------------------------------------------------------------------")
while True:
    choice = input("Choose a number(1 to 5): ")
    if choice == '1':
        Menu1()
    elif choice == '2':
        Menu2()
    elif choice == '3':
        Menu3()
    elif choice == '4':
        Menu4()
    elif choice == '5':
        print('Exiting Program!!')
        break
    else:
        print('Wrong number! Choose again.')

def get_grades(name):
    marks = {"James": 90, "Jules": 55, "Arthur": 77}

    for student in marks:
        if student == name:
            print(marks[student])
            break
    else:
        print('No entry with that name found.')

if __name__ == "__main__":
    print("Maths test results")
    student_name = input("Type student's name: ")
    get_grades(student_name)
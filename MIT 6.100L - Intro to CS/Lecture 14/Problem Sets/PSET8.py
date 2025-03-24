# 23/03/2025

# Problem: Student Grades Management

students = {}

def add_student(students, name):
    students[name] = 0

def add_grade(students, name, grade):
    if name in students:
        students[name] = grade
    else:
        return f"ERROR: Student {name} not found"

def average_grade(students, name):
    
    if name not in students:
        return f"Student {name} not found"
    
    grades = students[name]

    if len(grades) == 0:
        return f"No grades available for {name}"
    
    average = sum(grades) / len(grades)

    return average

def best_student(students):

    highest = 0

    best = ""

    for name, grades in students.items():
        if len(grades) == 0:
            continue
        average = sum(grades) / len(grades)

        if average > highest:
            highest = average
            best = name
    
    return best if best else "No student with grades found."

add_student(students, 'Bob')
add_grade(students, 'Tiffany', 10)
print(students)

# Solved.
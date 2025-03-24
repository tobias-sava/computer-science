# 23/03/2025

# Problem: Student Grades Management

students = {}

def add_student(students, name):
    students[name] = 0

def add_grade(students, name, grade):
    if name in students:
        students[name] = grade
    else:
        print(f"ERROR: Student {name} not found")

def average_grade(students, name):
    
    average = 0

    for i in students[name].values():
        average = sum(i) / len(i)

add_student(students, 'Bob')
add_grade(students, 'Tiffany', 10)
print(students)
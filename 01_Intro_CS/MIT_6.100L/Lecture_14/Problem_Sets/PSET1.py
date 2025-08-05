# 22/03/2025

def find_grades(grades, students):
    """ grades is a dict mapping student names (str) to grades (str)
        students is a list of student names
    Returns a list containing the grades for students (in the same order) """

    grades_list = []

    for i in students: # Loops through the list of students we want to get the grades for.
        grades_list.append(grades[i]) # Appends the value of i key to grades_list.

    return grades_list

# For example:

d = {'Ana':'B', 'Matt':'C', 'John':'B', 'Katy':'A'}
print(find_grades(d, ['Matt', 'Katy'])) # returns ['C', 'A']
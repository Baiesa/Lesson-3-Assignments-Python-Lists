'''

Objective:
The aim of this assignment is to integrate various list operations and methods to solve a complex problem.

Problem Statement:
You're organizing a school event, and you have lists containing student names, their grades, and the activities they're
 interested in.

Task 1: Given the lists:

'''
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

# Create a new list of dictionaries using list comprehension
student_info = [{"name": name, "grade": grade, "activity": activity}
    for name, grade, activity in zip(students, grades, activities)]

print(student_info)
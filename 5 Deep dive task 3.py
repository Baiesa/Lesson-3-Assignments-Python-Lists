# Task 3: For the remaining students, add a new key-value pair in their dictionary: "status": "Passed".

filtered_students_info = [
    {'name': 'John', 'grade': 85, 'activity': 'Football'},
    {'name': 'Doe', 'grade': 90, 'activity': 'Music'},
    {'name': 'Smith', 'grade': 88, 'activity': 'Dance'}]

for student in filtered_students_info:
    student['status'] = 'Passed'

print(filtered_students_info)
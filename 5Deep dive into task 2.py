# Task 2: Filter out students who have grades below 80.

students_info = [{'name': 'John', 'grade': 85, 'activity': 'Football'},
    {'name': 'Doe', 'grade': 90, 'activity': 'Music'},
    {'name': 'Jane', 'grade': 78, 'activity': 'Art'},
    {'name': 'Smith', 'grade': 88, 'activity': 'Dance'}]

filtered_students_info = [student for student in students_info if student['grade'] >= 80]

print(filtered_students_info)
# Problem Statement:
# You have two lists of student names. One list contains the names of students who have submitted their assignments,
# and the other list contains the names of students who attended the last class.

# Task 1: Given the two lists:

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

common_students = list(set(submitted)) and set(attended)
print("students who both submitted assignments and attended class", common_students)
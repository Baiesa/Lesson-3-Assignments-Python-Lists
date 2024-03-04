# Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
attended_copy = attended.copy()
for student in attended_copy:
    if student not in submitted:
        attended.remove(student)

print("Updated attended list:", attended)

# Task 2: Check if the two lists are identical in terms of their content, regardless of order.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
submitted_sorted = sorted(submitted)
attended_sorted = sorted(attended)
if submitted_sorted == attended_sorted:
    print("The two lists are identical in terms of their content.")
else:
    print("The two lists are not identical in terms of their content.")
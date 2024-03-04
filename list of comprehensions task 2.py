# Task 2: Use a list comprehension to create a new list containing numbers greater than 5.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 101]

greater_than_5 = [num for num in numbers if num > 5]
print(greater_than_5)

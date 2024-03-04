'''
4. List Comprehensions and Membership Operators

Objective:
The aim of this assignment is to practice using list comprehensions and membership operators in Python.

Problem Statement:
You have a list of numbers, and you'd like to generate a new list based on certain conditions.

Task 1: Given the list:
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 101]

even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
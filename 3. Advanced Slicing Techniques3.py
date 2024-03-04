# Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
                95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

reversed_temperatures = temperatures[::-1]
extracted_temperatures = reversed_temperatures[4:10]

print(extracted_temperatures)
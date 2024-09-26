numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

# List comprehension to filter negative numbers and zero
negative_and_zero = [num for num in numbers if num <= 0]

print(negative_and_zero)

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

# Flattening the list of lists of lists to a one-dimensional list
flattened_list = [num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2]

print(flattened_list)


# List comprehension to generate the tuples
result = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

# Output the result
for item in result:
    print(item)


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# List comprehension to flatten and format the list
flattened_list = [[country.upper(), country[:3].upper(), capital.upper()] for sublist in countries for (country, capital) in sublist]

print(flattened_list)



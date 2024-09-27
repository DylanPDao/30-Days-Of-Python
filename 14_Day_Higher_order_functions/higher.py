from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

# 1. map()
# Purpose: To apply a function to each item in an iterable (e.g., list) and return a new iterable with the results.
# How it works: It takes a function and an iterable as inputs. It applies the function to every element in the iterable and returns a map object, which can be converted to a list or another iterable.

# 2. filter()
# Purpose: To filter an iterable by applying a function that returns True or False for each item, and only keep the items for which the function returns True.
# How it works: It takes a function (that returns a boolean) and an iterable. The function is applied to each element, and only the elements that satisfy the condition (True) are included in the resulting iterable.

# 3. reduce()
# Purpose: To apply a function to accumulate or reduce an iterable to a single value. This function is part of the functools module and must be imported before use.
# How it works: It takes a function and an iterable. The function must take two arguments and the reduce() applies it cumulatively to the items in the iterable, reducing it to a single value.

upper_countries = list(map(lambda country: country.upper(), countries))
print(upper_countries)

squared_numbers = list(map(lambda num: num ** 2, numbers))

upper_names = list(map(lambda name: name.upper(), names))

countries_with_land = list(filter(lambda country: 'land' in country, countries))

countries_with_six_chars = list(filter(lambda country: len(country) == 6, countries))

countries_six_or_more = list(filter(lambda country: len(country) >= 6, countries))

countries_starting_with_e = list(filter(lambda country: country.startswith('E'), countries))


result = reduce(lambda acc, num: acc + num, filter(lambda num: num % 2 == 0, map(lambda num: num ** 2, numbers)))

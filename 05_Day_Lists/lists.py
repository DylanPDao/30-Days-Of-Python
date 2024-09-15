list = []
list5 = ['yes', 'yes', 'yes', 'yes', 'yes']
print(len(list5))
print(list5[0], list5[2], list5[-1],)
mixed_data_types = ['Dylan', 29, '5feet 8 inches', 'Single', 'address']
it_companies = ['FB', 'Goog', 'Micro']
it_companies.pop
print(it_companies)
does_exist = 'Facebook' in it_companies
print(does_exist)
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort(reverse=False)
print(ages)
median = ages[int(len(ages)/2)]
print(median)

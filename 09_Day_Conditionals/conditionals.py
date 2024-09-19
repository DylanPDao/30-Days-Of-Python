age = input("Enter your age: ")
if int(age) >= 18:
    print('You are old')
else: 
    print('You need ', 18 - int(age), ' more years to learn to drive')

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if person['skills']:
    print(person['skills'][2])

if person['skills']:
    if 'Python' in person['skills']:
        print('Hell yes')
    else:
        print('fk no')
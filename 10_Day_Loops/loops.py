person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

count = 0
hash = '#'
value = 0

#while count < 8:
#    print(hash)
#   hash = hash + '#'
#  count = count + 1


#while count < 11:
#    print(count,' x ', count, ' = ', count*count)
#    count += 1

while count < 101:
    value += count
    count += 1
    if count == 100:
        print('the sum of all numbers is ', value)
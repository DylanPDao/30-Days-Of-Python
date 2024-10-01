names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']

# Unpacking
*nordic_countries, es, ru = names

print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
print(es)  # 'Estonia'
print(ru)  # 'Russia'

my_dict = {'Name': 'Nadya', 'Year of birth': 2003}
print(my_dict)
my_dict['N'] = 'Gena'
my_dict['year'] = 2024
a = my_dict.pop('Name')
b = my_dict.pop('year')
print(a)
print(b)
my_dict.update({'pet': 'pats', 'age': 999})
del my_dict['Year of birth']
print(my_dict.get('Year of birth', 2003))
print(my_dict)

my_set = {1, 2, 1, 'man', 'one', 'man'}
my_list = [1, 2, 1, 'man']
my_list = set(my_list)
print(my_list)
print(my_list.add('cat'))
print(my_list.add(11.11))
print(my_list)
print(my_list.remove('man'))
print(my_list)

my_dict = {
    'tuple': ('apple', 'orange', 'lemon', 'chery', 'potato', 'cucumber'),
    'list': [1, 2, 3, 4, 5, 6],
    'dict': {'key_one': 'key', 'key_three': 3, 'key_four': 4, 'key_five': 5, 'key_six': 6},
    'set': {'name', 'surname', 'your_name', 'your_surname', 'any_value'}
}
#  print(my_dict['tuple'][-1])
my_dict['list'].append(7)
my_dict['list'].pop(1)
#  print(my_dict['list'])
my_dict['dict']['i am a tuple'] = '2805'
my_dict['dict'].pop('key_one')
#  print(my_dict['dict'])
my_dict['set'].add('phone')
my_dict['set'].discard('your_name')
#  print(my_dict['set'])
print(my_dict)

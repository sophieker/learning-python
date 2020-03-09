name = input('What is your name? ')
if len(name) > 7:
    print('Whoa', name, 'is a long name')
elif len(name) == 7:
    print('7 letters')
else:
    print('less than 7')


import random
import string
print('Welcome to Password Picker!')
adjectives = ['sleepy', 'fast', 'quick', 'smart', 'funny', 'fat', 'blue', 'sad', 'depressed', 'purple', 'burned']
nouns = ['apple', 'dinosaur', 'ball', 'toaster', 'goat', 'pig', 'dragon', 'hammer', 'duck', 'panda', 'minecraft']

while True:

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0,100)
    special_char = random.choice(string.punctuation)
    password = adjective + noun + str(number) + special_char
    print('Your new password is: ', password)

    response = input('Would you like another password? Type y or n: ')
    if response == 'n':
        break

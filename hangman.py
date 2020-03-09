import random
lives = 9
words = ['odyssey', 'iphone', 'food', 'gucci', 'sophie', 'mississipi', 'benzinger', 'knowledge', 'astronomy', 'hangman' ]
secret_word = random.choice(words)
clue = []
index = 0
while index < len(secret_word):
    clue.append('?')
    index = index + 1
heart_symbol = u'\u2764'
guessed_word_correctly = False

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1

difficulty = input('Choose difficulty (type 1, 2 or 3) : \n 1 Easy\n 2 Normal\n 3 Hard\n')
difficulty = int(difficulty)

if difficulty == 1:
    lives = 12
elif difficulty == 2:
    lives = 9
else:
    lives = 6

while lives > 0:
    print(clue)
    print('Lives left:' + heart_symbol * lives)
    guess = input('Guess a letter or the whole word: ')

    if guess == secret_word:
        guessed_word_correctly = True
        break
    
    elif guess in secret_word:
        update_clue(guess, secret_word, clue)
        if not ("?" in clue):
            guessed_word_correctly = True
            break
        
    else:
        print('Incorrect. You lose a life')
        lives = lives - 1


if guessed_word_correctly:
    print('You won! The secret word was ' + secret_word)
else:
    print('You lost! The secret word was ' + secret_word)

import random
#code to play rock paper scissors with computer
usage = ('Usage Instructions\n  Enter: \n  0 for Rock\n ' \
                   ' 1 for Paper \n  2 for Scissors')
print(usage)

while True:
    
    user_answer = int(input('Your turn: '))
    if user_answer < 0 or user_answer > 2:
        print('Incorrect input. Please enter again.')
        continue

    computer_answer = random.randint (0, 2)

    print('computer answer: ', computer_answer)
    
    # equals = tie
    if computer_answer == user_answer + 1:
        print ('computer wins!')

    elif computer_answer == user_answer:
        print ('tie!')

    else:
        print ('user wins!')


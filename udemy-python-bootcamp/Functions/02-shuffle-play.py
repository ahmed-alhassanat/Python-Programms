# a simple game to guess the index of 'O' in a shuffled list
from random import shuffle
# Function to shuffle the initial list
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

# Input Function to receive the player's guess
def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('Pick an index number: 0, 1 or 2 ')
        
    return int(guess)

# Function to check the player's guess
def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print('Correct!')
    else:
        print('Wrong!')
        print(mylist)

# initial list
mylist = ['', 'O', '']
# shuffle list
shuffled_list = shuffle_list(mylist)
#user guess
guess = player_guess()
# check guess
check_guess(shuffled_list, guess)

import random

def guess(n):
    random_number = random.randint(1, n) # define a random number
    user_input = 0 # init the user's input
    
    while user_input != random_number: #while the user\s input is different to the random number
        user_input = int(input('Enter a number between 1 and 20: ')) #ask him to enter a new number

        #testing if the number is higher or lower than the random_number
        if user_input > random_number:
            print('Sorry ! guess again, too low')
        elif user_input < random_number:
            print('Sorry ! guess again, too hight')
    #if the user got the right number
    print('yay ! you got it {}'.format(random_number))

guess(13)

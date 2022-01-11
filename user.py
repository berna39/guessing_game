import random

def guess(n):
    random_number = random.randint(1, n)
    user_input = 0
    
    while user_input != random_number:
        user_input = int(input('Enter a number : '))
        if user_input > random_number:
            print('Sorry ! guess again, too low')
        elif user_input < random_number:
            print('Sorry ! guess again, too hight')
    print('yay ! you got it {}'.format(random_number))

guess(13)

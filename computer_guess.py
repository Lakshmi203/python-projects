from itertools import count
import random

def guess(x):
    
    low = 1
    high = x
    feedback = ''
    print(f'guess number in between {low} and {high}')
    count = 0
    while count<3:
        if low != high:
            random_number = random.randint(low, high)
        else:
            random_number = low
        feedback = input(f"{random_number} is too high or too low or correct comparing to guess ")
        count+=1
        if(feedback == 'l'):
            low = random_number + 1
        elif(feedback == 'h'):
            high = random_number - 1
        elif(feedback == 'c'):
            print(f'computer guessed your number and that is {random_number}')
            break
    if count>=3:
        print("you won! congrats computer failed to guess your answer")
    
guess(10)
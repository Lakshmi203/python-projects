import random

def play():
    user = input("what's you choose? 'r' for rock, 'p' for papper, 's' for scissors ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "it is tie"
    print(f'computer chosen {computer}')

    if is_win(user, computer):
        return 'You won! '
    return 'You lost!'

def is_win(player, opponenet):
    if(player == 'r' and opponenet == 's') or (player == 's' and opponenet == 'p') or (player == 'p' and opponenet == 'r'):
        return True
print(play())
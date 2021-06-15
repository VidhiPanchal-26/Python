import random

def play():
    user = input("choose:'r' for rock 'p' for paper 's' for scissor? ")
    computer = random.choice(['r','p','s'])
    
    if user==computer:
        return 'it\'s a tie'

    if is_win(user,computer):
        return "You Win!!"
    
    return "You Lose!!"

def is_win(player , opponent):
    if (player=='r' and opponent=='s') or (player=='p' and opponent=='r') or (player=='s' and opponent=='p'):
        return True

print(play())
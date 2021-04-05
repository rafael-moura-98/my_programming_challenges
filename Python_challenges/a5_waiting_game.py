""" Um jogo basicamente impossível... Você precisa acertar o tempo apresentado como objetivo."""

import time
from random import randint


delay = randint(2, 4)
print(f'\nYour target is to wait {delay} seconds.')

input('\nType enter to start or stop: ')
print('GAME STARTED')

game_start_time = time.perf_counter() #start couting time running

input('\nType enter to stop: ')
game_duration_time = time.perf_counter() - game_start_time

print(f"\nYour goal was {delay} and you hit {game_duration_time}.")

if(delay > game_duration_time):
    print("\nYou were too fast! ;-;")
elif (delay < game_duration_time):
    print("\nToo slow. Try again!")
else:
    print("\nPerfect timing. That's amazing!")
    
    
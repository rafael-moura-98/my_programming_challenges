import time
from random import random, randint

"""
def input_time():
    timer = random() + randint(2, 3) # Soma um float aleatório entre 0 e 1 e um inteiro entre 2 e 3.
    timer_short = float(("%.2f" % round(timer, 2))) # Formata o numero para apenas 2 decimais.
    return timer_short
"""

delay = randint(2, 4)
print(f'Your target is to wait {delay} seconds.')

ready = input('\nType enter to start or stop: ')
if ready == '':
    print('GAME STARTED')
    time_playing = time.perf_counter()
    time.sleep(delay)
    print(time_playing)
    
    
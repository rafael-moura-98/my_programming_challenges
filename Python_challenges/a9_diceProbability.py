from random import randint 

def dices_pb_outcome(*args):
    """
    Function that runs a million times a given type of dice to check the percent of each outcome.
    
    Parameters
    -----------

    Args is a list that needs to be filled with types of dice.
    
    For example if you wanna check the outcome of a d20 (dice of 20 sides) and a d10, you just need to pass the parameter 20 and 10.
    
    dices_pb_outcome(20, 10)

    Prints
    -----------

    It prints on the console how many times a side has been the outcome. All the dices are rolled toguether.

    Might be improved
    -----------------

    *Function should return a value instead of print directly on the console.
    *The return should be ordered by the dice value or the percentage.
    """

    add = 0 #carrega a soma dos dados jogados

    outcomes = dict() #contém quantas x uma saida repetiu
    rolls = list() 

    rolls = []
    outcomes = dict(rolls)

    for i in range (1000000):    
        for j in range(len(args)):
            dice_throw = randint(1, args[j])
            add += dice_throw

        if(add in outcomes):
            outcomes[add] += 1
        else:
            rolls = list(outcomes.items())
            rolls.append((add, 1))
            outcomes = dict(rolls)
        add = 0
    
    print(f'Numero de dados rolados: {len(args)}')
    print(f'Tipos de dados:', end=' ')
    for dice_numbers in range(len(args)):
        print(f'd{args[dice_numbers]}', end=' ')
    print('')
    
    for key in outcomes.keys():
        print(f'A saída {key} caiu {outcomes[key]} vezes. Equivale a {(outcomes[key]/1000000)*100}%')


dices_pb_outcome(20, 10)
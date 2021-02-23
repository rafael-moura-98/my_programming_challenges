from random import randint 

def dices_pb_outcome(*args):
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



dices_pb_outcome(20)
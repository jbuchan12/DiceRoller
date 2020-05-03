import sys
from random import randrange

def rollD10() -> int:
    return randrange(10)

def rollD100() -> int:
    return randrange(100)

def roll():   
    chosenRoll = -1  

    if sys.argv[1] == '10':
        chosenRoll = rollD10()

    if sys.argv[1] == '100':
        chosenRoll = rollD100()

    print(chosenRoll)

roll()
    
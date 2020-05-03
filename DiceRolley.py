import sys
from random import randrange

#Roll a single D10 dice
def rollD10() -> int:
    return randrange(10)

#Roll a single D100 dice
def rollD100() -> int:
    return randrange(100)

#Roll from the command line
def roll():   
    result = -1  

    if sys.argv[1] == '10':
        result = rollD10()

    if sys.argv[1] == '100':
        result = rollD100()

    #Bad param
    if result == -1:
        print(f"Roll {sys.argv[1]} is not valid")

    #Print the dice roll
    print(result)

roll()
    
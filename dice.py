def dice6():
    import random
    x = random.randint(1, 6)
    print("You rolled, ")
    print(x)

def dice8():
    import random
    x = random.randint(1, 8)
    print("You rolled, ")
    print(x)

def dice10():
    import random
    x = random.randint(1, 10)
    print("You rolled, ")
    print(x)

def dice12():
    import random
    x = random.randint(1, 12)
    print("You rolled, ")
    print(x)

def dice20():
    import random
    x = random.randint(1, 20)
    print("You rolled, ")
    print(x)

def rolldice():
    if InputDice == "6":
        dice6()
    elif InputDice == "8":
        dice8()
    elif InputDice == "10":
        dice10()
    elif InputDice == "12":
        dice12()
    elif InputDice == "20":
        dice20()
    else:
        print("you must select the from the listed numbers")


while True:
    print("Enter what dice you want to roll. 6, 8, 10, 12, 20")
    InputDice = input()
    rolldice()
    while True:
        answer = input('Roll again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print ('Invalid input.')
    if answer == 'y':
        continue
    else:
        print ('goodbye')
        break



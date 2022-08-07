import random


def game(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif comp=='g':
        if you=='w':
            return True
        elif you=='s':
            return False    

randNO = random.randint(1, 3)

print("Computer turn: snake(s) water(w) or gun(g)?")
# print(randNO)
if randNO ==1:
    comp = 's'
elif randNO ==2:
    comp = 'w'
if randNO ==3:
    comp = 'g'
you = input("Your turn: snake(s) water(w) or gun(g)? ")

a=game(comp,you)

print(f"computer chose {comp}")
print(f"you chose {you}")
if a==None:
    print("the game is tie")
elif a:
    print("you win!!!")
else:
    print("you lose")
#sanke water gun Game
#while loop


import random
print("\t \t Welcome to Snake-Water-Gun Game")
c_score = 0
u_score = 0
chances = 10
chance = 0
ele = ['s','w','g']
print("s for snake\nw for water\ng for gun")
while chance < chances:
    computer = random.choice(ele)
    user = str(input("Snake/Water/Gun : "))

    if user==computer:
        print("Same guess. Zero point to each")
    elif user=='s' and computer=='w':
        u_score = u_score+1
        print(f"Your choice was {user} and Computer's choice was {computer}")
        print(f"You won 1 point")
        print(f"Your point is {u_score} and computer's point is {c_score}")
    elif user=='s' and computer=='g':
        c_score = c_score+1
        print(f"Your choice was {user} and Computer's choice was {computer}")
        print(f"Computer won 1 point")
        print(f"Your point is {u_score} and computer's point is {c_score}")
    elif user=='w' and computer=='g':
        u_score = u_score+1
        print(f"Your choice was {user} and Computer's choice was {computer}")
        print(f"You won 1 point")
        print(f"Your point is {u_score} and computer's point is {c_score}")
    elif user=='w' and computer=='s':
        c_score = c_score+1
        print(f"Your choice was {user} and Computer's choice was {computer}")
        print(f"Computer won 1 point")
        print(f"Your point is {u_score} and computer's point is {c_score}")
    elif user=='g' and computer=='s':
        u_score = u_score+1
        print(f"Your choice was {user} and Computer's choice was {computer}")
        print(f"You won 1 point")
        print(f"Your point is {u_score} and computer's point is {c_score}")
    elif user=='g' and computer=='w':
        c_score = c_score+1
        print(f"Your choice was {user} and Computer's choice was {computer}")
        print(f"Computer won 1 point")
        print(f"Your point is {u_score} and computer's point is {c_score}")
    else:
        print("Incorrect Input!")

    chance=chance+1
    print(f"{chances - chance} Chance left out of {chances}")
print("Game Over!")
if u_score>c_score:
    print("You Won!")
elif c_score>u_score:
    print("Computer Won!")
else:
    print("You and computer both Scored equal. Nobody won!")
print(f"Your score: {u_score} and Computer's score: {c_score}")
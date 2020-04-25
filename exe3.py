#Todo:
# make a number guessing game. should have a limit of guesses . if guess is correct
# print won and number of guesses he took to finish. if guesses finished print game over.


print("                   ...Game:: Guess The Number!...\n"
      "           You have to guess the number between 1 to 100!\n")
n = 18
g = 1
while(g<=9):
    num = int(input("Guess the Number: "))
    if num < 18:
        print("Larger than this one. Try again!\n")
    elif num > 18 or num >100:
        print("Smaller than this one. Try again!\n")
    else:
        print("YOU WON!!! You have guessed the Correct number.\n"
              "You took", g,"guesses to finish the game.")
        break
    print(9-g, "guesses left")
    g = g+1
    if g>9:
        print("Game Over! No Guesses Left!")


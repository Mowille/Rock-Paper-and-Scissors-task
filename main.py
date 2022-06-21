# Importing the inbuilt python module - random
import random
print("Welcome to Mowille's Rock, Paper, and Scissors Game...")
print("Rules of the game: \n" + "Rock beats Scissors, \n" +
      "Paper beats Rocks, \n" + "and Scissors beats Paper. \n")

while True:
    print("Choices: \n" "1. Rock\n"   "2. Paper\n"   "3. Scissors\n")
    # 1 for rock, 2 for paper and 3 for scissors.
    Choices = int(input("Your turn: "))
    while Choices > 3 or Choices < 1:
        Choices = int(input("Enter valid input: "))

    if Choices == 1:
        choicemade = "Rock"
    elif Choices == 2:
        choicemade = "Paper"
    else:
        choicemade = "Scissors"

    # Print the user's choice
    print("Your choice is: " + choicemade)
    print("CPU's turn...")

    # Computer is made to select a number between 1 and 3 randomly using random.randint...
    choice_of_cpu = random.randint(1, 3)
    while choice_of_cpu == Choices:
        choice_of_cpu = random.randint(1, 3)

    if choice_of_cpu == 1:
        cpu_choicename = "Rock"
    elif choice_of_cpu == 2:
        cpu_choicename = "Paper"
    else:
        cpu_choicename = "Scissors"

    print("CPU's choice is: " + cpu_choicename)

    print(choicemade + " vs " + cpu_choicename)

    if Choices == choice_of_cpu:
        print("Draw => ", end="")
        result = "Draw"

    if((Choices == 1 and choice_of_cpu == 3) or (Choices == 3 and choice_of_cpu == 1)):
        print("Rock smashes Scissors - Rock wins => ", end="")
        result = "Rock"
    elif ((Choices == 1 and choice_of_cpu == 2) or (Choices == 2 and choice_of_cpu == 1)):
        print("Paper covers Rock - Paper wins => ", end="")
        result = "Paper"
    else:
        print("Scissors cuts Paper - Scissors wins => ", end="")
        result = "Scissors"

    if result == "Draw":
        print("It is a tie!")
    elif result == choicemade:
        print("You win!")
    else:
        print("CPU wins!")

    print("Want to play some more? (Y/N)")
    answer = input().lower

    if answer == 'n':
        break

print("\nThanks for playing Mowille's Rock, Paper and Scissors game...")

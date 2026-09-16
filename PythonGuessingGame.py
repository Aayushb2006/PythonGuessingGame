import random

x = int

print("Number Guessing Game")

while True:
    print("Please choose a difficulty")
    print("1 - Easy (1 to 10)")
    print("2 - Medium (1 to 50)")
    print("3 - Hard (1 to 100)")

    difficulty = input("Please Enter 1, 2 or 3: ")

    if difficulty == "1":
        max_number = 10
    elif difficulty == "2":
        max_number = 50
    elif difficulty == "3":
        max_number = 100
    else:
        print("Invalid choice, default setting chosen: Level Medium")
        max_number = 50

    x = random.randint(1, max_number)
    Attempts = 0

    print("I am thinking of a number between 1 and ", max_number)

    while True:
        guess_input = input("Enter your guess: ")

        if not guess_input.isdigit():
            print("Please enter a whole number.")
            continue

        Attempts += 1
        guess = int(guess_input)

        if guess > x:
            print("Too High! Try again.")
        elif guess < x:
            print("Too low! Try again.")
        else:
            guess == x
            print("That is Correct Well done!")
            print("Number of Attempts:", Attempts)
            break

    restart_input = input("Would you like to play again (yes/no): ").lower()
    if restart_input != "yes":
        print("Thanks for playing!")
        break


    





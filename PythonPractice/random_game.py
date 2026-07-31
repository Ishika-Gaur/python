from random import randint

answer = randint(1, 10)

while True:

    try:

        guess = int(input("Guess a number (1-10): "))

        if 1 <= guess <= 10:

            if guess == answer:
                print(" You're a Genius!")
                break

            else:
                print("Wrong Guess. Try Again!")

        else:
            print("Please enter a number between 1 and 10.")

    except ValueError:
        print("Please enter only numbers.")
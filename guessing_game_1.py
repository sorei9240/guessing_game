import random

def guessing_game():
    secret_number = random.randint(1, 20)
    num_guesses = 0
    
    while True:
        user_guess = int(input("Pick a number between 1 and 20. "))
        if user_guess > secret_number:
            num_guesses += 1
            if num_guesses > 5:
                print("You lose")
                break
            print("Too high, try again.")

        elif user_guess < secret_number:
            num_guesses += 1
            if num_guesses > 5:
                print("You lose")
                break
            print("Too low, try again")
        else:
            print(f"That's right! The secret number was {secret_number}. You got it in {num_guesses} tries.")
            break

guessing_game()
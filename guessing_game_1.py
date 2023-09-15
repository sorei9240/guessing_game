#import random module
import random
#define guessing game function
def guessing_game():
    print("Welcome to the number guessing game. You have 5 tries to guess the correct number.")
    secret_number = random.randint(1, 20) #generates secret number
    num_guesses = 0 #counter variable for attempts
    remaining = 5 #counter variable for remaining attempts

    while True:
        #user prompted to guess a number
        user_guess = int(input("Pick a whole number between 1 and 20. ")) 
        if user_guess > secret_number: 
            num_guesses += 1 #put attempt counter up
            remaining += -1 #subtract from remaining attempts
            if num_guesses > 4: #checks to see if user has attempts left
                print("You lose, better luck next time.")
                break #stops program because user has no remaining attempts
            print(f"Too high, try again. You have {remaining} attempt(s) left.") 

        elif user_guess < secret_number: 
            num_guesses += 1 
            remaining += -1 
            if num_guesses > 4: 
                print("You lose, better luck next time.")
                break 
            print(f"Too low, try again. You have {remaining} attempt(s) left.") 

        else: 
            print(f"That's right! The secret number is {secret_number}. You got it in {num_guesses + 1} attempt(s).") #displays secret number and attempts
            break #stops program because user has won

guessing_game()

def play_again():
    while True:
        replay = input("Would you like to play again? (yes/no) ").lower()
        if replay == "yes":
            guessing_game()
        else:
            print("Thanks for playing!")
            break
play_again()
#import random module
import random
#define guessing game function
def guessing_game():
    print("Welcome to the number guessing game! You have four difficulty levels to choose from:")
    print("Easy gives you 10 attempts to guess a number between 1 and 50.")
    print("Medium gives you 5 attempts to guess a number between 1 and 50.")
    print("Hard gives you 5 attempts to guess a number between 1 and 100.")
    print("Impossible gives you 1 attempt to guess a number between 1 and 100.")
    
    while True:
        level = input("Please type easy, medium, hard or impossible to select your difficulty level: ").lower()
        if level == "easy":
            print("Going with the safe choice. Okay.")
            maximum = 50
            minimum = 1
            max_guesses = 10
            break
        elif level == "medium":
            print("Middle of the road, nothing wrong with that.")
            maximum = 50
            minimum = 1
            max_guesses = 5
            break
        elif level == "hard":
            print("Up for a challenge?")
            maximum = 100
            minimum = 1
            max_guesses = 5
            break
        elif level == "impossible":
            print("Feeling lucky are we?")
            maximum = 100
            minimum = 1
            max_guesses = 1
            break
        else:
            print("invalid input")
        
    num_guesses = 0 #counter variable for attempts
    remaining = max_guesses #counter variable for remaining attempts
    secret_number = random.randint(minimum, maximum) #generates secret number

    while True:
        #user prompted to guess a number
        user_guess = int(input(f"Pick a whole number between {minimum} and {maximum}. "))
        
        if user_guess > maximum or user_guess < minimum:
            print(f"Please pick a number between {minimum} and {maximum}.") 

        elif user_guess > secret_number: 
            num_guesses += 1 #put attempt counter up
            remaining += -1 #subtract from remaining attempts
            if remaining < 1: #checks to see if user has attempts left
                print(f"You lose. The secret number was {secret_number}, better luck next time.")
                break #stops program because user has no remaining attempts
            print(f"Too high, try again. You have {remaining} attempt(s) left.") 

        elif user_guess < secret_number: 
            num_guesses += 1 
            remaining += -1 
            if remaining < 1: 
                print(f"You lose. The secret number was {secret_number}, better luck next time.")
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
        elif replay == "no":
            print("Thanks for playing, see you next time!")
            break
        else:
            print("Invalid input, please type yes or no.")
play_again()
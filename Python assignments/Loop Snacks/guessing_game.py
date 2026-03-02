# prompt the user to guess a number
# initialise the secret number and guess
# use a while loop to keep asking the user for input until the guess is correct, with the condition of our guess not equal to secret number
# use if and else statements to check if the input is too high or too low or correct and display it accordingly
def guessing_game():
    guess = -1
    secret_number = 5


    while guess != secret_number:
        guess = int(input("Guess the number: "))
        if guess < secret_number:
            print("Your guess is too low")
        elif guess > secret_number:
            print("Your guess is too high")
        else :
            print("You are correct!")
guessing_game()

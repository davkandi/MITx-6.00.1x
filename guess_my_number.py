print("Please think of a number between 0 and 100!")

low = 0
high = 100

while True:
    secret = (low + high) // 2
    print(f"Is your secret number {secret}?")
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if guess == 'h':
        high = secret
    elif guess == 'l':
        low = secret
    elif guess == 'c':
        print(f"Game over. Your secret number was: {secret}")
        break
    else:
        print("Sorry, I did not understand your input.")

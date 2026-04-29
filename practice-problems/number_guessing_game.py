# number_guessing_game.py

secret_number = 7
attempts = 0

while True:
    n = int(input("Guess the number (1-10): "))
    attempts += 1

    if n == secret_number:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
    elif n < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
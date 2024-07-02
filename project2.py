def set_secret_number():
    while True:
        secret = input("Player 1, set a multi-digit secret number: ")
        if secret.isdigit():
            return secret
        else:
            print("Invalid input. Please enter a valid multi-digit number.")

def get_guess():
    while True:
        guess = input("Player 2, enter your guess: ")
        if guess.isdigit():
            return guess
        else:
            print("Invalid input. Please enter a valid multi-digit number.")

def provide_hint(secret, guess):
    correct_digits = sum(1 for s, g in zip(secret, guess) if s == g)
    print(f"Hint: You have {correct_digits} digit(s) correct.")

def play_round(player_num, secret):
    attempts = 0
    while True:
        guess = get_guess()
        attempts += 1
        if guess == secret:
            print(f"Player {player_num} guessed the number in {attempts} attempts!")
            return attempts
        else:
            provide_hint(secret, guess)

def mastermind_game():
    print("Welcome to the Mastermind Game!")

    # Player 1 sets the secret number
    print("Player 1's turn to set the secret number.")
    secret1 = set_secret_number()
    print("\n" * 50)  # Clear the screen for secrecy

    # Player 2 guesses the number
    print("Player 2's turn to guess the secret number.")
    attempts1 = play_round(2, secret1)

    # Player 2 sets the secret number
    print("Player 2's turn to set the secret number.")
    secret2 = set_secret_number()
    print("\n" * 50)  # Clear the screen for secrecy

    # Player 1 guesses the number
    print("Player 1's turn to guess the secret number.")
    attempts2 = play_round(1, secret2)

    # Determine the winner
    if attempts1 < attempts2:
        print("Player 1 wins and is crowned the mastermind!")
    elif attempts2 < attempts1:
        print("Player 2 wins and is crowned the mastermind!")
    else:
        print("It's a tie! Both players guessed the numbers in the same number of attempts.")

if __name__ == "__main__":
    mastermind_game()

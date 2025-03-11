import random
import time

def display_welcome_message():
    print(
        """
        Welcome to the Number Guessing Game!
        I'm thinking of a number between 1 and 100.

        Please select the difficulty level:
        1. Easy (10 attempts)
        2. Medium (5 attempts)
        3. Hard (3 attempts)
        """
    )

def get_difficulty_choice():
    """Gets the player's difficulty choice and validates it."""
    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_player_ready():
    """Asks the player if they are ready to start."""
    while True:
        is_ready = input("Are you ready to start? Enter `yes (y)` or `no (n)`: ").lower()
        if is_ready in ("yes", "y", "no", "n"):
            return is_ready in ("yes", "y")
        else:
            print("Invalid answer.")

def get_player_guess():
    """Gets a valid guess from the player."""
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess > 0:
                return guess
            else:
                print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_round(attempts):
    """Plays a single round of the guessing game."""
    random_number = random.randint(1, 100)

    start_time = time.time()

    for attempt in range(1, attempts + 1):
        guess = get_player_guess()

        if guess == random_number:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Congratulations! You guessed the correct number in {attempt} attempts. Your time: {elapsed_time:.2f} seconds")
            return True  # Player won

        elif guess < random_number:
            print(f"Incorrect! The number is greater than {guess}")
        else:
            print(f"Incorrect! The number is less than {guess}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f"Sorry, you lost. The number was {random_number}. Your time: {elapsed_time:.2f} seconds")
    return False


def game(choice: int):
    """Main game logic, including multiple rounds."""
    attempts_dict = {1: 10, 2: 5, 3: 3}
    attempts = attempts_dict[choice]

    print("It's your first round! Good luck!")

    if not get_player_ready():
        print("No problem! You can play anytime you want.")
        return

    while True:
        play_round(attempts)
        play_again = input("Do you want to play again? Enter `yes (y)` or `no (n)`: ").lower()
        if play_again not in ("yes", "y"):
            break

    print("No problem! You can play anytime you want.")

def main():
    """Main function to start the game."""
    display_welcome_message()
    choice = get_difficulty_choice()
    game(choice)

if __name__ == "__main__":
    main()

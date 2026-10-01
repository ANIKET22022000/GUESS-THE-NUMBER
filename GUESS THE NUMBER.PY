# ============================================================
#                 GUESS THE NUMBER GAME
# ============================================================
# A beginner-friendly Python number guessing game
# Features:
# - Multiple difficulty levels
# - Custom difficulty
# - Score system
# - Hints
# - Guess history
# - Statistics
# - Player name
# - Replay system
# ============================================================

import random
import time


# ------------------------------------------------------------
# GLOBAL VARIABLES
# ------------------------------------------------------------

games_played = 0
games_won = 0
total_score = 0
best_score = 0
player_name = ""


# ------------------------------------------------------------
# COLORS FOR TERMINAL
# ------------------------------------------------------------

RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"


# ------------------------------------------------------------
# CLEAR SCREEN
# ------------------------------------------------------------

def clear_screen():
    print("\n" * 3)


# ------------------------------------------------------------
# GAME TITLE
# ------------------------------------------------------------

def show_title():
    print(CYAN + "=" * 60 + RESET)
    print(MAGENTA + "              GUESS THE NUMBER GAME" + RESET)
    print(CYAN + "=" * 60 + RESET)
    print()


# ------------------------------------------------------------
# INTRODUCTION
# ------------------------------------------------------------

def introduction():
    global player_name

    print(YELLOW + "Welcome to Guess The Number!" + RESET)
    print("I have selected a secret number.")
    print("Your job is to guess it correctly.")
    print()

    if player_name == "":
        player_name = input("Enter your name: ").strip()

        if player_name == "":
            player_name = "Player"

    print()
    print(GREEN + "Hello, " + player_name + "!" + RESET)
    print("Let's see how good your guessing skills are.")
    print()


# ------------------------------------------------------------
# DIFFICULTY MENU
# ------------------------------------------------------------

def difficulty_menu():
    print(BLUE + "-" * 60 + RESET)
    print("                    DIFFICULTY")
    print(BLUE + "-" * 60 + RESET)

    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Extreme")
    print("5. Custom")
    print()

    while True:
        choice = input("Choose difficulty (1-5): ")

        if choice == "1":
            return 1, 50, 10

        elif choice == "2":
            return 2, 100, 8

        elif choice == "3":
            return 3, 500, 10

        elif choice == "4":
            return 4, 1000, 7

        elif choice == "5":
            return custom_difficulty()

        else:
            print(RED + "Invalid choice. Try again." + RESET)


# ------------------------------------------------------------
# CUSTOM DIFFICULTY
# ------------------------------------------------------------

def custom_difficulty():
    print()
    print(YELLOW + "CUSTOM DIFFICULTY" + RESET)

    while True:
        try:
            maximum = int(input("Enter maximum number: "))

            if maximum < 10:
                print("Maximum number must be at least 10.")
            else:
                break

        except ValueError:
            print(RED + "Please enter a valid number." + RESET)

    while True:
        try:
            attempts = int(input("Enter number of attempts: "))

            if attempts < 1:
                print("Attempts must be at least 1.")
            else:
                break

        except ValueError:
            print(RED + "Please enter a valid number." + RESET)

    return 5, maximum, attempts


# ------------------------------------------------------------
# DIFFICULTY NAME
# ------------------------------------------------------------

def get_difficulty_name(level):
    if level == 1:
        return "Easy"

    elif level == 2:
        return "Medium"

    elif level == 3:
        return "Hard"

    elif level == 4:
        return "Extreme"

    else:
        return "Custom"


# ------------------------------------------------------------
# SHOW GAME RULES
# ------------------------------------------------------------

def show_rules():
    print(CYAN + "=" * 60 + RESET)
    print("                       GAME RULES")
    print(CYAN + "=" * 60 + RESET)

    print("1. A random number will be generated.")
    print("2. You must guess the secret number.")
    print("3. You will receive higher/lower hints.")
    print("4. You have limited attempts.")
    print("5. Your score depends on your performance.")
    print("6. You can use special hints during the game.")
    print()

    input("Press ENTER to continue...")


# ------------------------------------------------------------
# GENERATE SECRET NUMBER
# ------------------------------------------------------------

def generate_number(maximum):
    return random.randint(1, maximum)


# ------------------------------------------------------------
# CALCULATE DISTANCE
# ------------------------------------------------------------

def calculate_distance(guess, secret):
    return abs(guess - secret)


# ------------------------------------------------------------
# TEMPERATURE HINT
# ------------------------------------------------------------

def temperature_hint(guess, secret, maximum):
    distance = calculate_distance(guess, secret)

    if distance <= maximum * 0.02:
        return "🔥 VERY HOT!"

    elif distance <= maximum * 0.05:
        return "🌡️ HOT!"

    elif distance <= maximum * 0.10:
        return "🙂 WARM!"

    elif distance <= maximum * 0.20:
        return "😐 COOL!"

    else:
        return "🥶 COLD!"


# ------------------------------------------------------------
# HIGHER / LOWER HINT
# ------------------------------------------------------------

def direction_hint(guess, secret):
    if guess < secret:
        return "The secret number is HIGHER."

    elif guess > secret:
        return "The secret number is LOWER."

    else:
        return "You found the number!"


# ------------------------------------------------------------
# SPECIAL HINT
# ------------------------------------------------------------

def special_hint(secret, maximum):
    hint_type = random.randint(1, 5)

    if hint_type == 1:
        if secret % 2 == 0:
            return "Hint: The number is EVEN."
        else:
            return "Hint: The number is ODD."

    elif hint_type == 2:
        if secret % 5 == 0:
            return "Hint: The number is divisible by 5."
        else:
            return "Hint: The number is NOT divisible by 5."

    elif hint_type == 3:
        middle = maximum // 2

        if secret <= middle:
            return "Hint: The number is in the LOWER half."
        else:
            return "Hint: The number is in the UPPER half."

    elif hint_type == 4:
        last_digit = secret % 10
        return "Hint: The last digit is " + str(last_digit) + "."

    else:
        if secret < 10:
            return "Hint: The number has only ONE digit."
        elif secret < 100:
            return "Hint: The number has TWO digits."
        else:
            return "Hint: The number has THREE or more digits."


# ------------------------------------------------------------
# SCORE CALCULATION
# ------------------------------------------------------------

def calculate_score(maximum, attempts_left, total_attempts):
    base_score = maximum

    bonus = attempts_left * 50

    accuracy_bonus = 0

    if total_attempts <= 2:
        accuracy_bonus = 200

    elif total_attempts <= 4:
        accuracy_bonus = 100

    elif total_attempts <= 6:
        accuracy_bonus = 50

    score = base_score + bonus + accuracy_bonus

    return score


# ------------------------------------------------------------
# WIN MESSAGE
# ------------------------------------------------------------

def win_message(score, attempts):
    print()
    print(GREEN + "=" * 60 + RESET)
    print(GREEN + "                 CONGRATULATIONS!" + RESET)
    print(GREEN + "=" * 60 + RESET)

    print("You guessed the number correctly!")
    print("Attempts used:", attempts)
    print("Your score:", score)

    if score >= 1000:
        print(MAGENTA + "Rating: LEGENDARY!" + RESET)

    elif score >= 700:
        print(YELLOW + "Rating: EXCELLENT!" + RESET)

    elif score >= 500:
        print(CYAN + "Rating: VERY GOOD!" + RESET)

    elif score >= 300:
        print("Rating: GOOD!")

    else:
        print("Rating: NICE TRY!")


# ------------------------------------------------------------
# LOSE MESSAGE
# ------------------------------------------------------------

def lose_message(secret):
    print()
    print(RED + "=" * 60 + RESET)
    print(RED + "                  GAME OVER!" + RESET)
    print(RED + "=" * 60 + RESET)

    print("You used all your attempts.")
    print("The secret number was:", secret)
    print("Better luck next time!")


# ------------------------------------------------------------
# SHOW GUESS HISTORY
# ------------------------------------------------------------

def show_history(history, secret):
    print()
    print(BLUE + "-" * 60 + RESET)
    print("                    GUESS HISTORY")
    print(BLUE + "-" * 60 + RESET)

    if len(history) == 0:
        print("No guesses were made.")
        return

    for index, guess in enumerate(history, start=1):

        if guess == secret:
            status = "CORRECT"

        elif guess < secret:
            status = "Too Low"

        else:
            status = "Too High"

        print(str(index) + ". " + str(guess) + " -> " + status)


# ------------------------------------------------------------
# GAME STATISTICS
# ------------------------------------------------------------

def show_statistics():
    print()
    print(CYAN + "=" * 60 + RESET)
    print("                    GAME STATISTICS")
    print(CYAN + "=" * 60 + RESET)

    print("Player:", player_name)
    print("Games Played:", games_played)
    print("Games Won:", games_won)

    if games_played > 0:
        win_rate = (games_won / games_played) * 100
    else:
        win_rate = 0

    print("Win Rate:", round(win_rate, 2), "%")
    print("Total Score:", total_score)
    print("Best Score:", best_score)

    print()


# ------------------------------------------------------------
# NUMBER VALIDATION
# ------------------------------------------------------------

def get_guess(maximum):
    while True:

        user_input = input(
            "Enter your guess (1-" + str(maximum) + "): "
        )

        try:
            guess = int(user_input)

            if guess < 1 or guess > maximum:
                print(
                    RED
                    + "Please enter a number between 1 and "
                    + str(maximum)
                    + "."
                    + RESET
                )
            else:
                return guess

        except ValueError:
            print(RED + "Invalid input. Enter a number." + RESET)


# ------------------------------------------------------------
# USE SPECIAL HINT
# ------------------------------------------------------------

def ask_for_hint(secret, maximum, hint_used):
    if hint_used:
        print(YELLOW + "You already used your special hint!" + RESET)
        return True

    answer = input("Do you want to use a special hint? (y/n): ")

    if answer.lower() == "y":
        print()
        print(CYAN + special_hint(secret, maximum) + RESET)
        return True

    return False


# ------------------------------------------------------------
# PLAY ONE GAME
# ------------------------------------------------------------

def play_game():
    global games_played
    global games_won
    global total_score
    global best_score

    clear_screen()
    show_title()

    level, maximum, max_attempts = difficulty_menu()

    difficulty_name = get_difficulty_name(level)

    secret = generate_number(maximum)

    history = []

    attempts_left = max_attempts
    attempts_used = 0
    hint_used = False

    games_played += 1

    print()
    print(CYAN + "=" * 60 + RESET)
    print("Difficulty:", difficulty_name)
    print("Number range: 1 to", maximum)
    print("Attempts:", max_attempts)
    print(CYAN + "=" * 60 + RESET)
    print()

    while attempts_left > 0:

        print(
            YELLOW
            + "Attempts remaining:"
            + RESET,
            attempts_left
        )

        if not hint_used:
            print("Type 'hint' if you want a special hint.")

        user_input = input("Enter your guess: ")

        if user_input.lower() == "hint":

            hint_used = ask_for_hint(
                secret,
                maximum,
                hint_used
            )

            print()
            continue

        try:
            guess = int(user_input)

        except ValueError:
            print(RED + "Please enter a valid number." + RESET)
            print()
            continue

        if guess < 1 or guess > maximum:
            print(
                RED
                + "Your guess must be between 1 and "
                + str(maximum)
                + "."
                + RESET
            )
            print()
            continue

        history.append(guess)

        attempts_used += 1
        attempts_left -= 1

        print()

        if guess == secret:

            games_won += 1

            score = calculate_score(
                maximum,
                attempts_left,
                attempts_used
            )

            total_score += score

            if score > best_score:
                best_score = score

            win_message(score, attempts_used)

            print()
            print(temperature_hint(
                guess,
                secret,
                maximum
            ))

            show_history(history, secret)

            return

        else:

            print(direction_hint(guess, secret))

            print(
                temperature_hint(
                    guess,
                    secret,
                    maximum
                )
            )

            if attempts_left == 0:
                lose_message(secret)

                show_history(
                    history,
                    secret
                )

                return

        print()


# ------------------------------------------------------------
# PLAY AGAIN
# ------------------------------------------------------------

def play_again():
    print()
    print(CYAN + "-" * 60 + RESET)

    while True:

        answer = input("Do you want to play again? (y/n): ")

        if answer.lower() == "y":
            return True

        elif answer.lower() == "n":
            return False

        else:
            print("Please enter y or n.")


# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------

def main_menu():
    while True:

        clear_screen()
        show_title()

        print("Player:", player_name)
        print()

        print("1. Start Game")
        print("2. Game Rules")
        print("3. Statistics")
        print("4. Change Player Name")
        print("5. Exit")
        print()

        choice = input("Select an option: ")

        if choice == "1":
            play_game()

            if not play_again():
                print()
                print("Returning to main menu...")

        elif choice == "2":
            clear_screen()
            show_rules()

        elif choice == "3":
            clear_screen()
            show_statistics()
            input("Press ENTER to continue...")

        elif choice == "4":
            change_player_name()

        elif choice == "5":
            exit_game()
            break

        else:
            print(
                RED
                + "Invalid option. Please choose 1-5."
                + RESET
            )

            time.sleep(1)


# ------------------------------------------------------------
# CHANGE PLAYER NAME
# ------------------------------------------------------------

def change_player_name():
    global player_name

    print()
    print(YELLOW + "CHANGE PLAYER NAME" + RESET)

    new_name = input("Enter new name: ").strip()

    if new_name == "":
        print(
            RED
            + "Name cannot be empty."
            + RESET
        )

    else:
        player_name = new_name

        print(
            GREEN
            + "Name changed successfully!"
            + RESET
        )

    time.sleep(1)


# ------------------------------------------------------------
# EXIT GAME
# ------------------------------------------------------------

def exit_game():
    print()
    print(CYAN + "=" * 60 + RESET)
    print("                 THANK YOU FOR PLAYING")
    print(CYAN + "=" * 60 + RESET)

    print()
    print("Player:", player_name)
    print("Games Played:", games_played)
    print("Games Won:", games_won)
    print("Total Score:", total_score)
    print("Best Score:", best_score)

    print()
    print(
        GREEN
        + "Keep practicing your Python skills!"
        + RESET
    )

    print()


# ------------------------------------------------------------
# START PROGRAM
# ------------------------------------------------------------

def main():

    global player_name

    clear_screen()
    show_title()

    print("Welcome to the Python Guess The Number Game!")
    print()

    player_name = input("Enter your name: ").strip()

    if player_name == "":
        player_name = "Player"

    print()
    print(
        GREEN
        + "Welcome, "
        + player_name
        + "!"
        + RESET
    )

    time.sleep(1)

    main_menu()


# ------------------------------------------------------------
# PROGRAM ENTRY POINT
# ------------------------------------------------------------

if __name__ == "__main__":
    main()
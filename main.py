from wordlisst import words
import random

hangman_art = {
    0: [
        "   ",
        "   ",
        "   "
    ],
    1: [
        " o ",
        "   ",
        "   "
    ],
    2: [
        " o ",
        " | ",
        "   "
    ],
    3: [
        " o ",
        "/| ",
        "   "
    ],
    4: [
        " o ",
        "/|\\",
        "   "
    ],
    5: [
        " o ",
        "/|\\",
        "/  "
    ],
    6: [
        " o ",
        "/|\\",
        "/ \\"
    ]
}


def display_hangman(wrong_guesses):
    print("*******************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*******************")


def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def has_won(hint):
    return "_" not in hint

def get_difficulity_level(level):
    levels = ["easy", "medium", "hard"]
    while level not in levels:
        level = input("Choose a difficulty level (easy, medium, hard): ").lower()
    if level == "easy":
        return {"reward_multiplier": 1.0, "penalty_multiplier": 0.5}
    elif level == "medium":
        return {"reward_multiplier": 1.0, "penalty_multiplier": 1.0}
    elif level == "hard":
        return {"reward_multiplier": 0.75, "penalty_multiplier": 1.5}


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    multiple_correct_guesses = 0
    wrong_streaks = 0
    level = input("Choose a difficulty level (easy, medium, hard): ").lower()
    difficulty = get_difficulity_level(level)
    points = int(20 / difficulty["penalty_multiplier"])

    while True:
        display_hangman(wrong_guesses)
        display_hint(hint)
        if len((guessed_letters)) > 0:
            print(f"Already guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Points: {points}")
        print(f"Wrong guesses: {wrong_guesses}")
        
        if has_won(hint):
            print("GG, you won!")
            if wrong_guesses == 0:
                print("You guessed it without any mistakes!")
            else:
                display_hangman(wrong_guesses)
            display_answer(answer)
            print(f"Total points: {points}")
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)
        
        if guess in answer:
            wrong_streaks = 0
            multiple_correct_guesses += 1
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
            points += int(10 * multiple_correct_guesses * difficulty["reward_multiplier"])

        else:
            wrong_streaks += 1
            multiple_correct_guesses = 0
            wrong_guesses += 1
            if points > 0:
                points -= int(5 * wrong_streaks * difficulty["penalty_multiplier"])
        
        if wrong_guesses == len(hangman_art) - 1 or points <= 0:
            print("You lost!")
            print("The answer was:")
            display_answer(answer)
            break

if __name__ == "__main__":
    main()


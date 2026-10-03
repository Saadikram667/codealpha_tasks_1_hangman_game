import random

WORDS = [
    "Lantern", "Whisper", "Cobalt", "Meadow", "Quartz",
    "Voyage", "Ember", "Tundra", "Mosaic", "Harbor",
]

# Normalize once so every comparison is case-insensitive
list_of_words = [w.lower() for w in WORDS]


def computer_guess_word(list_of_words, length_of_word, max_choices=6):
    """The computer guesses the word YOU are thinking of."""
    possible_words = [w.lower() for w in list_of_words if len(w) == length_of_word]

    if not possible_words:
        print(f"No words of length {length_of_word} were found in the provided list.")
        return

    guessed_letters = set()
    remaining_choices = max_choices

    while remaining_choices > 0 and len(possible_words) > 1:
        # Count how many candidate words contain each unguessed letter
        counts = {}
        for word in possible_words:
            for char in set(word):
                if char not in guessed_letters:
                    counts[char] = counts.get(char, 0) + 1

        # Letters in every word (or none) tell us nothing, so skip them
        total = len(possible_words)
        informative = {c: n for c, n in counts.items() if 0 < n < total}
        if not informative:
            break

        # Pick the letter that splits the candidates most evenly
        letter = max(informative, key=lambda c: min(informative[c], total - informative[c]))
        guessed_letters.add(letter)

        while True:
            check = input(f"Is the letter '{letter}' in your word? (y/n): ").strip().lower()
            if check in ("y", "n"):
                break
            print("Invalid input! Please enter 'y' or 'n'.")

        if check == "y":
            possible_words = [w for w in possible_words if letter in w]
        else:
            possible_words = [w for w in possible_words if letter not in w]
            remaining_choices -= 1

    if len(possible_words) == 1:
        print(f"The word you thought of was: {possible_words[0]}")
    elif not possible_words:
        print("No matching words found. Please check that your answers were consistent!")
    else:
        print(f"I couldn't narrow it down fully. Remaining candidates: {possible_words}")


def human_guess_word(list_of_words, max_choices=6):
    """YOU guess the word the computer picked."""
    secret_word = random.choice(list_of_words).lower()
    guessed_letters = set()
    remaining_choices = max_choices

    print(f"I have picked a {len(secret_word)}-letter word! "
          f"You have {max_choices} incorrect guesses allowed.")

    while remaining_choices > 0:
        display_word = " ".join(c if c in guessed_letters else "_" for c in secret_word)
        print(f"\nWord: {display_word}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Remaining attempts: {remaining_choices}")

        if "_" not in display_word:
            print(f"\nCongratulations! You correctly guessed the word: '{secret_word}'")
            return

        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter (a-z).")
            continue
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Correct! '{guess}' is in the word.")
        else:
            print(f"Wrong! '{guess}' is not in the word.")
            remaining_choices -= 1

    # The loop also exits right after the final correct letter is guessed,
    # so check for a win before declaring a loss
    if all(c in guessed_letters for c in secret_word):
        print(f"\nCongratulations! You correctly guessed the word: '{secret_word}'")
    else:
        print(f"\nGame Over! You ran out of attempts. The secret word was: '{secret_word}'")


def main():
    mode = input("Who guesses? (1 = you, 2 = computer): ").strip()
    if mode == "2":
        try:
            n = int(input("How many letters is your word? ").strip())
        except ValueError:
            print("Please enter a number.")
            return
        computer_guess_word(list_of_words, n)
    else:
        human_guess_word(list_of_words)


if __name__ == "__main__":
    main()
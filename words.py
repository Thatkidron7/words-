import random

# Word lists stored directly in the code
def get_word_list(difficulty):
    words = {
        "easy": ["cat", "dog", "sun", "hat", "pen", "cup", "book", "ball", "fish", "tree"],
        "medium": ["python", "guitar", "planet", "bottle", "rocket", "window", "castle", "jungle", "mirror", "hunter"],
        "hard": ["pneumonia", "algorithm", "xylophone", "jurisdiction", "metamorphosis", "psychology", "philosopher", "engineering", "microscope", "quadrilateral"]
    }
    return words.get(difficulty, [])

def get_random_word(word_list):
    return random.choice(word_list) if word_list else "default"

def scramble_word(word):
    return "".join(random.sample(word, len(word)))

def play_game(word_list):
    word_to_guess = get_random_word(word_list).strip().lower()
    scrambled_word = scramble_word(word_to_guess)
    attempts = 0
    hints_given = 0

    print(f"Unscramble this word: {scrambled_word}")

    while True:
        guess = input("Your guess: ").strip().lower()

        if guess == word_to_guess:
            print("Correct! You guessed the word.")

            option = input("Do you want to (1) continue or (2) switch difficulty? (1/2): ").strip()
            while option not in ["1", "2"]:
                print("Invalid option. Please enter 1 to continue or 2 to switch difficulty.")
                option = input("Do you want to (1) continue or (2) switch difficulty? (1/2): ").strip()

            if option == "1":
                return play_game(word_list)
            elif option == "2":
                return select_difficulty()

        else:
            attempts += 1
            print("Wrong guess! Try again.")

            if attempts == 2:
                hints_given += 1
                print(f"Hint: The word starts with '{word_to_guess[0]}'")
            elif attempts == 3:
                hints_given += 1
                print(f"Hint: The word starts with '{word_to_guess[0]}' and second letter is '{word_to_guess[1]}'")
            elif attempts >= 4:
                option = input("Do you want to (1) give up and see the answer, or (2) switch difficulty? (1/2): ").strip()
                if option == "1":
                    print(f"The word was: {word_to_guess}")
                    break
                elif option == "2":
                    return select_difficulty()
                else:
                    print("Invalid option, try again.")

def select_difficulty():
    difficulty = input("Choose difficulty (easy, medium, hard): ").strip().lower()
    while difficulty not in ["easy", "medium", "hard"]:
        print("Invalid difficulty. Choose easy, medium, or hard.")
        difficulty = input("Choose difficulty (easy, medium, hard): ").strip().lower()

    word_list = get_word_list(difficulty)
    play_game(word_list)

if __name__ == "__main__":
    select_difficulty()

import random
def hangman():
    words = ['python', 'programming', 'hangman', 'challenge']
    word = random.choice(words)
    guessed = "_" * len(word)
    guessed = list(guessed)
    attempts = 6
    while attempts > 0:
        print(" ".join(guessed))
        guess = input("Guess a letter: ").lower()
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print(f"Wrong! {attempts} attempts left.")
        if "_" not in guessed:
            print("You won!")
            break
    else:
        print(f"You lost! The word was {word}.")
hangman()
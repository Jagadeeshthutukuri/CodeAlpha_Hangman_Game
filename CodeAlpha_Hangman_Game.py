import random

# Predefined words with hints
words_with_hints = {
    "apple": "A fruit that keeps the doctor away.",
    "tiger": "A wild animal with black stripes.",
    "house": "A place where people live.",
    "train": "Moves on tracks and carries passengers.",
    "water": "Essential for life, you drink it."
}

# Randomly select a word and its hint
word, hint = random.choice(list(words_with_hints.items()))
word_letters = list(word)
display = ['_' for _ in word_letters]

# Tracking guesses
correct_guesses = []
wrong_guesses = []
MAX_TRIES = 6

print("🎯 Welcome to Hangman!")
print("Hint: ", hint)
print(f"You have {MAX_TRIES} wrong attempts allowed.\n")

# Game loop
while len(wrong_guesses) < MAX_TRIES and '_' in display:
    print("Word: ", ' '.join(display))
    print("✅ Correct guesses:", ', '.join(correct_guesses) or "-")
    print("❌ Wrong guesses  :", ', '.join(wrong_guesses) or "-")
    
    guess = input("Enter a letter: ").lower()

    # Input validation
    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single alphabet letter.\n")
        continue

    if guess in correct_guesses or guess in wrong_guesses:
        print("🔁 You already guessed that letter.\n")
        continue

    # Check the guess
    if guess in word_letters:
        correct_guesses.append(guess)
        for i, letter in enumerate(word_letters):
            if letter == guess:
                display[i] = guess
        print("✅ Correct!\n")
    else:
        wrong_guesses.append(guess)
        print(f"❌ Wrong guess! You have {MAX_TRIES - len(wrong_guesses)} tries left.\n")

# Game result
print("\n📢 Final Word: ", ' '.join(display))
if '_' not in display:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("💀 Game Over! The correct word was:", word)

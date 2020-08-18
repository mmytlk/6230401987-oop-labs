i = 2
secret_word = "kku"

while True:
    word = input("Enter a word: ")
    if i == 0:
        print("Incorrect! You have 0 guesses left.")
        print("Thanks for trying, but the secret word is "
            "actually: %s" % secret_word)
        break
    elif word == secret_word:
        print("Congrats that you can guess the secret word correctly")
        break
    elif word != secret_word:
        print(f"Incorrect! You have {i} guesses left.")
        i -= 1

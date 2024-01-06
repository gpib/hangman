import random
#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = word_list[random.randint(0, len(word_list)-1)]

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#guess = input("Guess a letter").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
mistery_word =""
for character in range(0, len(chosen_word)):
    mistery_word += "_"
print(mistery_word)
while chosen_word != mistery_word:
    guess = input("Guess a letter").lower()
    cnt = -1
    for letter in chosen_word:
        cnt += 1
        if letter == guess:
            print(f"Current letter {letter} and current guess {guess}")
            mistery_word = mistery_word[:cnt] + letter + mistery_word[cnt+1:]
            print(mistery_word)
    print(mistery_word)

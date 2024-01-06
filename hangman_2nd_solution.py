import random
#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = word_list[random.randint(0, len(word_list)-1)]
hidden_chosen_word =[]
for _ in chosen_word:
    hidden_chosen_word.append("_")
print(f"Here is the chosen word: {chosen_word} \n"
      f"and here is the hidden version {hidden_chosen_word}")

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.


#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
end_of_the_game = False
while not end_of_the_game:
    print(f"Chosen word {chosen_word} \n"
          f"guess word {hidden_chosen_word}")
    guess = input("Guess a letter").lower()
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            hidden_chosen_word[position] = chosen_word[position]

    print(hidden_chosen_word)
    if "_" not in hidden_chosen_word:
        end_of_the_game = True


""" old version
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
"""
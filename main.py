#Step 4

import random
import hangman_art
import hangman_words_list
print (hangman_art.logo)


end_of_game = False
chosen_word = random.choice(hangman_words_list.word_list)
word_length = len(chosen_word)
lives=6


#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
      lives-=1
      print("HEY YOU ARE MAKING ME KILL!!!! This letter is not in the word. Plz choose another letter")
      if lives==0:
        end_of_game=True
        print("You lose")
    if guess in chosen_word:
      print("Yes this letter is right.You are saving me.Thankx")

    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(hangman_art.stages[lives])


print(f'You made me kill by not able to choose the right word which was {chosen_word}.')

    
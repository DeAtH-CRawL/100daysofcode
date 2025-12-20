import random
import art
import words
lives=6
chosen_word = random.choice(words.word_list)
print(chosen_word)
print(art.logo) 

placeholder = " "
for position in range(len(chosen_word)):
    placeholder += "_ "
print(placeholder)

game_over = False
correct_letters = []
while not game_over:
    print("\n ** * ** * ** * ** * ** * ** * ** * ** * ** * ** * ** * **\n")
    user_guess = input("Guess a letter: ").lower()
    if user_guess in correct_letters:
        print(f"You've already guessed {user_guess}")
        continue

    display=""

    for letter in chosen_word:
        if letter == user_guess:
            display += letter + " "
            correct_letters.append(user_guess)
        elif letter in correct_letters:
            display += letter + " "
        else:
            display += "_ "

    print(display)
    if user_guess not in chosen_word:

        lives -= 1
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
        print(art.stages[lives])
        if lives == 0:
            game_over = True
            print("You lose.")
    if "_" not in display:
        game_over = True
        print('''          _______                             _________ _       
|\     /|(  ___  )|\     /|          |\     /|\__   __/( (    /|
( \   / )| (   ) || )   ( |          | )   ( |   ) (   |  \  ( |
 \ (_) / | |   | || |   | |          | | _ | |   | |   |   \ | |
  \   /  | |   | || |   | |          | |( )| |   | |   | (\ \) |
   ) (   | |   | || |   | |          | || || |   | |   | | \   |
   | |   | (___) || (___) |          | () () |___) (___| )  \  |
   \_/   (_______)(_______)          (_______)\_______/|/    )_)
                                                                ''')
    
    print(art.stages[lives])


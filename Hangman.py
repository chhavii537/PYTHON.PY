import random

stages = [
        """
            +-------+
            |
            |
            | 
            |
            |
         ==============
        """
            ,
        """
            +-------+
            |       |
            |       0
            | 
            |
            |
         ==============
        """
            ,
        """
            +-------+
            |       |
            |       0
            |       |
            |
            |
         ==============
        """
            ,
        """
            +-------+
            |       |
            |       0
            |      -|
            |
            |
         ==============
        """
            ,
        """
            +-------+
            |       |
            |       0
            |      -|-
            |
            |
         ==============
        """
            ,
        """
            +-------+
            |       |
            |       0
            |      -|-
            |      /
            |
         ==============
        """
            ,
        """
            +-------+
            |       |
            |       0
            |      -|-
            |      / \
            |
         ==============
        """]
word_list=["riya","dog","cloud","mouse","sea","cat"]



lives = 6

choosen_word = random.choice(word_list)
print(choosen_word)

place_holder =""
word_length = len(choosen_word)
for position in range(word_length):
    place_holder += "_"
print(place_holder)

game_over = False

correct_letter = []
while not game_over:
    guess =input("guess a letter:").lower()

    display = ""

    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you lose!")
    if "_" not in display:
        game_over = True
        print("You win")
    print(stages[lives])

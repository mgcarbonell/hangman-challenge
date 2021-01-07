import random
import math
#  Welcome to Hangman!!!
#   __________________
# /                  \
#|    ~H A N G M A N~|
#\__________________/
#  We're going to need inputs
#  A list of words - CHECK
#  A randomization definition - CHECK
# a way to use that to pull a random word - CHECK
# a number of rounds = to the list of words 

# a loop that loops through the word to find out how many "spaces" or "characters" there are
# probably another loop to convert # of characters = _
# Need a way to draw the characters
# input for a guess
# 

# Your game will need some state to keep track of the word, how many letters are yet to be guessed, and the current state of the hangman.
# You can initially represent the hangman as a decreasing number of guesses remaining.
# You can use the in keyword to test to see if a letter is in the secret word.
# Remember to account for case differences.
# fisher yates let's goooo

print("Hello, and welcome to a terribly named game!\n")

print("""\
:                  :
:__________________:
|                  |
| (D E A D M A N)  |
'~~~~~~~~~~~~~~~~~~'
*creaking noises*
  """)

player_name = input("What is your name? \n")

print(f"Hello, ", player_name.capitalize(), "let's play....\n D E A D M A N")

def introduction():
  print("Are you familiar with the game?")
  instructions =  input("Press y for yes, or n for no\n")
  if instructions == "y":
    print("Let the 'fun' begin!")
  elif instructions == "n":
      print("It's pretty easy, but...\n You can only guess one letter at a time. Don't forget to press your 'enter key' after each word. Too many guesses.. and well...\n")
      print("""\
     .... NO! ...                  ... MNO! ...
   ..... MNO!! ...................... MNNOO! ...
 ..... MMNO! ......................... MNNOO!! .
..... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
 ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...
    ....... MMMMM..    OPPMMP    .,OMI! ....
     ...... MMMM::   o.,OPMP,.o   ::I!! ...
         .... NNM:::.,,OOPM!P,.::::!! ....
          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
           .. MMMMMNNOOMMNNIIIPPPOO!! ......
          ...... MMMONNMMNNNIIIOO!..........
       ....... MN MOMMMNNNIIIIIO! OO ..........
    ......... MNO! IiiiiiiiiiiiI OOOO ...........
  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
      ...... OO! ................. ON! .......
         ................................
                  courtesy of https://ascii.co.uk/art/skulls
        """)


introduction()

words = ["banana", "mango", "baboon", "arctic", "four", "cat", "skunk", "wild", "west", "wyvern", "cool", "espionage", "gazebo", "frazzled", "mystify", "mnemonic"]

# can we have another bank of words for a "hard mode"
# and then a bank of words for "easy mode"

gallows = ["""\

+----+
    \|
     |
     |
     |
     |
=====+""", """\

+----+
 |  \|
 O   |
     |
     |
     |
=====+""", """\

+----+
 |  \|
 O   |
 T   |
     |
     |
=====+""", """\

+----+
 |  \|
 O   |
|T   |
     |
     |
=====+""", """\

+----+
 |  \|
 O   |
|T|  |
     |
     |
=====+""", """\

+----+
 |  \|
 O   |
|T|  |
 L   |
     |
=====+""", """\

+----+
 |  \|
 O   |
|T|  |
 LL  |
     |
=====+"""]

# for gallow in gallows:
#   print(gallow)


# function to pull a random word...
def get_random(words):
  word_index = random.randint(0, len(words) - 1)
  return words[word_index]

def main_game(misses, corrects, the_word):
# going to need a way to space things out otherwise it smashes stuff together
# print("Welcome to", end=' ')
# print("GeeksforGeeks", end=' ')
# >> Welcome to GeeksforGeeks
# MONEY
  print(gallows[len(misses)])
  print()
  print(f"{player_name}, you've missed these letters: ", end=' ')
  for letter in misses:
    print(letter, end=' ')
  print()

  blank = '_' * len(the_word) #lol looks like an axlotl

  for i in range(len(the_word)):
    if the_word[i] in corrects:
      blank = blank[:i] + the_word[i] + blank[i+1:] 
# so let's add in our spacer so that we can get words like
# b a n a n a to make things SUPER clear...
  for letter in blank:
    print(letter, end=' ')
  print()

def guesses(guessed):
  while True:
    print(f"{player_name}, what do you think the letter is?")
    guess = input()
    guess = guess.lower()
    if len(guess) != 1:
      print(f"Tsk, tsk {player_name} one letter at a time...")
    elif guess in guessed:
      print(f"Hmm... {player_name}, you already guessed that one.")
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
      print(f"You know the rules, {player_name}, enter a LETTER.")
    else:
      return guess

# I played one game that let you see your guesses.
# play again?
def another_one():
  print(f"{player_name} do you want to play again? \n y Yes n. No")
  return input().lower().startswith('y')


# # tracker for game stats?
# 
print('D E A D M A N')
# tracker for incorrect guesses
misses = ''
# tracker for correct guesses
corrects = ''
# grab our random word
# print(get_random(words))
the_word = get_random(words)
# tracker for the game status
done = False

while True:
  # drive the game
  main_game(misses, corrects, the_word)
  # guess
  guess = guesses(misses + corrects)
  # corrects
  if guess in the_word:
    corrects = corrects + guess

    all_letters = True
    for i in range(len(the_word)):
      if the_word[i] not in corrects:
        all_letters = False
        break
    if all_letters:
      print(f"Correct {player_name}! The word is {the_word}!")
      done = True
  #  misses
  else:
    misses = misses + guess
    # if len(misses -1) == len(gallows) - 1:
    # print (f"You have one guess left {player_name}, and their life depends on it...)
    if len(misses) == len(gallows) - 1:
      main_game(misses, corrects, the_word)
      print("Oh no... " + player_name + " you've run out of guesses! \n After " + str(len(misses)) + "missed guesses, and " + str(len(corrects)) + " correct gueses, the word is... " + the_word)
      done = True

  if done:
    if another_one():
      misses = ''
      corrects = ''
      done = False
      the_word = get_random(words)
    else:
      break





# random.shuffle(words) and then take word[0] (or something)
# then pop off the word

# # print(get_random_word(words))

# # split the word
# def split_word(random_word):
#   the_word = list(random_word)
#   return the_word

# split_word(random_word)

# print(split_word(get_random_word))

# def rounds(words):
#   rounds = len(words)
#   return rounds

# print(rounds(words))



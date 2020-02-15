
def displayed_game(attempt, wd):
    if (attempt == 0):
      print("    _____     ")
      print("   |     |    ")
      print("   |          ")
      print("   |          ")
      print("   |          ")
      print("   |          ")
      print("   |          ")
      print("--------------")
    elif (attempt == 1):
      print("    _____     ")
      print("   |     |    ")
      print("   |     O    ")
      print("   |          ")
      print("   |          ")
      print("   |          ")
      print("   |          ")
       print("--------------")
    elif (attempt == 2):
      print("    _____     ")
      print("   |     |    ")
      print("   |     O    ")
      print("   |     |    ")
      print("   |     |    ")
      print("   |          ")
      print("   |          ")
      print("--------------")
      elif (attempt == 3):
      print("    _____     ")
      print("   |     |    ")
      print("   |     O    ")
      print("   |     |    ")
      print("   |     |    ")
      print("   |    /     ")
      print("   |          ")
      print("--------------")
    elif (attempt == 4):
      print("    _____     ")
      print("   |     |    ")
      print("   |     O    ")
      print("   |     |    ")
      print("   |     |    ")
      print("   |    / \   ")
      print("   |          ")
      print("--------------")
    elif (attempt == 5):
      print("    _____     ")
      print("   |     |    ")
      print("   |     O    ")
      print("   |   _ |    ")
      print("   |     |    ")
      print("   |    / \   ")
      print("   |          ")
      print("--------------")
    elif (attempt == 6):
      print("    _____     ")
      print("   |     |    ")
      print("   |     O    ")
      print("   |   _ | _  ")
      print("   |     |    ")
      print("   |    / \   ")
      print("   |          ")
      print("--------------")
return True

#choose a word to play

def choose_word():
 my_word = "hangman"
 hidden_word = my_word
return hidden_word

#Hangman game code

def run_hangman():
  print("Hangman Game")
  hidden_word = choose_word()
  word_template = list("*"*len(hidden_word))
  word_characters = list(solution_word)
  attempt = 7
  number_guesses = []
  
  while lives >= 0:
   if word_template == word_characters
    print("".join(word_template))
    break
   hung = hangman_frames(attempt)
   if hung == True
    break
   valid_guess = False
   while valid_guess == False
    print("Lives remaining = " + str(lives))
    print("".join(word_template))
    guess = input("please enter your next guess: ")
    allowed_guesses = "abcdefghijklmnopqrstuvwxyz"
    if guess.lower() not in allowed allowed_guesses or len(guess) > 1:
      print("Invalid guess - must be single letter")
      valid_guess = False
    elif guess.lower() in guessed_letters:
      print("Invalid guess - letter has already been used")
      valid_guess = False
    else:
      valid_guess = True
   guess = guess.lower()
   guessed_letters.oppened(guess))
   correct = False
   for i in range(len(solution_word)):
     if guess == word_characters[i]:
       word_template[i] = word_characters[i]
       correct = True
   if correct == True
    print("Correct Guess")
      

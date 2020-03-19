import random

#User game display
displayed_game = ['''
      _____     
     |     |    
     |     O     
     |    _|_     
     |     |     
     |    / \   
     |          
  --------------''','''
      _____     
     |     |    
     |     O     
     |    _|_     
     |     |     
     |    /  
     |
  --------------''',''' 
      _____     
     |     |    
     |     O     
     |    _|_     
     |     |     
     |     
     |
  --------------''','''   
      _____     
     |     |    
     |     O     
     |     |_     
     |     |     
     |          
     |          
  --------------''',''' 
      _____     
     |     |    
     |     O     
     |     |     
     |     |     
     |     
     |          
  --------------''','''   
      _____     
     |     |    
     |     O     
     |         
     |         
     |        
     |          
  --------------''',''' 
      _____     
     |     |    
     |        
     |       
     |    
     |      
     |          
  --------------''','''
      _____     
     |        
     |         
     |        
     |     
     |        
     |          
  --------------'''] 
  
def find_word():
 #import random word into game from file:
 #with open('word_list.txt', 'r') as f:
 words = f.read()
 list_words = words.splitlines()
 game_word = random.choice(list_words)
 game_word = game_word.lower()
 return game_word
 
def Hangman():

 #Set up base conditions  
 word = find_word()
 used_characters = []
 valid_character = "abcdefghijklmnopqrstuvwxyz"
 attempts = 7
 guessed = False
 
 #Display Text and Word
 print("LET'S PLAY HANGMAN:")
 print("\n")
 print(len(word) * ' _')
 
 #Game Loop
 while guessed == False and attempts > 0:
   
  print(displayed_game[attempts])
  print("\n")
  print("Remaining attempts = " + str(attempts))
  
  #Character input
  character = input("Please enter your next guess: ")
  character = character.lower()
  
  #Check character against hidden word, ensure valid character
  if len(character) > 1:
   print("Invalid guess - must be single letter")
  elif character not in valid_character:
   print("Invalid guess - must be single letter")
  elif character == " ":
   print("Invalid guess - must be single letter")
  elif character in used_characters:
   print("Invalid guess - letter has already been used")
   
  elif character not in word:
   print("\n")  
   print("Incorrect Guess")
   used_characters.append(character)
   attempts -= 1
   
  elif character in word:
   print("\n")
   print("Correct Guess")
   used_characters.append(character)
 
 #Refresh guess display
  display = ''
  if guessed == False:
   for letter in word:
    if letter in used_characters:
     display += letter
    else:
      display += ' _'
   print(display)

#Set winning/loosing conditons
  if display == word:
   print("\n")
   print("Congratulations you win")
   guessed = True
   
  elif attempts == 0:
   print(displayed_game[0])
   print("\n")  
   print("You loose")
   print("The word was " + word)
    
Hangman()

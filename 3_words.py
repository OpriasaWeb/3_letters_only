# 3-letter word simple game

# Set a empty list here
words = []

# set the game variable to game
game = "play"

# while game is play - continue the loop
while game == "play":
  # the user should input 3 letter word only
  input_word = input("Enter a 3-letter word: ")
  
  # check if the word is less than or greater than 3 letters
  if len(input_word) > 3 or len(input_word) < 3:
    # if so, print this and return to input word
    print("Hey, that is not a 3-letter word.")
  
  else:
    # if the input word is in the words list
    if input_word in words:
      # stop the game because the word should be unique and 3 letters only
      print("You already entered that word. Game over.")
      game = "over"
    else:
      # if the input word is unique and 3 letters only, print it and append it to words list
      print("Nice one!")
      words.append(input_word)
      print(words)
      
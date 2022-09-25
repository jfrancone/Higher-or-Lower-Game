def continue_game(user_choice, winner, score):
  playing_game = True
  if user_choice == winner:
    return playing_game
  else:
    print(f"Sorry, that's wrong. Final score: {score}.")
    playing_game = False
    print(playing_game)
    return playing_game

def add_user_point(user_choice, winner, score):
  if user_choice == winner:
    score += 1
    print(f"You're right! Current score: {score}")
    return score
  else:
    print("Error: user winner is incorrect")
    
  
def celeb_assignment(user_input, celeb1, celeb2):
  if user_input == 'A':
    user_choice = celeb1
  elif user_input == 'B':
    user_choice = celeb2
  return user_choice
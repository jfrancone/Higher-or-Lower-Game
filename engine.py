from get_random_person import get_random_index, get_celeb
from art import vs
from compare_followers import compare_follows
from check_user_score import celeb_assignment, add_user_point, continue_game

def print_celeb_info(celeb):
  celeb_info = f"{celeb['name']}, a {celeb['description']}, from {celeb['country']}"
  return celeb_info
def engine():
  playing_game = True
  score = 0
  while playing_game == True:
    celeb1_index = get_random_index()
    celeb2_index = get_random_index()
    celeb1 = get_celeb(celeb1_index)
    celeb2 = get_celeb(celeb2_index)
    celeb1_info = print_celeb_info(celeb1)
    celeb2_info = print_celeb_info(celeb2)
    winner = compare_follows(celeb1, celeb2)
    print(f"Compare A: {celeb1_info}")
    print(vs)
    print(f"Against B: {celeb2_info}")
    user_input = input("Who has more followers? Type 'A' or 'B': ")
    user_choice = celeb_assignment(user_input, celeb1, celeb2)
    playing_game = continue_game(user_choice, winner, score, playing_game)
    add_user_point(user_choice, winner, score)
    print(f"The winner is {winner['name']}")
    
  
from art import logo


def continue_game(user_choice, winner, score):
    """
    Description: determines if the game will continue
    Parameters:
      user_choice: which celebrity user chose
      winner: which celebrity had the most followers in reality
      score: How many points the user has
    Return: A boolean: playing_game which is True if game should continue or False if game should not continue
    """
    playing_game = True
    if user_choice == winner:
        return playing_game
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        playing_game = False
        return playing_game


def add_user_point(user_choice, winner, score):
    """
    Description: Adds a point to the user's score
    Parameters:
      user_choice: which celebrity was chosen by the user
      winner: which celebrity truly had more followers
      score: the user's current score
    Return: The user's new score
    """
    if user_choice == winner:
        score += 1
        print(logo)
        print(f"You're right! Current score: {score}")
        return score
    else:
        print("Error: code should have exited")


def celeb_assignment(user_input, celeb1, celeb2):
    """
    Description: Assigns user input "a" or "b" to the celebrity chosen by the user
    Parameters:
      user_input: "a" or "b"; which celebrity the user chose
      celeb1: the identity of the first celebrity
      celeb2: the identity of the second celebrity
    Return: the user_choice (the celebrity the user chose)
    """
    if user_input == "a":
        user_choice = celeb1
    elif user_input == "b":
        user_choice = celeb2
    return user_choice

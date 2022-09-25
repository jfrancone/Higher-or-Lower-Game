def compare_follows(celeb1, celeb2):
    """
    Description: determines which celebrity has more instagram followers
    Parameters:
      celeb1: The first celebrity
      celeb2: The second celebrity
    Return: the celebrity that is the winner (has more followers)
    """
    winner = "No one"
    if celeb1["follower_count"] > celeb2["follower_count"]:
        winner = celeb1
        return winner
    elif celeb1["follower_count"] < celeb2["follower_count"]:
        winner = celeb2
        return winner
    else:
        winner = "Tie"
        return winner

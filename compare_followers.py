def compare_follows(celeb1 , celeb2):
  winner = "No one"
  if celeb1['follower_count'] > celeb2['follower_count']:
    winner = celeb1
    return winner
  elif celeb1['follower_count'] < celeb2['follower_count']:
    winner = celeb2
    return winner
  else:
    winner = 'Tie'
    return winner
  
    
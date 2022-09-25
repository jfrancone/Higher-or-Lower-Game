import random
from game_data import data

def get_random_index():
  index = random.randint(0, (len(data) - 1))
  return index
  
def get_celeb(index):
  celeb = data[index]
  return celeb


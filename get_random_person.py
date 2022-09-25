import random
from game_data import data


def get_random_index():
    """
    Description: gets a random index from list: Data
    Parameters:
      none
    Return: a random index within list: Data
    """
    index = random.randint(0, (len(data) - 1))
    return index


def get_celeb(index):
    """
    Description: gives the dictionary in the index given
    Parameters:
      index: the index of the dictionary (containing the celebrity information)
    Return: the dictionary at the given index
    """
    celeb = data[index]
    return celeb

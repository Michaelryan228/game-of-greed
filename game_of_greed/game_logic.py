import random
from collections import Counter

die_value = {1: 100, 5: 50}
three_set = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}

class GameLogic:

  def __init__(self):
    pass

  @staticmethod
  def calculate_score(tuple):
    counter = Counter(tuple)
    if len(counter) == 6:
      return 1500
    if len(Counter) == 3:
      if all(value == 2 for value in counter.values()):
        return 1500

    score = 0

    for num, counter in counter.items():
      if counter < 3:
        score += counter 


    thistuple = ("1", "2", "3", "4", "5", "6")
    print(thistuple)

  @staticmethod
  def roll_dice(roll_num):
    rolled = []
    for i in range(roll_num):
      rolled.append(random.randint(1,6))
    return tuple(rolled)

class Banker:
  
  def shelf():
    pass

  def bank():
    pass

  def clear_shelf():
    pass



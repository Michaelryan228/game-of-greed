import random
from collections import Counter

class GameLogic:

  @staticmethod
  def calculate_score():
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



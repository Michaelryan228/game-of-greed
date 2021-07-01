from random import randint
from collections import Counter



class GameLogic:

  def __init__(self):
    pass

  @staticmethod
  def calculate_score(roll):
    """
    input = tuple of dice we rolled.
    output = score based on the roll.
    """

    SINGLE_VALUE = {1: 100, 5: 50}
    THREE_OF_A_KIND = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}
    
    roll_counter = Counter(roll)
    if len(roll_counter) == 6:
      #this represents a straight
      return 1500
    if len(roll_counter) == 3:
      if all(value == 2 for value in roll_counter.values()):
        #this line represents 3 pairs
        return 1500

    score = 0

    for num, counter in roll_counter.items():
      if counter < 3:
        score += counter * SINGLE_VALUE.get(num, 0)
      elif counter == 3:
        score += THREE_OF_A_KIND[num]
      elif counter == 4:
        score += THREE_OF_A_KIND[num] * 2
      elif counter == 5:
        score += THREE_OF_A_KIND[num] * 3
      elif counter == 6:
        score += THREE_OF_A_KIND[num] * 4

    return score

  # def roll_dice(roll_num):
  #   rolled = []
  #   for i in range(roll_num):
  #     rolled.append(random.randint(1,6))
  #   return tuple(rolled)

  @staticmethod
  def to_str(dice_rolled):
    printed_results = ''
    for char in dice_rolled:
        printed_results += f'{char} '
    return(printed_results)

  def roll_dice(dnum = 6):
    return tuple([randint(1, 6) for _ in range(dnum)])

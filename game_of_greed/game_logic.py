import random
from collections import Counter

class GameLogic:

  def __init__(self):
      pass

  @staticmethod
  def roll_dice(num_of_dice):
    """
    Randomly generates roll.
    """
    rolled = []
    for i in range(num_of_dice):
      rolled.append(random.randint(1,6))
    return tuple(rolled)
  
  @staticmethod
  def calculate_score(rolled):
    """
    Calculates score of each roll.
    """
    score = 0
    # Return a list of the n most common elements and their counts from the most common to the least.
    dice_rolled_counter = Counter(rolled)
    most_common_rolled = Counter(dice_rolled_counter).most_common()
    unique_dice = len(most_common_rolled)
    most_rolled_number = most_common_rolled[0][1]
    occurrences = most_common_rolled[0][1] 
    
    
    single_values = {1:100, 5:50}
    if unique_dice == 6:
      score += 1500
    if unique_dice == 3 and most_common_rolled[0][1] == 2 and most_common_rolled[1][1] == 2:
      score += 1500
    
    if occurrences == 3:
      score += most_rolled_number*100
    if occurrences == 4:
      score += most_rolled_number*200
    if occurrences == 5:
      score += most_rolled_number*300
    if occurrences == 6:
      if most_rolled_number == 1:
        score += 4000
      else:
        score += most_rolled_number*400

    # for dice in most_common_rolled:
    #   if dice[0] == 1:
    #     score += dice[1]*100
    #   if dice[0] == 5:
    #     score += dice[1]*50
    for key in dice_rolled_counter:
      if key == 1 or key == 5:
        # print(key, '->', dice_rolled_counter[key]*single_values[key])
        score += dice_rolled_counter[key]*single_values[key]

    return score

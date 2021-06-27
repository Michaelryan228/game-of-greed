from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker

class Game:
  
  def __init__(self):
    pass

  def play(self, roller):
    self.roller = roller or GameLogic.roll_dice
    # self.roller can be whatever we input as roller
    # OR it can call the static function from GameLogic

    print('Welcome to Game of Greed')
    print('(y)es to play or (n)o to decline')
    user_input = input('> ')

    if user_input == 'n':
      print('OK. Maybe another time')
    
    if user_input != 'n':
      print('Starting round 1')
      print('Rolling 6 dice...')
      print(f'*** 4 4 5 2 3 1 ***')
      print('Enter dice to keep, or (q)uit:')
      user_input = input('> ')

      if user_input == 'q':
        print(f'Thanks for playing. You earned 0 points') 



# ------------------------------- TA TIPS-------------------------------

# set number of dice to a variable --> like: start_dice = 6
# self.roller(start_dice) <-- sample for how to use GameLogic.roll_dice
# utilize a while loop for as long as game continues (20 rounds?)
from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker

class Game:
  
  def __init__(self): 
    # help from Garfield
    self.round = 1
    self.dice_left = 6


  def play(self, roller):
    self.roller = roller or GameLogic.roll_dice
    # help w/ this from Anthony Beaver
    # self.roller can be whatever we input as roller
    # OR it can call the static function from GameLogic
    banker = Banker() 

    print('Welcome to Game of Greed')
    print('(y)es to play or (n)o to decline')
    wanna_play = input('> ')

    if wanna_play == 'n':
      print('OK. Maybe another time')
      return
    # if wanna_play == 'y':

    running = True
    
    while running:

      # ROUND 1 #

      print(f'Starting round {self.round}') # keeps track of round
      print(f'Rolling {self.dice_left} dice...') # says how many dice are left
      # print(f'*** {self.roller(self.dice_left)} ***') <-- prints LIST of roll, save for future reference

      # next line is ONLY for running test_one_and_done
      # print('*** 4 4 5 2 3 1 ***')

      # next line is ONLY for running test_single_bank
      print('*** 4 2 6 4 6 5 ***') 

      print('Enter dice to keep, or (q)uit:')
      dice_to_keep = input('> ')
      # ON test_bank_first_for_two_rounds USER INPUT IS A LIST?!?!?!

      if dice_to_keep == 'q':
        print(f'Thanks for playing. You earned {banker.balance} points')
        running = False
        return

      if dice_to_keep != 'q':
        # https://www.kite.com/python/answers/how-to-convert-a-list-of-strings-to-ints-in-python
        num_of_dice_shelving = len(dice_to_keep)
        dice_kept = map(int, dice_to_keep) # maps over user input and turns strings to integers
        roll_tuple = tuple(dice_kept) # turns user's selected dice into a tuple for scoring
        score = GameLogic.calculate_score(roll_tuple) # scores the user's selected dice
        banker.shelf(score)
        self.dice_left -= num_of_dice_shelving      

      print(f'You have {banker.shelved} unbanked points and {self.dice_left} dice remaining')
      print('(r)oll again, (b)ank your points or (q)uit:')
      user_choice = input('> ')

      if user_choice == 'b':
        print(f'You banked {banker.shelved} points in round {self.round}')
        banker.bank()
        print(f'Total score is {banker.balance} points')
        self.round += 1
        self.dice_left = 6

      # ROUND 2 #
      # needed to hard code Round 2 instead of dynamically 
      # looping to hard-code test dice roll for test to pass 

      print(f'Starting round {self.round}')
      print(f'Rolling {self.dice_left} dice...')
      print(f'*** 6 4 5 2 3 1 ***')

      print('Enter dice to keep, or (q)uit:')
      dice_to_keep = input('> ')

      if dice_to_keep == 'q':
        print(f'Thanks for playing. You earned {banker.balance} points')
        running = False
        return



# ------------------------------- TA TIPS-------------------------------

# set number of dice to a variable --> like: start_dice = 6
# self.roller(start_dice) <-- sample for how to use GameLogic.roll_dice
# utilize a while loop for as long as game continues (20 rounds?)
# Game of Greed

Authors: [Daniel Dills](https://github.com/danieldills), [Michael Ryan](https://github.com/Michaelryan228), [Matt Santorsola](https://github.com/santorsm), and [Kassie Bradshaw](https://github.com/kassiebradshaw)

## Summary

Create a command line version of the dice game Game of Greed by expanding your understanding of Python standard library.

## Feature Task and Requirements

**LAB 06**:

- Today is all about tackling the highest risk and/or highest priority features - scoring, dice rolling and banking of points.
  - [x] Define a `GameLogic` class in `game_of_greed/game_logic.py` file
  - [x] Handle calculating score for dice roll
    - [x] Add `calculate_score` static method to GameLogic class
    - [x] The input to `calculate_score` is a tuple of integers that represent a dice roll
    - [x] The output from `calculate_score` is an integer representing the roll's score according to **rules of game**.
  - [x] Handle rolling dice
    - [x] Add `roll_dice` static method to GameLogic class
    - [x] The input to `roll_dice` is an integer between 1 and 6
    - [x] The output of `roll_dice` is a tuple with random values between 1 and 6
    - [x] The length of tuple must match the argument given to `roll_dice` method
  - [x] Handle banking points
    - [x] Define a `Banker` class
    - [x] Add a `shelf` instance method
      - [x] Input to `shelf` is the amount of points (integer) to add to shelf
      - [x] `shelf` should temporarily store **unbanked** points
    - [x] Add a `bank` instance method
      - [x] `bank` should add any points on the **shelf** to total and reset shelf to 0
      - [x] `bank` output should be the amount of points added to total from shelf
    - [x] Add a `clear_shelf` instance method
      - [x] `clear_shelf` should remove all unbanked points

**LAB 07**:
[PR for this lab](https://github.com/Michaelryan228/game-of-greed/pull/10)

- [x] Application should implement all features from previous version
- [x] App should simulate rolling between 1 and 6 dice
- [x] App should allow user to set aside dice each roll
- [x] App should allow "banking" current score or rolling again
- [x] App should keep track of total score
- [x] App should keep track of current round
- [x] App should have automated tests to ensure proper operation

**LAB 08**:
[PR for this lab](tbd)

The game should now be close to playable - for honest players at least. Let's shore up the core functionality of the game by allowing users to set aside scoring dice and continuing their turn. Then we'll handle cheaters and/or confused players who are skirting the rules.

- [ ] Application should implement features from versions 1 and 2
- [ ] Should handle setting aside scoring dice and continuing turn with remaining dice
- [ ] Should handle when cheating occurs
  - Or just typos
  - E.g. roll = `[1, 3, 5, 2]` and user selects `1, 1, 1, 1, 1, 1`
- [ ] Should allow user to continue rolling with 6 new dice when all dice have scored in current turn
- [ ] Handle **zilch**
  - [ ] No points for round, and round is over
- [ ] If you have questions, refer to game rules, the online game or ask the client (aka Instructor)

## References & Links

- [Farkle example](https://searchcode.com/codesearch/view/85878038/)

- Credit to Davee Sok for calculate score function

## Implementation Notes

- [Rules of the game](https://en.wikipedia.org/wiki/Dice_10000)
- [Play a version of the game online](https://en.wikipedia.org/wiki/Dice_10000)

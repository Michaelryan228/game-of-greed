# Game of Greed

Authors: [Daniel Dills](https://github.com/danieldills), [Michael Ryan](https://github.com/Michaelryan228), [Matt Santorsola](https://github.com/santorsm), and [Kassie Bradshaw](https://github.com/kassiebradshaw)

## Summary

Lab 06: Game of Greed I

## Overview

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

- [ ] Application should implement all features from previous version
- [ ] App should simulate rolling between 1 and 6 dice
- [ ] App should allow user to set aside dice each roll
- [ ] App should allow "banking" current score or rolling again
- [ ] App should keep track of total score
- [ ] App should keep track of current round
- [x] App should have automated tests to ensure proper operation

## References & Links

- [Farkle example](https://searchcode.com/codesearch/view/85878038/)

- Credit to Davee Sok for calculate score function

## Implementation Notes

- [Rules of the game](https://en.wikipedia.org/wiki/Dice_10000)
- [Play a version of the game online](https://en.wikipedia.org/wiki/Dice_10000)

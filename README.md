# Hangman Game

A simple command-line Hangman game written in Python.

## Overview

The goal of the game is to guess the hidden word by suggesting letters one at a time.  
You have limited attempts before the game is over.

## How to Play

1. Run the `main.py` file in your Python environment.
2. Select a difficulty level: **easy**, **medium**, or **hard**.
3. Try to guess the word by entering one letter per turn.
4. Correct consecutive guesses increase your points multiplier.
5. Consecutive wrong guesses increase the penalty multiplier.
6. The game ends when you either guess the entire word or reach 6 incorrect guesses.

## Scoring System

- **Correct guesses:** Points increase with a multiplier that grows with consecutive correct letters.
- **Wrong guesses:** Points decrease, and the penalty gets harsher with each consecutive wrong guess.
- **Difficulty levels:** Affect the rewards and penalties through multipliers.

## Requirements

- Python 3.x
- A terminal or command prompt to run the game

## Running the Game

```bash
python main.py

By: Janix

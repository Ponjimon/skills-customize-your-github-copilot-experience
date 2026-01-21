
# 📘 Assignment: Games in Python — Hangman

## 🎯 Objective

Build a console-based Hangman game in Python that practices string manipulation, control flow, and user I/O. Students will implement game logic, track guesses and remaining attempts, and display clear win/lose states.

## 📝 Tasks

### 🛠️ Hangman Game

#### Description
Create a playable Hangman game that randomly selects a secret word from a predefined list and lets the player guess letters until they either reveal the word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from an internal list or provided word file.
- Accept single-letter guesses and update the displayed progress in the `_ _ _` format.
- Track and display incorrect guesses and remaining attempts.
- Prevent repeated penalty for the same guessed letter.
- End the game when the word is fully guessed or attempts are exhausted and show a clear win or lose message.
- Include a short usage section showing how to run the program (see `Starter Code`).

##### Example run

```
Word: _ a _ _ _
Guess a letter: n
Incorrect guesses left: 4
```

### 🛠️ Optional Enhancements (Extra Credit)

#### Description
Add one or more features to improve the game experience or code quality.

#### Requirements (pick any)

- Load the word list from an external `words.txt` file.
- Add difficulty levels that change number of attempts.
- Track and display a score or streak across multiple rounds.
- Add input validation and friendly prompts for replaying the game.

## Starter Files

- `starter-code.py` — a minimal starter with a main loop and example word list is included in this assignment folder.

## How to run

Run the starter script with Python 3:

```
python3 starter-code.py
```

---

Good luck — have fun building and extending Hangman!

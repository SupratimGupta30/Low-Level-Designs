# Tic-Tac-Toe

A simple Python implementation of the Tic-Tac-Toe game with a console-based play loop, board management, game rules, and notification support.

## Project Structure

- `main.py` - Entry point for running the game.
- `tictactoegame.py` - Main game logic, player rotation, move handling, win/draw detection, and notifier integration.
- `board.py` - Board representation, cell access, move validation, and display logic.
- `player.py` - Player model with name, symbol, and score tracking.
- `symbol.py` - Symbol wrapper used for board values (`X`, `O`, or `_`).
- `gameRules.py` - Abstract rule interface and standard Tic-Tac-Toe win/draw logic.
- `creategame.py` - Game factory for creating different game modes.
- `notification.py` - Observer-style notification interface and console notifier.

## Requirements

- Python 3.7+ recommended

## How to Run

1. Open a terminal in the `Tic-Tac-Toe` folder.
2. Run:

```bash
python main.py
```

3. Enter the board size when prompted (for example, `3` for a 3x3 board).
4. Follow the console prompts to enter row and column values for each move.

## Gameplay

- The game supports two players.
- Players take turns entering 0-indexed row and column values.
- The game checks for:
  - valid moves
  - win conditions across rows, columns, and diagonals
  - draw when the board is full and no player has won

## Notes

- The board is displayed after each move.
- Notifications are printed to the console.
- The current implementation assumes two players and a standard Tic-Tac-Toe game state.

## Example

```text
Enter the board size (e.g., 3 for a 3x3 board): 3
Notification: Game started! Players: Alice (X), Bob (O)
_ | _ | _
_ | _ | _
_ | _ | _
Alice's turn (X)
Enter row (0-indexed): 0
Enter column (0-indexed): 0
Notification: Alice placed X at (0, 0)
...
```

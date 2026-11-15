[Nederlands](./README.md) | **English**

# Tetris (BBC micro:bit)

A compact Tetris game for the BBC micro:bit 5×5 LED matrix, written in MakeCode Python ([`main.py`](./main.py)).

## How it works

- Randomly selected block shapes spawn at the top of the screen (`1×1`, `2×1`, `3×1`, `1×2`, and `2×2`).
- Whenever a horizontal row of 5 LEDs is completely filled, the row clears, upper blocks shift down, and you earn **1 point**.
- When a new piece can no longer fit at the top, `GAME OVER` is shown followed by your score.

## Controls

| Button | Action |
| :--- | :--- |
| **A** | Move 1 column left |
| **B** | Move 1 column right |
| **A + B** | Hard drop to the bottom |
| **A or B** *(on Game Over)* | Restart game |

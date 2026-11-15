[Nederlands](./README.md) | **English**

# Space Shooter (BBC micro:bit)

An arcade shooter for the BBC micro:bit 5×5 LED matrix, written in MakeCode Python ([`main.py`](./main.py)).

## How it works

- You control a ship along the bottom LED row and fire bullets straight upward.
- Debris spawns at the top and slowly falls down the screen.
- Every hit scores **1 point**.
- If any debris reaches the bottom row, `GAME OVER` is shown followed by your final score.

## Controls

| Button | Action |
| :--- | :--- |
| **A** | Move 1 step left |
| **B** | Move 1 step right |
| **A + B** | Fire bullet |
| **A or B** *(on Game Over)* | Restart game |

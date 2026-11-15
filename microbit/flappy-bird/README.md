# Flappy Bird (BBC micro:bit)

Een Flappy Bird-kloon voor het 5×5 LED-scherm van de BBC micro:bit, geschreven in MakeCode Python ([`main.py`](./main.py)).

## Hoe het werkt

- Zwaartekracht trekt het vogeltje langzaam naar beneden; door te fladderen stijg je 1 LED en zweef je heel even.
- Aankomende buizen schuiven van rechts naar links met steeds een opening van **2 LEDs** hoog.
- Elke gepasseerde buis levert **1 punt** op en het tempo neemt geleidelijk toe.
- Raak je een buis of val je op de grond, dan verschijnt `GAME OVER` gevolgd door je score.

## Besturing

| Knop | Actie |
| :--- | :--- |
| **A of B** | 1 vakje omhoog fladderen |
| **A of B** *(bij Game Over)* | Opnieuw starten |

---

<details>
<summary>English version</summary>

# Flappy Bird (BBC micro:bit)

A Flappy Bird clone for the BBC micro:bit 5×5 LED matrix, written in MakeCode Python ([`main.py`](./main.py)).

## How it works

- Gravity gradually pulls the bird downward; flapping moves you up 1 LED with a brief hover.
- Incoming pipes scroll from right to left, each with a **2-LED** vertical gap.
- Passing each pipe awards **1 point** and the speed slowly increases.
- Hitting a pipe or falling to the floor displays `GAME OVER` followed by your score.

## Controls

| Button | Action |
| :--- | :--- |
| **A or B** | Flap 1 row up |
| **A or B** *(on Game Over)* | Restart game |

</details>

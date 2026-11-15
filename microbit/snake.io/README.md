# Snake.io (BBC micro:bit)

Klassieke Snake-game voor het 5×5 LED-scherm van de BBC micro:bit, geschreven in MakeCode Python ([`main.py`](./main.py)).

## Hoe het werkt

- Je bestuurt een slang die begint met lengte 3 in het midden van het scherm.
- Eet het knipperende voedsel om langer te worden en **1 punt** te scoren; naarmate je score stijgt, beweegt de slang sneller.
- Raak je de rand of je eigen lichaam, dan verschijnt `GAME OVER` met je eindscore.
- Vul je alle 25 LEDs op het scherm, dan verschijnt `YOU WIN!`.

## Besturing

| Knop | Actie |
| :--- | :--- |
| **A** | 90° naar links draaien (vanuit de slang gezien) |
| **B** | 90° naar rechts draaien (vanuit de slang gezien) |
| **A of B** *(bij Game Over / Winst)* | Opnieuw starten |

---

<details>
<summary>English version</summary>

# Snake.io (BBC micro:bit)

Classic Snake game for the BBC micro:bit 5×5 LED matrix, written in MakeCode Python ([`main.py`](./main.py)).

## How it works

- You control a snake starting at length 3 in the center of the screen.
- Eat the blinking food to grow longer and score **1 point**; as your score increases, the snake moves faster.
- Hitting the screen border or your own body triggers `GAME OVER` followed by your final score.
- Filling all 25 LEDs on the grid displays `YOU WIN!`.

## Controls

| Button | Action |
| :--- | :--- |
| **A** | Turn 90° left (relative to heading) |
| **B** | Turn 90° right (relative to heading) |
| **A or B** *(on Game Over / Win)* | Restart game |

</details>

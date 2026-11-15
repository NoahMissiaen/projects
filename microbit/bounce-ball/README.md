# Bounce Ball (BBC micro:bit)

Een Breakout-/steenbreker-game voor het 5×5 LED-scherm van de BBC micro:bit, geschreven in MakeCode Python ([`main.py`](./main.py)).

## Hoe het werkt

- Bovenaan staan 2 rijen blokken (10 stenen); onderaan bestuur je een plankje van 2 LEDs breed.
- De bal start op de plank en schuift met je mee totdat je hem afschiet.
- Elke weggekaatste steen levert **1 punt** op. Door de bal op de linker- of rechterhelft van het plankje op te vangen, stuur je hem respectievelijk naar links- of rechtsboven.
- Zijn alle 10 stenen weg, dan verschijnt `CLEAR!`, start het volgende level met nieuwe blokken en gaat de bal sneller.
- Mis je de bal onderaan, dan verschijnt `GAME OVER` gevolgd door je score.

## Besturing

| Knop | Actie |
| :--- | :--- |
| **A** | Plank naar links |
| **B** | Plank naar rechts |
| **A + B** | Bal afschieten vanaf de plank |
| **A of B** *(bij Game Over)* | Opnieuw starten |

---

<details>
<summary>English version</summary>

# Bounce Ball (BBC micro:bit)

A Breakout-style brick breaker game for the BBC micro:bit 5×5 LED matrix, written in MakeCode Python ([`main.py`](./main.py)).

## How it works

- Two rows of bricks (10 in total) sit at the top; at the bottom you control a 2-LED paddle.
- The ball starts perched on the paddle and moves along with it until you launch it.
- Each broken brick awards **1 point**. Catching the ball on the left or right side of the paddle bounces it up-left or up-right.
- Clearing all 10 bricks displays `CLEAR!`, spawns a new wall, and speeds up the ball.
- Missing the ball triggers `GAME OVER` followed by your score.

## Controls

| Button | Action |
| :--- | :--- |
| **A** | Move paddle left |
| **B** | Move paddle right |
| **A + B** | Launch ball from paddle |
| **A or B** *(on Game Over)* | Restart game |

</details>

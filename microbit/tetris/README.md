# Tetris (BBC micro:bit)

Een compacte Tetris-game voor het 5×5 LED-scherm van de BBC micro:bit, geschreven in MakeCode Python ([`main.py`](./main.py)).

## Hoe het werkt

- Er verschijnen willekeurig gekozen blokvormen bovenaan het scherm (`1×1`, `2×1`, `3×1`, `1×2` en `2×2`).
- Zodra een horizontale rij van 5 LEDs volledig gevuld is, verdwijnt de rij, schuiven bovenliggende blokken omlaag en krijg je **1 punt**.
- Als een nieuw blokje bovenaan niet meer geplaatst kan worden, verschijnt `GAME OVER` gevolgd door je score.

## Besturing

| Knop | Actie |
| :--- | :--- |
| **A** | 1 kolom naar links |
| **B** | 1 kolom naar rechts |
| **A + B** | Blok direct naar beneden laten vallen (hard drop) |
| **A of B** *(bij Game Over)* | Opnieuw starten |

---

<details>
<summary>English version</summary>

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

</details>

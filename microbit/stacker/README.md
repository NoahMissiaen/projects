# Stacker (BBC micro:bit)

Een snelle arcade-torenstapelaar voor het 5×5 LED-scherm van de BBC micro:bit, geschreven in MakeCode Python ([`main.py`](./main.py)).

## Hoe het werkt

- Je begint onderaan met een snel bewegend blok van 3 LEDs breed dat gedeeltelijk buiten het scherm kan schuiven.
- Druk op een knop om het blok stil te zetten. Alleen de LEDs die op het scherm staan en precies boven het vorige blok liggen blijven behouden — elk overhangend deel valt weg.
- Elke geplaatste rij levert **1 punt** op. Haal je de bovenste rij (`rij 0`), dan verschijnt `CLEAR!` en start een sneller level.
- Mis je de toren volledig, dan verschijnt `GAME OVER` gevolgd door je score.

## Besturing

| Knop | Actie |
| :--- | :--- |
| **A of B** | Bewegend blok vastzetten |
| **A of B** *(bij Game Over)* | Opnieuw starten |

---

<details>
<summary>English version</summary>

# Stacker (BBC micro:bit)

A fast-paced arcade tower stacker for the BBC micro:bit 5×5 LED matrix, written in MakeCode Python ([`main.py`](./main.py)).

## How it works

- You start at the bottom with a fast-moving 3-LED bar that slides partially off-screen at both edges.
- Press a button to lock the bar in place. Only LEDs on screen that align directly above the previous row remain — any overhang is cut off.
- Each stacked row awards **1 point**. Reaching the top row (`row 0`) triggers `CLEAR!` and starts a faster level.
- Missing the tower completely shows `GAME OVER` followed by your score.

## Controls

| Button | Action |
| :--- | :--- |
| **A or B** | Lock moving bar |
| **A or B** *(on Game Over)* | Restart game |

</details>

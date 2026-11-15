# Simon Says (BBC micro:bit)

Een geheugenspel voor het 5×5 LED-scherm van de BBC micro:bit, geschreven in MakeCode Python ([`main.py`](./main.py)).

## Hoe het werkt

- De micro:bit toont elke ronde een steeds langere reeks symbolen: een pijl naar links, een pijl naar rechts of een diamant in het midden.
- Herhaal de volledige reeks in dezelfde volgorde om **1 punt** te verdienen en naar de volgende ronde te gaan (het tempo neemt geleidelijk toe).
- Bij een fout verschijnt een kruisje gevolgd door `GAME OVER` en je score.

## Besturing

| Symbool / Situatie | Knop |
| :--- | :--- |
| Pijl naar links | **A** |
| Pijl naar rechts | **B** |
| Diamant | **A + B** |
| Opnieuw starten *(bij Game Over)* | **A of B** |

---

<details>
<summary>English version</summary>

# Simon Says (BBC micro:bit)

A memory pattern game for the BBC micro:bit 5×5 LED matrix, written in MakeCode Python ([`main.py`](./main.py)).

## How it works

- Each round, the micro:bit displays a growing sequence of symbols: a left arrow, a right arrow, or a center diamond.
- Repeat the sequence in the exact same order to earn **1 point** and advance to the next round (display speed gradually increases).
- Making a mistake shows a cross icon followed by `GAME OVER` and your score.

## Controls

| Symbol / State | Button |
| :--- | :--- |
| Left arrow | **A** |
| Right arrow | **B** |
| Diamond | **A + B** |
| Restart game *(on Game Over)* | **A or B** |

</details>

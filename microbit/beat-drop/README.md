# Beat Drop (BBC micro:bit)

Een 3-baans ritmespel met achtergrondmuziek en geluidseffecten voor het 5×5 LED-scherm van de BBC micro:bit, geschreven in MakeCode Python ([`main.py`](./main.py)).

## Hoe het werkt

- Van bovenaf vallen noten op de maat van de melodie omlaag over 3 banen (kolom `0`, `2` en `4`), onderaan afgebakend door twee vaste markerings-LEDs (`x = 1` en `x = 3`).
- Druk op de bijbehorende knop zodra een noot de onderste twee rijen (`y = 3` of `4`) bereikt om **1 punt** te scoren en een akkoordtoon te laten klinken.
- Je hebt **3 levens**: mis je een noot of druk je verkeerd, dan klinkt een lage bromtoon en verlies je 1 leven.
- Hoe hoger je score, hoe sneller de noten vallen. Bij 0 levens klinkt een Game Over-deuntje en verschijnt je eindscore.

## Besturing

| Baan / Situatie | Knop |
| :--- | :--- |
| Linkerbaan (`x = 0`) | **A** |
| Middelste baan (`x = 2`) | **A + B** |
| Rechterbaan (`x = 4`) | **B** |
| Opnieuw starten *(bij Game Over)* | **A of B** |

---

<details>
<summary>English version</summary>

# Beat Drop (BBC micro:bit)

A 3-lane rhythm game with background music and sound effects for the BBC micro:bit 5×5 LED matrix, written in MakeCode Python ([`main.py`](./main.py)).

## How it works

- Notes fall in sync with a background melody down 3 lanes (columns `0`, `2`, and `4`), marked at the bottom by two fixed divider LEDs (`x = 1` and `x = 3`).
- Press the matching button when a note reaches the bottom two rows (`y = 3` or `4`) to score **1 point** and trigger a lane tone.
- You have **3 lives**: missing a note or pressing an empty lane plays a low buzz and costs 1 life.
- Notes fall faster as your score increases. At 0 lives, a Game Over tune plays followed by your final score.

## Controls

| Lane / State | Button |
| :--- | :--- |
| Left lane (`x = 0`) | **A** |
| Center lane (`x = 2`) | **A + B** |
| Right lane (`x = 4`) | **B** |
| Restart game *(on Game Over)* | **A or B** |

</details>

# Dino Game (BBC micro:bit)

Een offline Dino-runner voor het 5×5 LED-scherm van de BBC micro:bit, geschreven in MakeCode Python ([`main.py`](./main.py)).

## Hoe het werkt

- De dino staat helemaal links op de onderste rij en springt over aankomende cactussen.
- Cactussen verschijnen met willekeurige tussenpozen aan de rechterkant en schuiven naar links; naarmate je score stijgt gaat het spel sneller.
- Elke ontweken cactus levert **1 punt** op.
- Raak je een cactus, dan verschijnt `GAME OVER` gevolgd door je score.

## Besturing

| Knop | Actie |
| :--- | :--- |
| **A** | Normale sprong (2 blokjes hoog) |
| **A + B** | Hoge sprong (3 blokjes hoog) |
| **A of B** *(bij Game Over)* | Opnieuw starten |

---

<details>
<summary>English version</summary>

# Dino Game (BBC micro:bit)

An offline Dino runner game for the BBC micro:bit 5×5 LED matrix, written in MakeCode Python ([`main.py`](./main.py)).

## How it works

- The dino stands on the far left of the bottom row and jumps over incoming cacti.
- Cacti spawn at random intervals on the right and move left; the game gradually speeds up as your score increases.
- Each cleared cactus awards **1 point**.
- Hitting a cactus shows `GAME OVER` followed by your score.

## Controls

| Button | Action |
| :--- | :--- |
| **A** | Normal jump (2 blocks high) |
| **A + B** | High jump (3 blocks high) |
| **A or B** *(on Game Over)* | Restart game |

</details>

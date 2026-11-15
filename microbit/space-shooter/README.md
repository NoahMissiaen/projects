**Nederlands** | [English](./README.en.md)

# Space Shooter (BBC micro:bit)

Een arcade shooter voor het 5×5 LED-scherm van de BBC micro:bit, geschreven in MakeCode Python ([`main.py`](./main.py)).

## Hoe het werkt

- Je bestuurt een schip op de onderste LED-rij en schiet kogels recht omhoog.
- Bovenaan verschijnen brokstukken die langzaam naar beneden vallen.
- Elke voltreffer levert **1 punt** op.
- Zodra een brokstuk de onderste rij bereikt, verschijnt `GAME OVER` gevolgd door je eindscore.

## Besturing

| Knop | Actie |
| :--- | :--- |
| **A** | 1 stap naar links |
| **B** | 1 stap naar rechts |
| **A + B** | Kogel afvuren |
| **A of B** *(bij Game Over)* | Opnieuw starten |

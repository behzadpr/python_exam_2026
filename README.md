# Examination

Individuell examinationsuppgift i kursen Programmering med Python.

Börja läs igenom game.py - det är där projektet startas.

## Starta projektet

```commandline
python -m src.game
```

Tips! Du kan spara denna rad som en "run configuration" i PyCharm.
1. Välj "Edit configurations..."
2. Ändra i sektionen "run" så det står `module` i stället för `script`
3. Skriv `src.game` i rutan till höger om `module`

## Implementerade krav

### Version 1 – grundkrav

- **A. Startposition** – Spelaren börjar nära mitten av rummet.
- **B. Förflyttning** – Man kan röra sig i alla 4 riktningar med tangenterna W, A, S och D.
- **C. Väggar** – Man kan inte gå igenom väggar.
- **D. Fruktsallad** – Alla frukter är värda 20 poäng i stället för 10.
- **E. Inventory** – Alla saker man plockar upp sparas i en lista.
- **F. Inventory-kommando** – Kommandot "i" skriver ut innehållet i spelarens inventory.
- **G. The floor is lava** – För varje steg man går tappar man 1 poäng.
- **H. Sammanhängande väggar** – For-loopar används för att skapa flera sammanhängande väggar på kartan. Det skapas inga rum som man inte kan komma in i. Logiken finns i `grid.py`.

### Version 2 – nice to have

- **I. Fällor** – Fällor finns på spelplanen. Om man går på en fälla förlorar man 10 poäng. Fällan ligger kvar så att man kan falla i den flera gånger.
- **J. Spade** – En spade kan plockas upp. När man sedan går in i en vägg förbrukas spaden och väggen tas bort.
- **K. Nycklar och kistor** – Nycklar och lika många kistor slumpas på spelplanen. Man plockar upp en nyckel i sitt inventory. Vid en kista förbrukas en nyckel och man får en skatt värd 100 poäng.
- **L. Bördig jord** – Efter varje 25:e drag skapas en ny frukt/grönsak någonstans på kartan.
- **M. Exit** – Ett "E" slumpas på kartan när alla ursprungliga saker har plockats upp. Då kan man gå till exit för att vinna spelet. Innan dess har Exit ingen effekt.

## Symboler på kartan

| Symbol | Betydelse | Poäng |
|--------|-----------|-------|
| `@` | Spelaren | – |
| `.` | Tom ruta (golv) | -1 per steg |
| `■` | Vägg | – |
| `?` | Frukt eller vanligt föremål | +20 (frukt) / +10 (föremål) |
| `*` | Fälla | -10 |
| `#` | Spade | 0 |
| `p` | Nyckel | 0 |
| `O` | Kista | +100 |
| `E` | Exit | 0 |

## Tester

Några tesfall har lagts till i mappen `test/` för att verifiera funktionaliteten:


| Testfil | Vad den testar |
|---|---|
| `test_traps.py` | Fällor: poängavdrag, fällan ligger kvar, multipla träffar |
| `test_shovel.py` | Spade: blockeras utan spade, spade förbrukas, vägg bryts |

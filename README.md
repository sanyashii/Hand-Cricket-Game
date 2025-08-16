# Hand-Cricket-Game
A fun text-based Hand Cricket game in Python.

---

---

## 🚀 Features

* Toss system (Odd/Even toss).
* Bat or Bowl decision.
* Play with **1 to 10 batters**.
* Interactive CLI gameplay.
* Keeps track of runs, wickets, and results.
* Random PC moves for fair gameplay.

---

## 🎮 How to Play

1. Run the script:

   ```bash
   python hand_cricket.py
   ```
2. Toss:

   * Choose **Odd (O)** or **Even (E)**.
   * Pick a number between 0–6.
   * Toss result decides who bats first.
3. Match:

   * Enter a number between 0–6 each turn.
   * If your number = PC’s number → Batter is OUT ❌.
   * Else, runs are added 🏃.
4. Play until all batters are out.
5. Highest score wins!

---

## 📦 Requirements

* Python 3.x
* No external libraries required (only uses `random`).

---

## 📝 Example Gameplay

```
🏏 Welcome to Hand Cricket!

🪙 Toss Time!
Choose Odd (O) or Even (E): o
Enter a number between 0 and 6 for toss: 3
You chose: 3, PC chose: 4
Total: 7 → Odd
✅ You won the toss!
Do you want to Bat or Bowl first? (bat/bowl): bat
```

---

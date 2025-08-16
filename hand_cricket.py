import random

def OE():
    print()
    print('''🏏 Welcome to Hand Cricket!
    
Instructions:
- Toss: Choose Odd or Even, and a number between 0 and 6. 
- Match: Choose a number between 0 and 6.
- If your number matches PC's number, the batter is OUT!
- Otherwise, the batter scores runs equal to their number.
Let's begin!
''')

    # ---------------- Toss ----------------
    print("🪙 Toss Time!")
    while True:
        toss_choice = input("Choose Odd (O) or Even (E): ").strip().lower()
        if toss_choice in ['o', 'e']:
            break
        else:
            print("Invalid choice. Enter 'O' or 'E'.")

    while True:
        try:
            user_toss_number = int(input("Enter a number between 0 and 6 for toss: ").strip())
            if 0 <= user_toss_number <= 6:
                break
            else:
                print("Number must be between 0 and 6.")
        except ValueError:
            print("Please enter a valid number.")

    pc_toss_number = random.randint(0, 6)
    toss_sum = user_toss_number + pc_toss_number
    result = 'even' if toss_sum % 2 == 0 else 'odd'

    print(f"\nYou chose: {user_toss_number}, PC chose: {pc_toss_number}")
    print(f"Total: {toss_sum} → {'Even' if result == 'even' else 'Odd'}")

    user_bats_first = None

    if (toss_choice == 'e' and result == 'even') or (toss_choice == 'o' and result == 'odd'):
        print("✅ You won the toss!")
        while True:
            decision = input("Do you want to Bat or Bowl first? (bat/bowl): ").strip().lower()
            if decision in ['bat', 'bowl']:
                user_bats_first = decision == 'bat'
                break
            else:
                print("Enter 'bat' or 'bowl'.")
    else:
        print("❌ PC won the toss!")
        user_bats_first = random.choice([True, False])
        print(f"PC chooses to {'Bat' if user_bats_first == False else 'Bowl'} first.")

    # ---------------- Match Setup ----------------
    while True:
        try:
            n = int(input("\nEnter number of batters (1-10): ").strip())
            if 1 <= n <= 10:
                break
            else:
                print("Choose between 1 and 10.")
        except ValueError:
            print("Enter a valid number.")

    def play_innings(is_user_batting):
        i = 1
        total = []
        side = "Your" if is_user_batting else "PC's"
        print(f"\n🎮 {side} innings begins!\n")
        while i <= n:
            runs = []
            def play():
                C = random.randint(0, 6)
                try:
                    H = int(input("Enter number (0-6): ").strip())
                except ValueError:
                    print("Invalid input.")
                    return play()
                if H not in range(0, 7):
                    print("Enter a number between 0 and 6.")
                    return play()
                print(f"You chose: {H}, PC chose: {C}")
                if H == C:
                    print(f"❌ Batter {i} is OUT! Scored: {sum(runs)}\n")
                    total.append(sum(runs))
                    return
                else:
                    runs.append(H if is_user_batting else C)
                    print(f"{'You' if is_user_batting else 'PC'} scored: {runs[-1]}")
                    print(f"Total for Batter {i}: {sum(runs)}\n")
                    return play()
            play()
            i += 1
        return sum(total)

    # ---------------- Play Both Innings ----------------
    if user_bats_first:
        user_score = play_innings(is_user_batting=True)
        print(f"🧑 Your innings total: {user_score}\n")
        pc_score = play_innings(is_user_batting=False)
        print(f"🤖 PC innings total: {pc_score}\n")
    else:
        pc_score = play_innings(is_user_batting=False)
        print(f"🤖 PC innings total: {pc_score}\n")
        user_score = play_innings(is_user_batting=True)
        print(f"🧑 Your innings total: {user_score}\n")

    # ---------------- Match Result ----------------
    print("🏁 Match Result:")
    print(f"Your Score: {user_score}")
    print(f"PC Score:   {pc_score}\n")

    if user_score > pc_score:
        print("🏆 You won the match!")
    elif user_score < pc_score:
        print("💔 You lost the match!")
    else:
        print("🤝 It's a Tie!")

OE()

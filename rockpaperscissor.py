import random

def play_game():
    options = ["rock", "paper", "scissor"]
    user_points = 10
    comp_points = 10
    round_num = 1

    print("🎮 Rock Paper Scissors Game")
    print("🏁 First to reach 20 points wins!")
    print("-----------------------------")

    while user_points < 20 and comp_points < 20:
        print(f"\n🔢 Round {round_num}")
        print(f"🧑 Your Points: {user_points} | 🤖 Computer Points: {comp_points}")
        user_choice = input("Choose rock, paper, or scissor: ").lower()

        if user_choice not in options:
            print("❌ Invalid input! Please choose from rock, paper, or scissor.")
            continue

        comp_choice = random.choice(options)
        print(f"🤖 Computer chose: {comp_choice}")

        if user_choice == comp_choice:
            user_points += 1
            comp_points += 1
            print("🤝 It's a tie! Both get 1 point.")
        elif (
            (user_choice == "rock" and comp_choice == "scissor") or
            (user_choice == "paper" and comp_choice == "rock") or
            (user_choice == "scissor" and comp_choice == "paper")
        ):
            user_points += 2
            print("🎉 You win this round! +2 points")
        else:
            comp_points += 2
            print("😢 You lost this round. Computer gets 2 points")

        round_num += 1

    print("\n🏁 Final Score:")
    print(f"🧑 You: {user_points} | 🤖 Computer: {comp_points}")

    if user_points >= 20 and comp_points >= 20:
        print("🤝 It's a draw!")
    elif user_points >= 20:
        print("🏆 Congratulations! You won the game!")
    else:
        print("💀 Computer won the game. Better luck next time!")

play_game()

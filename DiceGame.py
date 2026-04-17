import random
player_score = 0
computer_score = 0
rounds = 5

for i in range(rounds):
    input("\nPress Enter to roll dice...")
    player = random.randint(1, 6)
    computer = random.randint(1, 6)
    print("You rolled:", player)
    print("Computer rolled:", computer)

    if player > computer:
        player_score += 1
        print("You win this round!")
    elif computer > player:
        computer_score += 1
        print("Computer wins this round!")
    else:
        print("Draw!")

print("\nFinal Score:")
print("You:", player_score)
print("Computer:", computer_score)

if player_score > computer_score:
    print("You are the winner!")
else:
    print("Computer wins!")
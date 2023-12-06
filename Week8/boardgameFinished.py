#Maahir Vohra
#10/4/21
#Not so simple program that creates a board game. (Googled a lot of things that I used that we havent learned in class.)
player_position = 0
number_of_moves = 0

mystery_move_blocks = [3, 7, 11, 13]

print("Let's play a board game! \nSee how many moves it takes to reach the end.\n \nStart")
print("-" * 30)

for i in range(1, 16):

    if i in mystery_move_blocks:
        print(f"Block {i} Mystery Move")

    else:
        print(f"Block {i}")

print("-" * 30 + "\nFinish\n")

while True:

    roll = random.randint(1, 6)
    print(f"You rolled a {roll}.")

    if player_position in mystery_move_blocks:
        print("You landed on a mystery block!")
        mystery_move = random.randint(1, 4)

        if mystery_move == 1:
            print("Go ahead two blocks.")
            player_position += 2

        elif mystery_move == 2:
            print("Go back three blocks.")
            player_position -= 3

        elif mystery_move == 3:
            print("Go back to Start.")
            player_position = 0

        elif mystery_move == 4:
            print("Surprise win!")
            player_position = 16

    else:
        player_position += roll

    number_of_moves += 1
    print(f"You are currently on Block {player_position}.")

    if player_position >= 15:
        print(f"\nCongratulations! You finished the game in {number_of_moves} moves.")
        replay_game = input("Would you like to play again? (Y/N) ").strip().upper()

        if replay_game == "Y":
            player_position = 0
            number_of_moves = 0
            continue

        else:
            print("Thank you for playing!")
            break

    else:
        continue

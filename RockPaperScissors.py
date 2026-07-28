import random

choices = ["rock", "paper", "scissors"]

games_played = 0
player_win = 0
computer_win = 0
ties = 0

print("Rock crushes scissors. Scissors cut paper. Paper covers rock.")

player = input("Do you want to be rock, paper or scissors (or quit)? ")

while player != "quit":
    player = player.lower()

    computer = random.choice(choices)
    print("You chose " + player + ", and the computer chose " + computer + ".")

    if player == computer:
        print("It's a tie!")
        ties +=1

    elif player == "rock":
        if computer == "scissors":
            print("You Win!")
            player_win += 1
        else:
            print("Computer Wins!")
            computer_win += 1

    elif player == "paper":
        if computer == "rock":
            print("You Win!")
            player_win += 1
        else:
            print("Computer Wins!")
            computer_win += 1

    elif player == "scissors":
        if computer == "paper":
            print("You Win!")
            player_win += 1
        else:
            print("Computer Wins!")
            computer_win += 1

    else:
        print("I think there was some sort of error...")
        player = input("Do you want to be rock, paper or scissors (or quit)? ")
        continue

    
    games_played += 1

    player = input("Do you want to be rock, paper or scissors (or quit)? ")
print("\n+----------------------+")
print("|      SCOREBOARD      |")
print("+----------------------+")
print(f"| Games:      {games_played:<8} |")
print(f"| Ties:       {ties:<8} |")
print(f"| You:        {player_win:<8} |")
print(f"| Computer:   {computer_win:<8} |")
print("+----------------------+\n")

print("Thanks for playing!")

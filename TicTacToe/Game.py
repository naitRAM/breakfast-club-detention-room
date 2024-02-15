from Grid import Grid
from random import seed, random
play = True
player_score = 0
computer_score = 0
ties = 0

while play:
    print("Welcome to Tic Tac Toe, you will be playing against the computer")
    player_mark = input("Enter your preferred mark (X or O): ")
    while player_mark != "X" and player_mark != "O":
        player_mark = input("Enter a valid mark (X or O): ")
    print()
    grid = Grid()
    if player_mark == "X":
        computer = "O"
    else:
        computer = "X"
    print("selecting first to play...")
    seed()
    ran = random()
    if ran <= 0.5:
        turn = "computer"
        print("computer plays first")
    else:
        turn = "player"
        print("you play first")
    print()
    grid.print_grid()
    print()
    player_wins = False
    computer_wins = False
    while not player_wins and not computer_wins and not grid.count_empties() == 0:
        if turn == "player":
            cell = input("Enter a valid cell to play (e.g. a1, b3, c2): ")
            while cell not in grid.cell_names or not grid.cells[grid.cell_names.index(cell)].is_empty():
                cell = input("Enter a valid empty cell: ")
            cell_index = grid.cell_names.index(cell)
            cell = grid.cells[cell_index]
            grid.play_cell(cell, player_mark)
            print()
            grid.print_grid()
            print()
            turn = "computer"
        elif turn == "computer":
            grid.play(computer)
            print()
            grid.print_grid()
            print()
            turn = "player"
        player_wins = grid.is_win(player_mark)
        computer_wins = grid.is_win(computer)
    print()
    if player_wins:
        print("You won!")
        player_score += 1
    elif computer_wins:
        print("Sorry, computer wins!")
        computer_score +=1
    else:
        print ("You tied!")
        ties += 1
    print("Player: " + str(player_score), "Computer: " + str(computer_score), "Ties: " + str(ties), sep="\n")
    player_response = input("Play again? (Y/N)").lower()
    while player_response != "y" and player_response != "n":
        player_response = input("Play again? Enter a valid response (Y/N or y/n)")
    if player_response == 'n':
        play = False
        if computer_score > player_score:
            print("Have a nice day, loser!")
        elif player_score > computer_score:
            print("Next time you'll lose")
        else:
            print("Way to pussy out while we're tying!")
    else:
        if computer_score > player_score:
            print("Not tired of losing yet?")
        elif player_score > computer_score:
            print("Don't think you'll keep winning!")
        else:
            print("Time to break you!")
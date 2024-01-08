from TTTGrid import TTTGrid
from random import seed, random

play = True
while play:
    print("Welcome to Tic Tac Toe, you will be playing against the computer")
    player_mark = input("Enter your preferred mark (X or O): ")
    while player_mark != "X" and player_mark != "O":
        player_mark = input("Enter a valid mark (X or O): ")
    print()
    grid = TTTGrid()
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
    while not grid.is_win(player_mark) and not grid.is_win(computer) and not grid.count_empty() == 0:
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
    play = False


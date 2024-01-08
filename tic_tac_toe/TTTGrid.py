from TTTCell import TTTCell
from random import seed
from random import random
from random import choice

class TTTGrid:
    """ A class that creates a new TicTacToe grid object """

    def __init__(self):
        self.a1 = TTTCell()
        self.a2 = TTTCell()
        self.a3 = TTTCell()
        self.b1 = TTTCell()
        self.b2 = TTTCell()
        self.b3 = TTTCell()
        self.c1 = TTTCell()
        self.c2 = TTTCell()
        self.c3 = TTTCell()
        self.cells = [self.a1, self.a2, self.a3, self.b1, self.b2, self.b3, self.c1, self.c2, self.c3]
        self.cell_names = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
        self.corners = [self.a1, self.a3, self.c1, self.c3]
        self.edges = [self.a2, self.b1, self.b3, self.c2]
        self.row1 = [self.a1, self.b1, self.c1]
        self.row2 = [self.a2, self.b2, self.c2]
        self.row3 = [self.a3, self.b3, self.c3]
        self.col1 = [self.a1, self.a2, self.a3]
        self.col2 = [self.b1, self.b2, self.b3]
        self.col3 = [self.c1, self.c2, self.c3]
        self.diag1 = [self.a1, self.b2, self.c3]
        self.diag2 = [self.a3, self.b2, self.c1]
        self.categs = [self.row1, self.row2, self.row3, self.col1, self.col2, self.col3, self.diag1, self.diag2]
    
    def print_grid(self):
        rows = [self.row1, self.row2, self.row3]
        col_headings = ["a", "b", "c"]
        print("  ", end="")
        for i in range(len(col_headings)):
            print(col_headings[i], end=" ")
        print()
        for i in range(len(rows)):
            print(i+1, end=" ")
            for j in range(len(rows[i])):
                value = rows[i][j].get_value()
                if not value:
                    value = "-"
                print(value, end=" ")
            print()

    def is_win(self, mark):
        for categ in self.categs:
            count = 0
            for cell in categ:
                if cell.get_value() == mark:
                    count += 1
            if count == 3:
                return True
        return False
    
    def play_cell(self, cell, mark):
        cell.set_value(mark)

    def count_empty(self):
        count = 0
        for cell in self.cells:
            if cell.is_empty():
                count += 1
        return count

    def corner_played(self):
        played = False
        for cell in self.corners:
            if not cell.is_empty():
                played = True
        return played

    def shared_empties(self, criterion1, criterion2):
        empties = []
        criterion1_list = []
        criterion2_list = []
        for category in criterion1:
            for cell in category:
                if cell not in criterion1_list and cell.is_empty():
                    criterion1_list.append(cell)
        for category in criterion2:
            for cell in category:
                if cell not in criterion2_list and cell.is_empty():
                    criterion2_list.append(cell)
        for cell in criterion1_list:
            if cell in criterion2_list:
                    empties.append(cell)
        return empties
        
   
    def play(self, mark):
        critical = []
        defendable = []
        clear = []
        playable = []
        winnable = []
        misc = []
        for categ in self.categs:
            enemy_count = 0
            self_count = 0
            empty_count = 0
            for cell in categ:
                if not cell.is_empty():
                    if cell.get_value() == mark:
                        self_count += 1
                    else:
                        enemy_count += 1
                else:
                    empty_count += 1
            if enemy_count == 2 and self_count == 0:
                critical.append(categ)
            elif enemy_count == 1 and self_count == 0:
                defendable.append(categ)
            elif enemy_count == 0 and self_count == 0:
                clear.append(categ)
            elif enemy_count == 0 and self_count == 1:
                playable.append(categ)
            elif enemy_count == 0 and self_count == 2:
                winnable.append(categ)
            elif empty_count == 1:
                misc.append(categ)

        if self.count_empty() == 9:
            seed()
            ran = random();
            if 0 <= ran < 0.45:
                self.b2.set_value(mark)
            elif 0.45 <= ran < 0.80:
                seed()
                ran_corner = choice(self.corners)
                ran_corner.set_value(mark)
            elif 0.80 <= ran < 1:
                seed()
                ran_edge = choice(self.edges)
                ran_edge.set_value(mark)

        elif self.count_empty() == 8:
            if not self.b2.is_empty():
                seed()
                ran_corner = choice(self.corners)
                ran_corner.set_value(mark)
            else:
                self.b2.set_value(mark)
        else:
            if winnable:
                for cell in winnable[0]:
                    if cell.is_empty():
                        cell.set_value(mark)
            elif critical:
                for cell in critical[0]:
                    if cell.is_empty():
                        cell.set_value(mark)
            elif defendable and playable and self.shared_empties(defendable, playable):
                shared = self.shared_empties(defendable, playable)
                seed()
                ran_cell = choice(shared)
                ran_cell.set_value(mark)
            elif playable:
                seed()
                ran_choice = choice(playable)
                playable_cells = []
                for cell in ran_choice:
                    if cell.is_empty():
                        playable_cells.append(cell)
                seed()
                ran_cell = choice(playable_cells)
                ran_cell.set_value(mark)
            elif defendable:
                seed()
                ran_choice = choice(defendable)
                defendable_cells = []
                for cell in ran_choice:
                    if cell.is_empty():
                        defendable_cells.append(cell)
                seed()
                ran_cell = choice(defendable_cells)
                ran_cell.set_value(mark)
            elif clear:
                seed()
                ran_choice = choice(clear)
                seed()
                ran_cell = choice(ran_choice)
                ran_cell.set_value(mark)
            elif misc:
                for cell in misc[0]:
                    if cell.is_empty():
                        cell.set_value(mark)
                
                        







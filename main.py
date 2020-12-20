import tkinter

from board import Board
from cell import Cell


def click(x: int, y: int):
    if board.get_selected_cell() is not None:
        pos_x = board.get_selected_cell().get_pos_x()
        pos_y = board.get_selected_cell().get_pos_y()
    board.select_peons(x, y)

    if 'pos_x' in locals():
        display_cell(cells[pos_x][pos_y])
    display_cell(cells[x][y])


def display_cell(cell: Cell):
    x = cell.get_pos_x()
    y = cell.get_pos_y()

    color = cell.peons.color if cell.peons is not None else 'white'

    btn = tkinter.Button(fenetre, bg=color, borderwidth=5, command=lambda x=cell.get_pos_x(), y=cell.get_pos_y(): click(x, y))

    btn.grid(row=x, column=y)


cells = []
for i in range(9):
    row = []
    for j in range(9):
        row.append(Cell(peon=None, position=[i, j]))
    cells.append(row)

if __name__ == '__main__':
    fenetre = tkinter.Tk()
    fenetre.title('Djambi')
    board = Board(cells)
    board.init_board()

    for rowCells in cells:
        for row in rowCells:
            display_cell(row)

    fenetre.mainloop()

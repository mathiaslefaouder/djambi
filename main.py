import tkinter

from cell import Cell

cells = []
for i in range(9):
    row = []
    for j in range(9):
        position = [i, j]
        row.append(Cell(peon=None, position=position))
    cells.append(row)

if __name__ == '__main__':
    fenetre = tkinter.Tk()
    fenetre.title('Djambi')
    # TODO: display cell in board

    fenetre.mainloop()

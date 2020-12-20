from cell import Cell
from peon import Chef, Assasin, Necromobile, Diplomate, Militant, Reporter


class Board:
    """ Board and cell definition """

    def __init__(self, cells: [Cell]):
        self._cells = cells
        self._teams = []
        self._selected_cell = None

    def move(self, x: int, y: int):
        if self._selected_cell is not None:
            cell = self._cells[x][y]
            cell.peons = self._selected_cell.peons
            self._selected_cell.peons = None

    def select_peons(self, x: int, y: int):
        cell = self._cells[x][y]
        if self._selected_cell != cell:
            if self._selected_cell is None:
                self._selected_cell = None
            else:
                self.move(x, y)
                self._selected_cell = None
        else:
            self._selected_cell = None

    def init_board(self):
        team1 = 'Yellow'
        team2 = 'Green'
        team3 = 'Blue'
        team4 = 'Red'

        """ team 1 """
        self._cells[0][0].peons = Chef(team1)
        self._cells[0][1].peons = Assasin(team1)
        self._cells[1][0].peons = Reporter(team1)
        self._cells[1][1].peons = Diplomate(team1)
        self._cells[2][2].peons = Necromobile(team1)
        self._cells[0][2].peons = Militant(team1)
        self._cells[1][2].peons = Militant(team1)
        self._cells[2][0].peons = Militant(team1)
        self._cells[2][1].peons = Militant(team1)

        """ team 2 """
        self._cells[0][8].peons = Chef(team2)
        self._cells[0][7].peons = Assasin(team2)
        self._cells[1][8].peons = Reporter(team2)
        self._cells[1][7].peons = Diplomate(team2)
        self._cells[2][6].peons = Necromobile(team2)
        self._cells[0][6].peons = Militant(team2)
        self._cells[1][6].peons = Militant(team2)
        self._cells[2][8].peons = Militant(team2)
        self._cells[2][7].peons = Militant(team2)

        """ team 3 """
        self._cells[8][0].peons = Chef(team3)
        self._cells[8][1].peons = Assasin(team3)
        self._cells[7][0].peons = Reporter(team3)
        self._cells[7][1].peons = Diplomate(team3)
        self._cells[6][2].peons = Necromobile(team3)
        self._cells[8][2].peons = Militant(team3)
        self._cells[7][2].peons = Militant(team3)
        self._cells[6][0].peons = Militant(team3)
        self._cells[6][1].peons = Militant(team3)

        """ team 4 """
        self._cells[8][8].peons = Chef(team4)
        self._cells[8][7].peons = Assasin(team4)
        self._cells[7][8].peons = Reporter(team4)
        self._cells[7][7].peons = Diplomate(team4)
        self._cells[6][6].peons = Necromobile(team4)
        self._cells[8][6].peons = Militant(team4)
        self._cells[7][6].peons = Militant(team4)
        self._cells[6][8].peons = Militant(team4)
        self._cells[6][7].peons = Militant(team4)

    def get_selected_cell(self):
        return self._selected_cell

    def set_selected_cell(self, selected_cell: Cell):
        self._selected_cell = selected_cell

    def get_cells(self):
        return self._cells

    def set_cells(self, cells: []):
        self._cells = cells

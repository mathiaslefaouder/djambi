from cell import Cell


class Board:
    """ Board and cell definition """

    def __init__(self, cells: [Cell]):
        self._cells = cells
        self._teams = []
        self._selected_cell = None

    def move(self):
        pass

    def get_empty_cells(self):
        pass

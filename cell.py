from peon import Peon


class Cell:
    """ Cell class for board"""

    def __init__(self, peon, position: list):
        self._peon = peon
        self._position = position

    def get_peon(self):
        return self._peon

    def set_peon(self, peon: Peon):
        self._peon = peon

    def get_pos_x(self):
        return self._position[0]

    def get_pos_y(self):
        return self._position[1]

    peons = property(get_peon, set_peon)

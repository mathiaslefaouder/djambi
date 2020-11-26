import peon


class Assasin(peon):
    _icon: str = "icons/assassin.png"

    def available_move(self):
        return True

    def after_move(self):
        return True

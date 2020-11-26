import peon


class Diplomate(peon):
    _icon: str = "icons/diplomate.png"

    def available_move(self):
        return True

    def after_move(self):
        return True

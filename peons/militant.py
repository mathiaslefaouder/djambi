import peon


class Militant(peon):
    _icon: str = "icons/militant.png"

    def available_move(self):
        return True

    def after_move(self):
        return True

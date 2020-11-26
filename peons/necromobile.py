import peon


class Necromobile(peon):
    _icon: str = "icons/necromobile.png"

    def available_move(self):
        return True

    def after_move(self):
        return True

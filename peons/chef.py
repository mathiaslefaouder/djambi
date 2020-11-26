import peon


class Chef(peon):
    _icon: str = "icons/chief.png"

    def available_move(self):
        return True

    def after_move(self):
        return True
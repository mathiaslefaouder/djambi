import peon


class Reporter(peon):
    _icon: str = "icons/reporter.png"

    def available_move(self):
        return True

    def after_move(self):
        return True

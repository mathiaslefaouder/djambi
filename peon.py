import abc


class Peon(abc):

    def __init__(self, color: str):
        self._is_alive = True
        self._color = color
        self._icon: str

    def available_move(self):
        return True

    def after_move(self):
        return True

    def get_icon(self):
        return self._icon

    def get_color(self):
        return self._color

    def set_color(self, color: str):
        self._color = color

    def get_is_alive(self):
        return self._is_alive

    def set_is_alive(self, is_alive: bool):
        self._is_alive = is_alive

    icon = property(get_icon)
    color = property(get_color, set_color)
    is_alive = property(get_is_alive, set_is_alive)


class Assasin(Peon):
    _icon: str = "icons/assassin.png"

    def available_move(self):
        return True

    def after_move(self):
        return True


class Chef(Peon):
    _icon: str = "icons/chief.png"

    def available_move(self):
        return True

    def after_move(self):
        return True


class Diplomate(Peon):
    _icon: str = "icons/diplomate.png"

    def available_move(self):
        return True

    def after_move(self):
        return True


class Militant(Peon):
    _icon: str = "icons/militant.png"

    def available_move(self):
        return True

    def after_move(self):
        return True


class Necromobile(Peon):
    _icon: str = "icons/necromobile.png"

    def available_move(self):
        return True

    def after_move(self):
        return True


class Reporter(Peon):
    _icon: str = "icons/reporter.png"

    def available_move(self):
        return True

    def after_move(self):
        return True

class Cell:
    """ A class that creates an empty Tic Tac Toe cell object. """
    def __init__(self):
        self.value = None

    def is_empty(self):
        return not bool(self.value)

    def get_value(self):
        return self.value

    def set_value(self, mark):
        self.value = mark
class Base:
    def __init__(self, type, number):
        self.type = type
        self.number = number

    def _is_libre(self, loop):
        return 0

    def __str__(self):
        return self.type+str(self.number)
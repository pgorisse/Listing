class Base:
    def __init__(self, type, number):
        self.type = type
        self.number = number

    def __str__(self):
        return self.type+str(self.number)
class Base:
    def __init__(self, type, number):
        self.type = str(type)
        self.number = str(number)

    def __str__(self):
        return self.type+str(self.number)

    def __eq__(self, other):
        if str(self.type) == str(other.type) and int(self.number) == int(other.number):
            return True
        return False

    def __contains__(self, item):
        for base in item:
            if self.__eq__(base):
                return True
        return False
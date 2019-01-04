class Interaction:
    def __init__(self, base1, type, base2):
        self.base1 = base1
        self.type = str(type)
        self.base2 = base2

    def __str__(self):
        return str(self.base1) + " " + self.type + " " + str(self.base2)

    def __eq__(self, other):
        if self.base1.__eq__(other.base1) and self.base2.__eq__(other.base2) and self.type == other.type:
            return True
        if self.base2.__eq__(other.base1) and self.base1.__eq__(other.base2) and self.type == other.type:
            return True
        return False

    def is_canonique(self):
        if self.type == "cWW":
            if [str(self.base1.type), str(self.base2.type)] in [["A", "U"], ["U", "A"], ["G", "C"], ["C", "G"], ["G", "U"],
                                                      ["U", "G"]]:
                return True
        return False

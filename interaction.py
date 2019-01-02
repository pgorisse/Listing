class Interaction:
    def __init__(self, base1, type, base2):
        self.base1 = base1
        self.type = type
        self.base2 = base2

    def __str__(self):
        return str(self.base1) + " " + self.type + " " + str(self.base2)

    def is_canonique(self):
        if self.type == "cWW":
            if [self.base1.type, self.base2.type] in [["A", "U"], ["U", "A"], ["G", "C"], ["C", "G"], ["G", "U"],
                                                      ["U", "G"]]:
                return True
            print(self.type)
        return False

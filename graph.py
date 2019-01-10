from base import Base
from interaction import Interaction


class Graph:
    def __init__(self, bases, interactions, loop_name):
        self.V = bases
        self.E = interactions
        self.interacting_interfaces = []
        self.loop_name = loop_name

    def __str__(self):
        return "V: " + str([str(base) for base in self.V]) + "\nE: " + str(
            [str(inter) for inter in self.E]) + "\nInteracting interfaces: " + str(self.interacting_interfaces)

    def __eq__(self, other):
        for base in self.V:
            if base not in other.V:
                return False
        for base in other.V:
            if base not in self.V:
                return False
        for inter in self.E:
            if inter not in other.E:
                return False
        for inter in other.E:
            if inter not in self.E:
                return False
        return True

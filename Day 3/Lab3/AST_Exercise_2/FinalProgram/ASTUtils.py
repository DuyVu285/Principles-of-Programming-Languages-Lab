from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple


def printlist(lst, f=str, start="[", sepa=",", end="]"):
    return start + sepa.join(f(i) for i in lst) + end


class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self, param)


class Exp(AST):
    __metaclass__ = ABCMeta
    pass


@dataclass
class IntStatement(Exp):
    identifiers: List[str]

    def __str__(self):
        return f"IntStatement({printlist(self.identifiers)})"

    def accept(self, v, param):
        return v.visitIntStatement(self, param)


@dataclass
class FloatStatement(Exp):
    identifiers: List[str]

    def __str__(self):
        return f"FloatStatement({printlist(self.identifiers)})"

    def accept(self, v, param):
        return v.visitFloatStatement(self, param)


@dataclass
class Id(Exp):
    def __str__(self):
        return "ID"

    def accept(self, v, param):
        return v.visitIdentifier(self, param)


@dataclass
class Prog(AST):
    expr: List[Exp]

    def __str__(self):
        return "Prog(" + printlist(self.expr, start="", end="") + ")"

    def accept(self, v, param):
        return v.visitProgram(self, param)

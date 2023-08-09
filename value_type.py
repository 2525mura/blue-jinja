from enum import Enum, auto


class ValueType(Enum):
    Int = auto()
    Float = auto()
    String = auto()


class Language(Enum):
    Cpp = auto()
    Swift = auto()

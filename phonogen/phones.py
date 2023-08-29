from dataclasses import dataclass
from typing import TypeAlias, Literal, TypeVar, Generic

T = TypeVar("T")


Manner: TypeAlias = Literal[
    "plosive",
    "nasal",
    "trill",
    "tapflap",
    "fricative",
    "lateralfricative",
    "approximant",
    "lateralapproximant",
]

Place: TypeAlias = Literal[
    "bilabial",
    "labiodental",
    "dental",
    "alveolar",
    "postalveolar",
    "retroflex",
    "palatal",
    "velar",
    "uvular",
    "pharyngeal",
    "glottal",
]


@dataclass
class Phone:
    glyph: str

    def __str__(self) -> str:
        return f"\\[{self.glyph}]"

    def __rich__(self) -> str:
        return f"[red]{self}[/red]"


@dataclass
class Consonant(Phone):
    manner: Manner
    place: Place
    voiced: bool
    semivowel: bool = False

    def __hash__(self):
        return hash((self.manner, self.place, self.voiced, self.semivowel))


@dataclass
class Vowel(Phone):
    closeness: float
    frontness: float
    rounded: bool

    def __hash__(self):
        return hash((self.closeness, self.frontness, self.rounded))


@dataclass
class Phoneme:
    glyph: str
    allophones: list[Phone]

    complexity: float = 1

    def __str__(self) -> str:
        return f"/{self.glyph}/"

    def __rich__(self) -> str:
        return f"[cyan]{self}[/cyan]"

    def __hash__(self):
        return hash((self.glyph, tuple(self.allophones), self.complexity))


CLOSE = 1
NEAR_CLOSE = 0.875
CLOSE_MID = 0.75
MID = 0.5
OPEN_MID = 0.25
NEAR_OPEN = 0.125
OPEN = 0

FRONT = 1
NEAR_FRONT = 0.75
CENTER = 0.5
NEAR_BACK = 0.25
BACK = 0

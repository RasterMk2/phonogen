from collections.abc import Iterable
from itertools import product
from dataclasses import dataclass

from phonogen.phones import Phoneme
from functools import partial


@dataclass
class Combo:
    seq: Iterable[Iterable[Phoneme]]
    complexity: float = 1


@dataclass
class Syllable:
    syl: str
    complexity: float

    def __hash__(self):
        return hash((self.syl, self.complexity))


def str_from_iter(itr: Iterable[str]) -> str:
    return "".join(itr)


def create_syllable(
    phonemes: Iterable[Phoneme], complexity_multiplier: float
) -> Syllable:
    syl = ""
    complexity = 0
    for pme in phonemes:
        syl += pme.glyph
        complexity += pme.complexity

    return Syllable(syl, complexity * complexity_multiplier)


def syl_product(combo: Combo) -> set[Syllable]:
    return set(
        map(
            partial(create_syllable, complexity_multiplier=combo.complexity),
            product(*combo.seq),
        )
    )


def generate_syllables(combos: Iterable[Combo]):
    return set().union(*map(syl_product, combos))

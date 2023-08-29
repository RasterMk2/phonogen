from collections.abc import Sequence
from dataclasses import dataclass
from random import choice

from phonogen.syllables import Syllable


@dataclass
class Word:
    word: str
    complexity: float


def create_word(syllables: Sequence[Syllable], syl_count: int):
    word = ""
    complexity = 0

    for _ in range(syl_count):
        syl = choice(syllables)
        word += syl.syl
        complexity += syl.complexity

    return Word(word, complexity)

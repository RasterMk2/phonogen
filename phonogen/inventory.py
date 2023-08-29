from phonogen.phones import Phoneme, Consonant, Vowel, Manner, Place, Phone
from collections.abc import Container, Generator


class Inventory:
    phonemes: list[Phoneme]

    def __init__(self, phonemes: list[Phoneme] | None = None):
        if phonemes is None:
            phonemes = []

        self.phonemes = phonemes

    def get_phones(self) -> set[Phone]:
        phones = set()
        for pme in self.phonemes:
            for pne in pme.allophones:
                phones.add(pne)

        return phones

    def get_allophones(self) -> Generator[tuple[Phoneme, Phone], None, None]:
        for pme in self.phonemes:
            for pne in pme.allophones:
                yield pme, pne

    def get_consonants(
        self,
        *,
        manners: Container[Manner] | None = None,
        places: Container[Place] | None = None,
        semivowel: bool | None = None
    ) -> set[Phoneme]:
        consonants = set()
        for pme, pne in self.get_allophones():
            if not isinstance(pne, Consonant):
                continue
            if manners is not None and pne.manner not in manners:
                continue
            if places is not None and pne.place not in places:
                continue
            if semivowel is not None and pne.semivowel != semivowel:
                continue
            consonants.add(pme)

        return consonants

    def get_vowels(self) -> set[Phoneme]:
        vowels = set()
        for pme, pne in self.get_allophones():
            if isinstance(pne, Vowel):
                vowels.add(pme)

        return vowels

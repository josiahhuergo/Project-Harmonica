from typing import Iterator

from more_itertools import powerset
from harmonica.pitch._scales import PitchClassSet


__all__ = ["find_pcset_supersets"]

PCSetResults = Iterator[PitchClassSet]


def find_pcset_supersets(pitch_class_set: PitchClassSet) -> PCSetResults:
    complement = set(range(pitch_class_set.modulus)) - set(
        pitch_class_set.pitch_classes
    )
    pcset_powerset = powerset(complement)

    for other_pitch_classes in pcset_powerset:
        pitch_classes = sorted(
            pitch_class_set.pitch_classes + list(other_pitch_classes)
        )
        yield PitchClassSet(
            pitch_classes=pitch_classes,
            modulus=pitch_class_set.modulus,
        )


def find_pcsets_containing_pclass(pclass: int, mod: int) -> PCSetResults:
    return find_pcset_supersets(PitchClassSet([pclass], mod))


def filter_min_size(pcsets: PCSetResults, min: int) -> PCSetResults:
    return filter(lambda pcset: pcset.cardinality >= min, pcsets)


def filter_max_size(pcsets: PCSetResults, max: int) -> PCSetResults:
    return filter(lambda pcset: pcset.cardinality <= max, pcsets)

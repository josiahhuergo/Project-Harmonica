from itertools import product

from harmonica.pitch._pitchset import PitchSet
from harmonica.pitch._scales import PitchClassSet


def diatonic_neighborhood(
    pitch_set: PitchSet, pitch_class_set: PitchClassSet, proximity: int
) -> list[PitchSet]:
    """Returns a list of pitch sets belonging to a pitch class set that
    are proximal to a given pitch set.

    Useful for finding successive chord voicings that have smooth voice
    leading with the previous chord."""

    assert proximity >= 0, "Proximity must be non-negative."

    pitch_neighborhoods: list[list[int]] = []

    for pitch in pitch_set:
        # Take the neighborhood around each pitch in the set
        pitch_neighborhood = range(pitch - proximity, pitch + proximity + 1)

        # We only want the pitches belonging to the pitch class set
        pitch_neighborhood = pitch_class_set.scale_function(
            pitch_class_set[0]
        ).in_range(pitch - proximity, pitch + proximity)

        pitch_neighborhoods.append(pitch_neighborhood)

    # Now we take the cartesian product of these pitch neighborhoods to yield our results
    neighborhood = [list(x) for x in product(*pitch_neighborhoods)]
    neighborhood = [PitchSet(pitches) for pitches in neighborhood]

    return neighborhood

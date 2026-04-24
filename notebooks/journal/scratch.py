from harmonica import pitch
from harmonica.pitch._pitchset import PitchSet
from harmonica.pitch._scales import PitchClassSet


pset = PitchSet([0, 10, 19])
pcset = PitchClassSet([1, 4, 8, 10], 12)

neighborhood = pitch.diatonic_neighborhood(pset, pcset, 3)

[print(x) for x in neighborhood]

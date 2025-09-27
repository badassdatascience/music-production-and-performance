
#
# Later more enharmonics will be added, or
# maybe calculated to account for double-
# and triple-accidentals:
#
enharmonics_map = {
    'Cb' : 'B',
    'C#' : 'Db',
    'D#' : 'Eb',
    'E#' : 'F',
    'Fb' : 'E',
    'Gb' : 'F#',
    'G#' : 'Ab',
    'A#' : 'Bb',
    'B#' : 'C',
}

#
# define a C-based chromatic scale with its enharmonic spellings (up to two accidentals per spelling)                    #
# We are not using this at the moment; keeping it around
# while I decide whether this approach makes sense in any
# way:
#
chromatic_c_based_enharmonic_spellings = [
    ['Dbb', 'C', 'B#'],
    ['Db', 'C#', 'B##'],
    ['Ebb', 'D', 'C##'],
    ['Fbb', 'Eb', 'D#'],
    ['Fb', 'E', 'D##'],
    ['Gbb', 'F', 'E#'],
    ['Gb', 'F#', 'E##'],
    ['Abb', 'G', 'F##'],
    ['Ab', 'G#'],
    ['Bbb', 'A', 'G##'],
    ['Cbb', 'Bb', 'A#'],
    ['Cb', 'B', 'A##'],
]


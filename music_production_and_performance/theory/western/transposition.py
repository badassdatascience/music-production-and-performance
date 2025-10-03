import numpy as np

def chromatic_transpose(
    notes_as_numbers : np.array,
    chromatic_interval : np.int16 = 7,
    verbose : bool = False,
) -> (np.array, np.array):

    pitches_as_numbers = notes_as_numbers + chromatic_interval
    octaves = np.int16(np.floor(np.float16(pitches_as_numbers / 12.))) - 1

    if verbose:
        print('Sequence provided by user:', notes_as_numbers)
        print('Chromatic interval provided by user:', chromatic_interval)
        print('Transposed pitch numbers:', pitches_as_numbers)
        print('Corresponding octaves:', octaves)
        print()
    
    return pitches_as_numbers, octaves
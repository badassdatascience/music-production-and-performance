import numpy as np

def chromatic_transpose(
    notes_as_numbers : np.array,
    chromatic_interval : np.int16 = 7,
    verbose : bool = False,
) -> (np.array, np.array):

    pitches_as_numbers = notes_as_numbers + chromatic_interval
    octaves = np.int16(np.floor(np.float16(pitches_as_numbers / 12.))) - 1

    if verbose:
        print(notes_as_numbers)
        print(pitches_as_numbers)
        print(octaves)
        print()
    
    return pitches_as_numbers, octaves
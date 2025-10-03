
#
# load useful system libraries
#
import numpy as np

#
# load useful local libraries
#
from music_production_and_performance.theory.western.scales.chromatic import chromatic_scale_numeric

# ?
chromatic_scale_numeric = np.array(chromatic_scale_numeric)

#
# define a function to extract octave numbers from MIDI notes
#
def MIDI_number_to_scientific_pitch_octave(
    pitches_as_numbers : np.array,
) -> np.array:
    octaves = np.int16(np.floor(np.float16(pitches_as_numbers / 12.))) - 1
    return octaves

#
# define a function to chromatically transpose
#
def MIDI_number_chromatic_transpose(
    notes_as_numbers : np.array,
    chromatic_interval : np.int16 = 7,
    verbose : bool = False,
) -> (np.array, np.array):

    pitches_as_numbers = notes_as_numbers + chromatic_interval
    octaves = MIDI_number_to_scientific_pitch_octave(pitches_as_numbers)
    
    if verbose:
        print('Sequence provided by user:', notes_as_numbers)
        print('Chromatic interval provided by user:', chromatic_interval)
        print('Transposed pitch numbers:', pitches_as_numbers)
        print('Corresponding octaves:', octaves)
        print()
    
    return pitches_as_numbers, octaves



def main():
    x = MIDI_number_chromatic_transpose(chromatic_scale_numeric, verbose = True)
    x = MIDI_number_chromatic_transpose(chromatic_scale_numeric, chromatic_interval = -7, verbose = True)
    x = MIDI_number_chromatic_transpose(chromatic_scale_numeric, chromatic_interval = 60, verbose = True)
    x = MIDI_number_chromatic_transpose(chromatic_scale_numeric, chromatic_interval = 120, verbose = True)
    x = MIDI_number_chromatic_transpose(chromatic_scale_numeric, chromatic_interval = 127, verbose = True)
    x = MIDI_number_chromatic_transpose(chromatic_scale_numeric, chromatic_interval = 132, verbose = True)

if __name__ == '__main__':
    main()

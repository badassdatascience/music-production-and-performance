#
# load useful system libraries
#
import numpy as np

#
# define a function to test for MIDI value range violation
#
def MIDI_number_test_value_ranges(
    pitches_as_numbers : np.array,
    MIDI_min_allowed_value : np.int16 = 0,
    MIDI_max_allowed_value : np.int16 = 127,
):
    assert np.min(np.int8(pitches_as_numbers >= MIDI_min_allowed_value)) == 1
    assert np.min(np.int8(pitches_as_numbers <= MIDI_max_allowed_value)) == 1

    return True
    

        

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
    MIDI_min_allowed_value : np.int16 = 0,
    MIDI_max_allowed_value : np.int16 = 127,
) -> (np.array, np.array):

    pitches_as_numbers = notes_as_numbers + chromatic_interval
    octaves_of_the_pitches = MIDI_number_to_scientific_pitch_octave(pitches_as_numbers)
    
    if verbose:
        print('Sequence provided by user:', notes_as_numbers)
        print('Chromatic interval provided by user:', chromatic_interval)
        print('Transposed pitch numbers:', pitches_as_numbers)
        print('Corresponding octaves:', octaves_of_the_pitches)
        print()
    #
    # check note range and throw and exception if MIDI range is violated
    #
    MIDI_number_test_value_ranges(
        pitches_as_numbers,
        MIDI_min_allowed_value = MIDI_min_allowed_value,
        MIDI_max_allowed_value = MIDI_max_allowed_value,
    )


    #assert np.min(np.int8(pitches_as_numbers >= MIDI_min_allowed_value)) == 1
    #assert np.min(np.int8(pitches_as_numbers <= MIDI_max_allowed_value)) == 1

    return pitches_as_numbers, octaves_of_the_pitches



def main():
    chromatic_scale_numeric = np.arange(0, 12)
    x = MIDI_number_chromatic_transpose(chromatic_scale_numeric, verbose = True)
    x = MIDI_number_chromatic_transpose(chromatic_scale_numeric, chromatic_interval = -7, verbose = True)
    x = MIDI_number_chromatic_transpose(chromatic_scale_numeric, chromatic_interval = 60, verbose = True)
    x = MIDI_number_chromatic_transpose(chromatic_scale_numeric, chromatic_interval = 110, verbose = True)
    x = MIDI_number_chromatic_transpose(chromatic_scale_numeric, chromatic_interval = 120, verbose = True)
    
if __name__ == '__main__':
    main()

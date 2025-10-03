#
# load useful system libraries
#
import numpy as np

#
# Convert MIDI number to frequency
#
# (This defaults to 12-tone equal temperament,
# and I haven't implemented anything else yet).
#
def MIDI_note_number_array_to_frequency_array(
    midi_note_number : np.array, 
    method : str = '12-tone equal temperament',
    concert_frequency_a4 : np.float64 = 440.,
    concert_midi_note_number_a4 : np.int16 = 69,
) -> np.array:

    #
    # because we are not worrying about any other
    # temperment at the moment
    #
    assert method == '12-tone equal temperament', \
        f"Please use '12-tone equal temperament' as the method argument (the default), as I have not implemented anything else yet."
    
    if method == '12-tone equal temperament':
        frequency = concert_frequency_a4 * (np.power(2., (1./12.)) ** (midi_note_number - concert_midi_note_number_a4))

    return frequency

#
# define a function to test for MIDI value range violation
#
def MIDI_note_number_array_to_test_value_ranges(
    pitches_as_numbers : np.array,
    MIDI_min_allowed_value : np.int16 = 0,
    MIDI_max_allowed_value : np.int16 = 127,
) -> bool:

    # test ranges
    assert np.min(np.int8(pitches_as_numbers >= MIDI_min_allowed_value)) == 1, \
        f"A number in your pitch series is smaller than the minimum accepted MIDI value of {MIDI_min_allowed_value}"
    assert np.min(np.int8(pitches_as_numbers <= MIDI_max_allowed_value)) == 1, \
        f"A number in your pitch series exceeds the maximum accepted MIDI value of {MIDI_max_allowed_value}"

    return True

#
# identifies the pitch class of a given MIDI note number
#
def MIDI_note_number_array_to_pitch_class_array(
    pitches_as_numbers : np.array,
) -> np.array:
    return pitches_as_numbers % 12

#
# define a function to extract octave numbers from MIDI notes
#
def MIDI_note_number_array_to_scientific_pitch_octave_array(
    pitches_as_numbers : np.array,
) -> np.array:
    octaves = np.int16(np.floor(np.float16(pitches_as_numbers / 12.))) - 1
    return octaves

#
# define a function to chromatically transpose
#
def MIDI_note_number_array_to_chromatic_transpose_array(
    notes_as_numbers : np.array,
    chromatic_interval : np.int16 = 7,
    MIDI_min_allowed_value : np.int16 = 0,
    MIDI_max_allowed_value : np.int16 = 127,
) -> (np.array, np.array, np.array):

    #
    # compute the transposition
    #
    pitches_as_numbers = notes_as_numbers + chromatic_interval
    
    #
    # check note range and throw and exception if MIDI range is violated
    #
    MIDI_note_number_array_to_test_value_ranges(
        pitches_as_numbers,
        MIDI_min_allowed_value = MIDI_min_allowed_value,
        MIDI_max_allowed_value = MIDI_max_allowed_value,
    )
    
    return pitches_as_numbers

#
# verbose summary display of some of these functions in action
#
def verbose_summary(
        chromatic_series_numeric : np.array,
        chromatic_interval : np.int16 = 7,
) -> None:
    pitches_as_numbers = MIDI_note_number_array_to_chromatic_transpose_array(chromatic_series_numeric, chromatic_interval = chromatic_interval)
    octaves_of_the_pitches_C_negative_1_based = MIDI_note_number_array_to_scientific_pitch_octave_array(pitches_as_numbers)
    pitch_classes_zero_based = MIDI_note_number_array_to_pitch_class_array(pitches_as_numbers)

    print('Sequence provided by user:', chromatic_series_numeric)
    print('Chromatic interval provided by user:', chromatic_interval)
    print('Transposed pitch numbers:', pitches_as_numbers)
    print('Corresponding pitch classes:', pitch_classes_zero_based)
    print('Corresponding octaves:', octaves_of_the_pitches_C_negative_1_based)

#
# main function
#
def main():
    chromatic_scale_numeric = np.arange(0, 12)
    
    print(); x = verbose_summary(chromatic_scale_numeric)
    print(); x = verbose_summary(chromatic_scale_numeric, chromatic_interval = 0)
    print(); x = verbose_summary(chromatic_scale_numeric, chromatic_interval = 60)
    print(); x = verbose_summary(chromatic_scale_numeric, chromatic_interval = 110)
    print(); x = verbose_summary(chromatic_scale_numeric, chromatic_interval = 108)

    #
    # These are designed to fail the assertions, used to test the assertions
    #
    if False:
        print(); x = verbose_summary(chromatic_scale_numeric, chromatic_interval = -7)
        print(); x = verbose_summary(chromatic_scale_numeric, chromatic_interval = 120)
    
    print()
        
    #
    # test the frequency calculation(s)
    #
    assert np.all(np.round(MIDI_note_number_array_to_frequency_array(np.array([60, 69, 0])), 4) == np.array([261.6256, 440., 8.1758]))

#
# command-line entry point (for testing)
#
if __name__ == '__main__':
    main()

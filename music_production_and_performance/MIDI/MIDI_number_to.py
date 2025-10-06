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

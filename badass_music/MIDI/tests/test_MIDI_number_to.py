import unittest
import numpy as np

from badass_music.MIDI.MIDI_number_to import MIDI_note_number_array_to_frequency_array
from badass_music.MIDI.MIDI_number_to import MIDI_note_number_array_to_chromatic_transpose_array
from badass_music.MIDI.MIDI_number_to import MIDI_note_number_array_to_pitch_class_array
from badass_music.MIDI.MIDI_number_to import MIDI_note_number_array_to_scientific_pitch_octave_array
    
class TestMidiNumberTo(unittest.TestCase):

    #
    # works like a constructor
    #
    def setUp(self):
        chromatic_series_numeric = np.arange(0, 12)
        self.pitches_as_numbers_67 = MIDI_note_number_array_to_chromatic_transpose_array(chromatic_series_numeric, chromatic_interval = 67)
        self.pitches_as_numbers_7 = MIDI_note_number_array_to_chromatic_transpose_array(chromatic_series_numeric, chromatic_interval = 7)

    #
    # test frequency computation
    #
    def test_MIDI_note_number_array_to_frequency_array(self):
        test = (
            np.all(
                np.round(
                    MIDI_note_number_array_to_frequency_array(
                        np.array(
                            [60, 69, 0]
                        )
                    ),
                    4
                ) == np.array(
                    [261.6256, 440., 8.1758]
                )
            )
        )
        self.assertEqual(test, bool(True))

    #
    # test chromatic interval-based transposition
    #
    def test_MIDI_note_number_array_to_chromatic_transpose_array(self):
        self.assertTrue(bool(np.all([i == j for i, j in zip(self.pitches_as_numbers_67, np.arange(67, 67 + 12))])))
        
    #
    # test computation of pitch classes (to eventually get to scientific notation)
    #
    def test_MIDI_note_number_array_to_pitch_class_array(self):
        self.assertTrue(bool(np.all([i == j for i, j in zip(MIDI_note_number_array_to_pitch_class_array(self.pitches_as_numbers_7), (np.arange(0, 12) + 7) % 12)])))

    #
    # test computation of octaves (for scientific notation)
    #
    def test_MIDI_note_number_array_to_scientific_pitch_octave_array(self):
        octaves_computed = MIDI_note_number_array_to_scientific_pitch_octave_array(self.pitches_as_numbers_67)
        octaves_specified = np.array([4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5])
        self.assertTrue(bool(np.all([i == j for i, j in zip(octaves_computed, octaves_specified)])))

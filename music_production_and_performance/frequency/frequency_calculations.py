import numpy as np
import librosa

def calculate_frequency(
    midi_note_number, 
    method = '12-tone equal temperament',
    concert_frequency_a4 = 440.,
    concert_midi_note_number_a4 = 69,
):
    frequency = np.nan
    
    if method == '12-tone equal temperament':
        frequency = concert_frequency_a4 * (np.power(2., (1./12.)) ** (midi_note_number - concert_midi_note_number_a4))

    return frequency

#
# librosa: pitch to frequency
#
# This is just an external function called by a more
# verbose name to ease development and documentation 
# clarity
#
# Appears to use equal temperament by default:
#
def get_librosa_scientific_pitch_notation_to_hz(pitch_in_scientific_notation):
    return librosa.note_to_hz(pitch_in_scientific_notation)

#
# librosa: pitch to MIDI number
#
# This is just an external function called by a more
# verbose name to ease development and documentation 
# clarity:
#
def get_librosa_scientific_pitch_notation_to_MIDI(pitch_in_scientific_notation):
    return librosa.note_to_midi(pitch_in_scientific_notation)




if __name__ == '__main__':
    print()
    print(calculate_frequency(60))
    print(get_librosa_scientific_pitch_notation_to_hz('C4'))
    print()
    print(calculate_frequency(69))
    print(get_librosa_scientific_pitch_notation_to_hz('A4'))
    print()
    print(get_librosa_scientific_pitch_notation_to_MIDI('C4'))
    print(get_librosa_scientific_pitch_notation_to_MIDI('A4'))

    print()
    print(get_librosa_scientific_pitch_notation_to_MIDI('Cb4'))
    print(get_librosa_scientific_pitch_notation_to_MIDI('C#4'))
    print(get_librosa_scientific_pitch_notation_to_MIDI('Ab4'))
    print(get_librosa_scientific_pitch_notation_to_MIDI('Abb4'))
    print(get_librosa_scientific_pitch_notation_to_MIDI('C##4'))
    print()

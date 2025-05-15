import numpy as np

class CamelotWheel():

    def __init__(self):
        self.chromatic_scale_numeric = np.arange(0, 12, dtype = np.uint8)

        # using Mixed In Key's enharmonic spellings
        self.array_chromatic_scale_pitch_classes = np.array(['C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B'], dtype = str)
        
        self.compute_circle_of_fifths()
        self.compute_minor_offset()
        self.compute_camelot_wheel()
    
    def compute_circle_of_fifths(self):
        circle_of_fifths = [0]
        for pitch_class in self.chromatic_scale_numeric[1:]:
            circle_of_fifths.append((circle_of_fifths[-1] + 7) % 12)
        self.circle_of_fifths_numeric = np.array(circle_of_fifths, dtype = np.uint8)

    def compute_minor_offset(self):
        minor_offset_fifths = []
        for pitch_class in self.circle_of_fifths_numeric:
            minor_offset_fifths.append((pitch_class + 9) % 12)
        self.minor_offset_fifths_numeric = np.array(minor_offset_fifths, dtype = np.uint8)

    def compute_camelot_wheel(self):

        def get_camelot_symbols(symbol):
            return np.array([str(((q + 7) % 12) + 1) + symbol for q in range(0, 12)], dtype = str)

        camelot_minor = get_camelot_symbols('A')
        camelot_major = get_camelot_symbols('B')

        self.camelot_wheel_minor_layer = list(
            zip(self.array_chromatic_scale_pitch_classes[self.minor_offset_fifths_numeric], camelot_minor)
        )
        self.camelot_wheel_major_layer = list(
            zip(self.array_chromatic_scale_pitch_classes[self.circle_of_fifths_numeric], camelot_major)
        )
        self.camelot_combined_minor_and_major = list(zip(self.camelot_wheel_minor_layer, self.camelot_wheel_major_layer))
        
    def summary(self):
        return self.camelot_combined_minor_and_major

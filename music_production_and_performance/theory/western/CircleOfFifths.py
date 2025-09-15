import numpy as np

class CircleOfFifths():

    def __init__(
        self,
        chromatic_scale_pitch_classes = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B'],
        chromatic_scale_numeric = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    ):
        self.chromatic_scale_numeric = np.array(chromatic_scale_numeric)
        self.chromatic_scale_pitch_classes = np.array(chromatic_scale_pitch_classes)
        self.compute_circle_of_fifths_numerically()
        self.compute_circle_of_fifths_pitch_class_names()
    
    def compute_circle_of_fifths_numerically(self):
        circle_of_fifths = [0]
        for pitch_class in self.chromatic_scale_numeric[1:]:
            circle_of_fifths.append((circle_of_fifths[-1] + 7) % 12)
        self.circle_of_fifths_numeric = np.array(circle_of_fifths, dtype = np.uint8)

    def compute_circle_of_fifths_pitch_class_names(self):
        self.circle_of_fifths = list(self.chromatic_scale_pitch_classes[self.circle_of_fifths_numeric])

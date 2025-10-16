
import pprint as pp
import numpy as np
from badass_music.theory.western.scales.chromatic import chromatic_scale_pitch_class_names

# maybe?
from badass_music.theory.western.scales.chromatic import chromatic_scale_alt_formulation



chromatic_scale_pitch_class_names = np.array(chromatic_scale_pitch_class_names)

# Fb-Major has a double flat at Bbb
# For double sharps:  D# major and possibly C# major?

# maybe?
chromatic_scale_alt_formulation = np.array(chromatic_scale_alt_formulation)


major_scale_base_c = np.array(['C', 'D', 'E', 'F', 'G', 'A', 'B'])
major_scale_base_c_numbers_base_8 = np.arange(1, len(major_scale_base_c) + 1)

major_scale_intervals_as_chromatic = []
for pitch_class_no_accidental in major_scale_base_c:
    major_scale_intervals_as_chromatic.append(np.where(chromatic_scale_pitch_class_names == pitch_class_no_accidental)[0][0])
major_scale_intervals_as_chromatic = np.array(major_scale_intervals_as_chromatic)

octave_base_interval_numbers = np.arange(1, len(major_scale_intervals_as_chromatic) + 1)

#print()
#print(major_scale_base_c)
#print(octave_base_interval_numbers)
#print(major_scale_intervals_as_chromatic)










interval_major_to_chromatic_dict = {}
for base_interval_number, chromatic_interval_number in zip(octave_base_interval_numbers, major_scale_intervals_as_chromatic):
    interval_major_to_chromatic_dict[base_interval_number] = chromatic_interval_number


print()
pp.pprint(interval_major_to_chromatic_dict)
print()
    

    

if True:
    
    def stuff(test_interval_major_number, note_list_as_numbers):
        note_list_as_numbers = np.array(note_list_as_numbers)

        # first we establish the corresponding chromatic interval
        test_interval_chromatic = interval_major_to_chromatic_dict[test_interval_major_number]

        print()
        print()
        print(test_interval_major_number)
        print(note_list_as_numbers)
        print(test_interval_chromatic)



        transposed_basic_interval = (note_list_as_numbers - 1) + test_interval_major_number
        transposed_basic_interval_mod_8 = transposed_basic_interval % 8
        print()
        print(transposed_basic_interval)
        print(transposed_basic_interval_mod_8)

        corrected_transposed_basic_interval_mod_8 = np.array([x + 1 if x < test_interval_major_number else x for x in transposed_basic_interval_mod_8])
        print(corrected_transposed_basic_interval_mod_8)
        print()

        #a = np.array([interval_major_to_chromatic_dict[x] for x in corrected_transposed_basic_interval_mod_8])

        modal_transposition = major_scale_base_c[corrected_transposed_basic_interval_mod_8 - 1]
        print(modal_transposition)
        
        transposed_numeric_but_with_wrong_accidentals = np.array([interval_major_to_chromatic_dict[x] for x in corrected_transposed_basic_interval_mod_8])
        print(transposed_numeric_but_with_wrong_accidentals)


        correct_chromatics = np.array([(interval_major_to_chromatic_dict[x] + test_interval_chromatic) % 12 for x in note_list_as_numbers])
        print(correct_chromatics)

        to_shift = correct_chromatics - transposed_numeric_but_with_wrong_accidentals
        results = []
        for pitch_class, step in zip(modal_transposition, to_shift):
            accidentals = ''
            if step >= 1:
                accidentals = '#' * step
            elif step <= -1:
                accidentals = 'b' * abs(step)
            results.append(pitch_class + accidentals)
        print(results)

        

n = 5
stuff(n, octave_base_interval_numbers)


# # a = major_scale_base_c

# # print(a)
# # print(octave_base_interval_numbers)
# # b = ((octave_base_interval_numbers + n) - 1) % 8
# # print(b)
# # c = np.array([x - 1 if x >= n else x for x in b])
# # print(c)
# # print(major_scale_base_c[c])


print()


class Interval():
    def __init__(self, number, quality, direction = 'up'):
        # 1 is unison
        # 8 is octave
        # 16 is two octaves

        assert quality in ['perfect', 'major', 'minor', 'augmented', 'diminished']
        assert direction in ['up', 'down']

        self.number = number
        self.quality = quality
        self.direction = direction

    

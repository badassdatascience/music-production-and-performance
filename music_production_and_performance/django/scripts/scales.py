








#
# import the Django boilerplate code
#
import music_production_and_performance.django.django_boilerplate
##from music_production_and_performance.config import config

from theory_western.models import PitchClass
from music_production_and_performance.theory.western.scales.scales import *

print()
print(scale_Major)
print(scale_minor)
print()

def get_pitchclass_list_by_pitchclass_name(pitch_class_list):
    pitch_class_object_list = []
    for pitch_name in pitch_class_list:
        pc = PitchClass.objects.get(name = pitch_name)
        pitch_class_object_list.append(pc)
    return pitch_class_object_list

def get_pitchclass_object_list_by_pitchclass_name(pitch_class_name_list):
    pitch_class_object_list = get_pitchclass_list_by_pitchclass_name(pitch_class_name_list)
    numeric_list = []
    for i, pc in enumerate(pitch_class_object_list):
        numeric_list.append(pc.chromatic_index_base_c)
    return numeric_list

def compute_interval_list(numeric_list):
    return [y - x for x, y in zip(numeric_list[0:-1], numeric_list[1:])]


for scale_dict in [scale_Major, scale_minor]:
    scale_by_pitch_class_name = scale_dict['scale_base_c']['scale_by_name']
    numeric_list = get_pitchclass_object_list_by_pitchclass_name(scale_by_pitch_class_name)
    interval_list = compute_interval_list(numeric_list)

    print()
    print(interval_list)

print()


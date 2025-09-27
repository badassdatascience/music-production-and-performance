
#
# Need to test what happens with negative intervals
#
# Need to test or refactor regarding series involving
# more than one octave
#

#
# import the Django boilerplate code
#
import music_production_and_performance.django.django_boilerplate

#
# import the modules and scales we need
#
from theory_western.models import PitchClass, IntervalSeries
from music_production_and_performance.theory.western.scales.scales import *

#
# user settings
#
load_data = True

#
# converts a list of pitch classes (by name) to a list of the
# same pitch classes as a list of PitchClass objects
#
# I may move this into "models.py":
#
def get_pitchclass_object_list_by_pitchclass_name_list(pitch_class_list):
    pitch_class_object_list = []
    for pitch_name in pitch_class_list:
        pc = PitchClass.objects.get(name = pitch_name)
        pitch_class_object_list.append(pc)
    return pitch_class_object_list

#
# converts a list of pitch classes (by name) to a list of the
# same pitch classes as numbers
#
# might move this into one of the model definitions...
#
def get_pitchclass_numeric_list_by_pitchclass_name_list(pitch_class_name_list):
    pitch_class_object_list = get_pitchclass_object_list_by_pitchclass_name_list(pitch_class_name_list)
    numeric_list = []
    for i, pc in enumerate(pitch_class_object_list):
        numeric_list.append(pc.chromatic_index_base_c)
    return numeric_list

#
# a helper function for computing intevals
#
# I realize list comprehension is slow; if we
# come across a performance issue I'll move
# this calculation into NumPy:
#
# might move this into one of the model definitions
#
def compute_interval_list(numeric_list):
    return [y - x for x, y in zip(numeric_list[0:-1], numeric_list[1:])]

#
# load into database
#
if load_data:
    for scale_dict in [scale_Major, scale_minor]:
        scale_by_pitch_class_name = scale_dict['scale_base_c']['scale_by_name']
        numeric_list = get_pitchclass_numeric_list_by_pitchclass_name_list(scale_by_pitch_class_name)
        interval_list = compute_interval_list(numeric_list)

        series_name = scale_dict['name']
        interval_list_dict_for_json = interval_list
        
        interval_series = IntervalSeries(
            name = series_name,
            series = interval_list_dict_for_json,
        )
        interval_series.save()


#
# query to test it
#
for series_name in ['Major', 'minor']:
    interval_series = IntervalSeries.objects.get(name = series_name)
    print(series_name, interval_series.name, interval_series.series, interval_series.reconstruct())

    










#
# import the Django boilerplate code
#
import music_production_and_performance.django.django_boilerplate

from theory_western.models import PitchClass, IntervalSeries
from music_production_and_performance.theory.western.scales.scales import *

load_data = True



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

#
# load
#
if load_data:
    for scale_dict in [scale_Major, scale_minor]:
        scale_by_pitch_class_name = scale_dict['scale_base_c']['scale_by_name']
        numeric_list = get_pitchclass_object_list_by_pitchclass_name(scale_by_pitch_class_name)
        interval_list = compute_interval_list(numeric_list)
        
        series_name = scale_dict['name']
        interval_list_dict_for_json = interval_list
    
        interval_series = IntervalSeries(
            name = series_name,
            series = interval_list_dict_for_json,
        )
        interval_series.save()


#
# query
#
print()
for series_name in ['Major', 'minor']:
    interval_series = IntervalSeries.objects.get(name = series_name)
    print(series_name, interval_series.name, interval_series.series, interval_series.reconstruct())

print()
    

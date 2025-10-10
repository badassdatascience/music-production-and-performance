#
# import the Django boilerplate code
#
import music_production_and_performance.django.django_boilerplate

#
# import useful modules and scales
#
from theory_western.models import PitchClass
from music_production_and_performance.theory.western.scales.chromatic import chromatic_scale_pitch_class_names
from music_production_and_performance.theory.western.enharmonics import enharmonics_map

#
# initial load from a "pure"-ish chromatic scale
#
PitchClass.load_by_list_of_pitch_class_names(chromatic_scale_pitch_class_names)

#
# now add the enharmonic spellings
#
PitchClass.load_enharmonics(enharmonics_map)


    





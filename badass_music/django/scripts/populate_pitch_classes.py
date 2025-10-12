#
# import the Django boilerplate code
#
import badass_music.django.django_boilerplate

#
# import useful modules and scales
#
from theory_western.models import PitchClass
from badass_music.theory.western.scales.chromatic import chromatic_scale_pitch_class_names
from badass_music.theory.western.enharmonics import enharmonics_map

#
# initial load from a "pure"-ish chromatic scale
#
PitchClass.load_by_list_of_pitch_class_names(chromatic_scale_pitch_class_names)

#
# now add the enharmonic spellings
#
PitchClass.load_enharmonics(enharmonics_map)


    





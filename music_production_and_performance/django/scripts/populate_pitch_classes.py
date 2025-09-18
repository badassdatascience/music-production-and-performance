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


for i, pc_name in enumerate(chromatic_scale_pitch_class_names):

    # need to add a specific exception for uniqueness violation
    try:
        pc = PitchClass(
            name = pc_name.strip(),
            chromatic_index_base_c = i,
        )
        pc.save()
    except:
        pass

for name in enharmonics_map.keys():
    enharmonic_name = enharmonics_map[name]
    pc_base = PitchClass.objects.get(name = enharmonic_name)

    # need to add a specific exception for uniqueness violation
    try:
        pc = PitchClass(
            name = name.strip(),
            chromatic_index_base_c = pc_base.chromatic_index_base_c,
        )
        pc.save()
        pc.enharmonics.add(pc_base),
        pc.save()
    
        pc_base.enharmonics.add(pc)
        pc_base.save()
    except:
        pass

    





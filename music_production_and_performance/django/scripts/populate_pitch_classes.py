
import django
from django.conf import settings

settings.configure(
    DEBUG=True,
    INSTALLED_APPS=['theory_western.apps.TheoryWesternConfig'],
    DATABASES = {
        'default' : {
            'ENGINE' : 'django.db.backends.sqlite3',
            'NAME' : '/Users/emily/Desktop/projects/music-production-and-performance/music_production_and_performance/django/db.sqlite3',
        }
    }
)

django.setup()

from theory_western.models import PitchClass

chromatic_scale_pitch_class_names = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']

enharmonics_map = {
    'Cb' : 'B',
    'C#' : 'Db',
    'D#' : 'Eb',
    'E#' : 'F',
    'Fb' : 'E',
    'Gb' : 'F#',
    'G#' : 'Ab',
    'A#' : 'Bb',
    'B#' : 'C',
}


for i, pc_name in enumerate(chromatic_scale_pitch_class_names):

    try:
        pc = PitchClass(
            name = pc_name,
            chromatic_index_base_c = i,
        )
        pc.save()
    except:
        pass

for name in enharmonics_map.keys():
    enharmonic_name = enharmonics_map[name]
    pc_base = PitchClass.objects.get(name = enharmonic_name)

    try:
        pc = PitchClass(
            name = name,
            chromatic_index_base_c = pc_base.chromatic_index_base_c,
        )
        pc.save()
        pc.enharmonics.add(pc_base),
        pc.save()
    
        pc_base.enharmonics.add(pc)
        pc_base.save()
    except:
        pass

    





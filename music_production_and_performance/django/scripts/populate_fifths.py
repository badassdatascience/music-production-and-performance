
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
from theory_western.models import Fifths

from music_production_and_performance.theory.western.CircleOfFifths import CircleOfFifths

cf = CircleOfFifths()
n = len(cf.circle_of_fifths)


#                                                                                                              
# The enharmonic spellings don't quite make sense here                                                         
# because this used Camelot wheel pitch definitions.                                                           
#                                                                                                              
# We'll deal with that later:                                                                                  
#                                                                                                              
for i in range(0, n):
    pc_below = PitchClass.objects.get(name = cf.circle_of_fifths[(i - 1) % n])
    pc = PitchClass.objects.get(name = cf.circle_of_fifths[i % n])
    pc_above = PitchClass.objects.get(name = cf.circle_of_fifths[(i + 1) % n])

    #
    # We need a uniqueness constraint (not implemented yet)
    #
    fifths = Fifths(
        pitch_class_below = pc_below,
        pitch_class = pc,
        pitch_class_above = pc_above,
    )
    fifths.save()


    


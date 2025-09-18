#
# import the Django boilerplate code and configuration
#
import music_production_and_performance.django.django_boilerplate
from music_production_and_performance.config import config

#
# import useful modules
#
import pandas as pd
from theory_western.models import PitchClass
from theory_western.models import Fifths
from music_production_and_performance.theory.western.CircleOfFifths import CircleOfFifths

#
# calculate the circle of fifths
#
cf = CircleOfFifths()
n = len(cf.circle_of_fifths)

#
# create and store dataframe
#
df = pd.DataFrame({
    'pitch_class' : cf.circle_of_fifths,
    'pitch_class_numeric' : cf.circle_of_fifths_numeric,
})

df.to_csv(config['output_path'] + '/circle_of_fifths.csv', index = False)

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


    


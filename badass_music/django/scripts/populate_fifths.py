#
# import the Django boilerplate code and configuration
#
import badass_music.django.django_boilerplate
from badass_music.config import config

#
# import useful modules
#
import pandas as pd
from theory_western.models import Fifths
from badass_music.theory.western.CircleOfFifths import CircleOfFifths

#
# calculate the circle of fifths
#
cf = CircleOfFifths()

#
# Create and store a "circle_of_fifths" data frame for
# downstream usage:
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
Fifths.load_circle_of_fifths(cf)

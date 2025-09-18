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

#
# user settings
#
do_qc = False

#
# load the circle of fifths
#
df = pd.read_csv(config['output_path'] + '/circle_of_fifths.csv')

#
# define the minor Camelot key numbers
#
# It may be better to calculate these rather than
# define the lists. Maybe later.
#
camelot_minor_list = list(range(5, 13)); camelot_minor_list.extend(list(range(1, 5)))
camelot_major_list = list(range(8, 13)); camelot_major_list.extend(list(range(1, 8)))

#
# construct a data frame
#
df = pd.DataFrame(
    {
        'pitch_class' : list(df['pitch_class']),
        'pitch_class_numeric' : list(df['pitch_class_numeric']),
        'camelot_minor' : camelot_minor_list,
        'camelot_major' : camelot_major_list,
    }
)

#
# QC by the "eyeball" test
#
if do_qc:
    print()
    print(df)
    print()

#
# load into the relevent PitchClass
#
for i, row in df.iterrows():
    chromatic_index_base_c = row['pitch_class_numeric']
    pitch_classes = PitchClass.objects.filter(chromatic_index_base_c = chromatic_index_base_c)
    for pc in pitch_classes:
        pc.camelot_minor_number = row['camelot_minor']
        pc.camelot_major_number = row['camelot_major']
        pc.save()



    


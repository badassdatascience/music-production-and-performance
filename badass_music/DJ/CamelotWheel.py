# Copyright 2025, Emily Marie Williams

#
# import useful system libraries
#
import numpy as np
import pandas as pd
import re
import json

#
# import useful classes from this module
#
from badass_music.theory.western.CircleOfFifths import CircleOfFifths
from badass_music.theory.western.scales.chromatic import chromatic_scale_pitch_class_names

#
# define a class for computing and storing a Camelot wheel,
# a tool used by DJs to facilitate harmonic mixing invented
# by the good folks at Mixed In Key
#
class CamelotWheel():

    #
    # constructor
    #
    # Enables one to provide their own circle of fifths object
    #
    # The static "default" function below allows bypassing this
    # step to simply compute a version matching Mixed In Key's
    # Camelot wheel.
    #
    def __init__(
        self,
        circle_of_fifths : CircleOfFifths,
    ) -> None:
        self.cof = circle_of_fifths
        self.compute_minor_offset()
        self.compute_camelot_wheel()
        self.compute_camelot_dataframe()
        self.compute_json_string()

    #
    # given a pitch number element in a pitch class number array,
    # compute relative minor mode
    #
    def compute_minor_offset(self) -> None:
        minor_offset_fifths = []
        for pitch_class in self.cof.circle_of_fifths_numeric:
            minor_offset_fifths.append((pitch_class + 9) % 12)
        self.minor_offset_fifths_numeric = np.array(minor_offset_fifths, dtype = np.uint8)

    #
    # performs the "meat" of camelot wheel computation
    #
    def compute_camelot_wheel(self) -> None:

        #
        # Adds the major or minor indicator, "B" or "A" respectively
        #
        def get_camelot_symbols(symbol) -> np.array:
            return np.array([str(((q + 7) % 12) + 1) + symbol for q in range(0, 12)], dtype = str)

        camelot_minor = get_camelot_symbols('A')
        camelot_major = get_camelot_symbols('B')

        self.camelot_wheel_minor_layer = list(
            zip(self.cof.chromatic_scale_pitch_classes[self.minor_offset_fifths_numeric], camelot_minor)
        )
        self.camelot_wheel_major_layer = list(
            zip(self.cof.chromatic_scale_pitch_classes[self.cof.circle_of_fifths_numeric], camelot_major)
        )
        self.camelot_combined_minor_and_major = list(zip(self.camelot_wheel_minor_layer, self.camelot_wheel_major_layer))

    #
    # produces a dataframe summarizing the results
    #
    def compute_camelot_dataframe(self) -> None:
        df_minor = pd.DataFrame(self.camelot_wheel_minor_layer, columns = ['tonic_pitch_class_minor', 'camelot_minor'])
        df_major = pd.DataFrame(self.camelot_wheel_major_layer, columns = ['tonic_pitch_class_major', 'camelot_major'])

        for df_x, mode in zip([df_minor, df_major], ['minor', 'major']):
            df_x['camelot_tonic_number'] = np.uint8([re.findall(r'\d+', camelot_key) for camelot_key in df_x['camelot_' + mode]])

        self.df = (
            pd.merge(
                df_minor,
                df_major,
                on = ['camelot_tonic_number'],
                how = 'left',
            )
            [['camelot_tonic_number', 'tonic_pitch_class_minor', 'camelot_minor', 'tonic_pitch_class_major', 'camelot_major']]
            .sort_values(by = ['camelot_tonic_number'])
            .reset_index()
            .drop(columns = ['index'])
        )

    #
    # reports the dataframe with a friendly function name
    #
    # (I'll never actually use this in practice... consider it
    # legacy code from development).
    #
    def summary(self) -> pd.DataFrame:
        return self.df

    #
    # output JSON suitable for use with D3.js' "Sunburst" graphic
    #
    def compute_json_string(self) -> str:
        to_json_list = []
        for i, row in self.df.iterrows():
            to_json_list.append(
                {
                    'name' : row['camelot_minor'] + ' - ' + row['tonic_pitch_class_minor'] + ' Minor',
                    'children' : [
                        { 
                            'name' : row['camelot_major'] + ' - ' + row['tonic_pitch_class_major'] + ' Major',
                            'value' : 1,
                        }
                    ]
                }
            )

        to_json_full = {
            'name' : 'Camelot Wheel',
            'children' : to_json_list,
        }
        result = json.dumps(to_json_full)
        result = result.replace('"name"', 'name').replace('"children"', 'children').replace('"value"', 'value')
        self.json_string = result
    
    #
    # define a static function to generate the default Camelot wheel,
    # which should exactly match Mixed In Key's version
    #
    def compute_default_camelot_wheel() -> object:
        scale_enumeration_indices = np.arange(0, 12, dtype = np.uint8)
        cf = CircleOfFifths(
            chromatic_scale_pitch_classes = chromatic_scale_pitch_class_names,
            chromatic_scale_numeric = scale_enumeration_indices,
        )
        cw = CamelotWheel(cf)
        return cw

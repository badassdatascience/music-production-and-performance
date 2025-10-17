# Camelot Wheel Computation and Graphic Generation

The code contained in this directory computes Camelot wheels from a given CircleOfFifths object ("../../theory/western/CircleOfFifths.py") which in turn is calculated from a provided chromatic scale ("../../theory/western/scales/chromatic.py").

Given the following chromatic scale:
```
chromatic_scale_pitch_class_names = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
```
this code produces the following graphical output:

![Computed Camelot Wheel](CamelotWheel.png "Computed Camelot Wheel")

Data output, in the form of both a Pandas dataframe and a JSON object, is provided by the the Jupyter notebook "Camelot_Wheel.ipynb". The dataframe output supports downstream programmatic use of a computed Camelot wheel while the JSON object is pasted into the provided HTML file to produce the graphical display.

"Camelot_Wheel.ipynb" demonstrates how to use this module, from generating the prerequisite "CircleOfFifths" object to generating the dataframe and JSON results.

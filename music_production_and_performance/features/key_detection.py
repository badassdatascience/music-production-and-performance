
#
# import system libraries
#
import librosa
import numpy as np
import matplotlib.pyplot as plt

#
# import local libraries
#
from music_production_and_performance.theory.western.definitions import chromatic_scale_pitch_class_names   # we assume these are ordered correctly starting at C

#
# define a function to compute chromagrams
#
def compute_chromagram(y, sr, hop_length, function_to_use = librosa.feature.chroma_stft):
    return function_to_use(y=y, sr=sr, hop_length = hop_length) 

#
# define a function to display chromagrams
#
def display_chromagram(chromagram, track_title):
    fig, ax = plt.subplots(sharex=True, sharey=True, figsize = [12, 6])
    img = librosa.display.specshow(chromagram, y_axis='chroma', x_axis='time', ax=ax)
    ax.set(title='Chromagram:  ' + track_title)
    fig.colorbar(img, ax=ax)
    plt.show()
    plt.close()

#
# define a function to detect pitch class key from the chromagram
#
def detect_key_using_chromagram(
    chromagram,
    chroma_to_key = chromatic_scale_pitch_class_names,
):

    # Calculate the mean chroma feature across time
    mean_chroma = np.mean(chromagram, axis=1)

    # Find the key by selecting the maximum chroma feature
    estimated_key_index = np.argmax(mean_chroma)
    estimated_key = chroma_to_key[estimated_key_index]

    return estimated_key
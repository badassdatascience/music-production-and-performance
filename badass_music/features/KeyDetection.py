# Copyright 2025, Emily Marie Williams

#
# load useful libraries
#
import librosa
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pprint as pp
from scipy.stats import entropy
from scipy.stats import chisquare
from scipy.stats import kurtosis

from music_production_and_performance.features.Track import Track
from music_production_and_performance.theory.western.scales.chromatic import chromatic_scale_pitch_class_names

#
# Define class to facilitate key detection
#
class KeyDetection(Track):
    def __init__(
        self,
        track_to_analyze_filename : str,
        track_title : str,
        sampling_rate_for_import : int = 48000,
        hop_length : int = 1024
    ):
        super().__init__(track_to_analyze_filename, track_title, sampling_rate_for_import)
        
        self.hop_length = hop_length

        self.chromagram_method_list = []
        self.chromagram_method_name_list = []
        self.is_fit = False

        # the casting is not strictly necessary, but helps documentation of intent
        self.hop_length_in_seconds = float(hop_length) / float(sampling_rate_for_import)

    def fit(self):
        super().fit()
        self.separate_harmonics_and_percussives()
        self.compute_chromagrams()
        self.estimate_key()
        self.compute_uniformity_metrics()

        self.df = pd.merge(
            self.df_estimated_key,
            self.df_uniformity,
            on = ['track_title', 'track_to_analyze_filename', 'method', 'hop_length'],
            how = 'left',
        )

    def summary_full(self):
        self.plot_split_harmonics_and_percussives()
        self.display_chromagrams()
        self.plot_chromagram_boxplot()
        
    def summary_key_detection(self):
        self.display_key_estimates()
        self.plot_chromagram_boxplot()
    
    def separate_harmonics_and_percussives(self):
        self.y_harmonic, self.y_percussive = librosa.effects.hpss(self.y)

    def plot_split_harmonics_and_percussives(self):
        plt.figure(figsize = [25, 8])

        plt.subplot(2, 1, 1)
        plt.plot(self.y_harmonic)
        plt.title('Harmonics Waveform')
        plt.tight_layout()

        plt.subplot(2, 1, 2)
        plt.plot(self.y_percussive)
        plt.title('Percussives Waveform')
        plt.tight_layout()

        plt.show()
        plt.close()

    # Normalized energy for each chroma bin at each frame.
    # https://librosa.org/doc/main/generated/librosa.feature.chroma_stft.html
    #
    # Energy distribution of each pitch class across time:
    # 
    def compute_chromagrams(self):
        self.chromagram_stft = librosa.feature.chroma_stft(
            y = self.y_harmonic,
            sr = self.sampling_rate_for_import,
            hop_length = self.hop_length,
        )
        self.chromagram_method_list.append(self.chromagram_stft)
        self.chromagram_method_name_list.append('Short-Time Fourier Transform')

        #
        # a bit redundant... we can redesign this to use a loop
        # iterating through the chromagram-generation functions
        #
        self.chromagram_cqt = librosa.feature.chroma_cqt(
            y = self.y_harmonic,
            sr = self.sampling_rate_for_import,
            hop_length = self.hop_length,
        ) 
        self.chromagram_method_list.append(self.chromagram_cqt)
        self.chromagram_method_name_list.append('Constant-Q Transform')

        #
        # boxplot content prep et. al.
        #
        self.chromagram_values_list_per_method_per_note = {}
        for chrm, method in zip(self.chromagram_method_list, self.chromagram_method_name_list):
            self.chromagram_values_list_per_method_per_note[method] = []
            for note_index in np.arange(0, chrm.shape[0]):
                self.chromagram_values_list_per_method_per_note[method].append(chrm[note_index, :])     
        
    # Energy distribution of each pitch class across time
    def display_chromagrams(self):
        for chrm, method in zip(self.chromagram_method_list, self.chromagram_method_name_list):
            fig, ax = plt.subplots(sharex=True, sharey=True, figsize = [12, 6])
            img = librosa.display.specshow(chrm, y_axis = 'chroma', x_axis = 'time', ax = ax)
            ax.set(title='Chromagram: "' + self.track_title + '"\nMethod: "' + method + '"')
            fig.colorbar(img, ax=ax)
            plt.tight_layout()
            plt.show()
            plt.close()

    def plot_chromagram_boxplot(self):
        for method in self.chromagram_values_list_per_method_per_note.keys():
            plt.figure()
            plt.boxplot(self.chromagram_values_list_per_method_per_note[method], widths=0.85, showmeans=True, meanline=True)
            plt.xticks(np.arange(1, len(chromatic_scale_pitch_class_names) + 1), chromatic_scale_pitch_class_names)
            plt.title('Energy Distribution of Each Pitch Class Across Time\nMethod = "' + method + '"')
            plt.tight_layout()
            plt.show()
            plt.close()

    def estimate_key(self):
        key_estimate_list = []
        for chrm, method in zip(self.chromagram_method_list, self.chromagram_method_name_list):
            key_estimate_dict = {
                'track_title' : self.track_title,
                'track_to_analyze_filename' : self.track_to_analyze_filename,
                'method' : method,
                'hop_length' : self.hop_length,
                'hop_length_in_seconds' : self.hop_length_in_seconds,
            }
            
            key_as_chromatic_index = np.argmax(np.mean(chrm, axis = 1))
            key_estimate_dict['key_as_chromatic_index'] = key_as_chromatic_index
            key_estimate_dict['key_as_pitch_class'] = chromatic_scale_pitch_class_names[key_as_chromatic_index]
            key_estimate_list.append(key_estimate_dict)
        self.df_estimated_key = pd.DataFrame(key_estimate_list)

    def display_key_estimates(self):
        pp.pprint(self.df_estimated_key.to_dict(orient = 'records'))

    def compute_uniformity_metrics(self):
        uniformity_metrics_list = []
        for chrm, method in zip(self.chromagram_method_list, self.chromagram_method_name_list):
            
            uniformity_metrics = {
                'track_title' : self.track_title,
                'track_to_analyze_filename' : self.track_to_analyze_filename,
                'method' : method,
                'hop_length' : self.hop_length,
            }
            
            #self.uniformity_metrics[method] = {}
            probability_distribution = np.mean(chrm, axis = 1) / np.sum(np.mean(chrm, axis = 1))
            N = len(probability_distribution)
            uniform_distribution = np.array([1. / N] * N)

            # dissimilarity indices
            uniformity_metrics['dissimilarity_index'] = 0.5 * np.sum(np.abs(probability_distribution - uniform_distribution))
            
            # kurtosis
            uniformity_metrics['kurtosis'] = kurtosis(probability_distribution)

            # entropy
            uniformity_metrics['entropy'] = entropy(probability_distribution)
            
            uniformity_metrics_list.append(uniformity_metrics)
        
        self.df_uniformity = pd.DataFrame(uniformity_metrics_list)

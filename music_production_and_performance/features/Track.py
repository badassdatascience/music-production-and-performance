import librosa


class Track():
    def __init__(
        self,
        track_to_analyze_filename : str,
        track_title : str,
        sampling_rate_for_import : int = 48000,
    ):
        self.track_to_analyze_filename = track_to_analyze_filename
        self.track_title = track_title
        self.sampling_rate_for_import = sampling_rate_for_import
        
        self.is_fit = False

    def load_track_timeseries(self):
        #
        # we are using a single mono channel here for these analyses
        #
        self.y, self.sr = librosa.load(
            self.track_to_analyze_filename,
            sr = self.sampling_rate_for_import,
        )  

    def fit(self):
        self.is_fit = True
        self.load_track_timeseries()

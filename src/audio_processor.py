import librosa
from pydub import AudioSegment
import io


class AudioProcessor:
    @staticmethod
    def convert_to_wav(file_path):
        """Converts an MP3 file to WAV format if necessary."""
        audio = AudioSegment.from_file(file_path)
        buffer = io.BytesIO()
        audio.export(buffer, format="wav")
        buffer.seek(0)
        return buffer

    @staticmethod
    def extract_features(file_path):
        """Extracts audio features from the WAV file."""
        y, sr = librosa.load(file_path, sr=None)
        features = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        return features.tolist()

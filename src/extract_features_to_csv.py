import os
import csv
from pydub import AudioSegment
import librosa
import numpy as np

# Directory containing the audio files
audio_files_dir = '/Users/chanceneihouse/myuzo/Spotify Music/001_Database_Telaviv'
# CSV file path
csv_file_path = 'src/data/features.csv'

# Prepare to write to CSV
with open(csv_file_path, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write the header
    csv_writer.writerow(['track_id', 'feature1', 'feature2', 'feature3'])

    # Process each audio file
    for filename in os.listdir(audio_files_dir):
        if filename.lower().endswith('.mp3'):
            file_path = os.path.join(audio_files_dir, filename)
            # Convert MP3 to WAV using pydub
            try:
                audio = AudioSegment.from_mp3(file_path)
            except Exception as e:
                print(f'Error processing file {file_path}: {e}')
                continue
            wav_file_path = os.path.splitext(file_path)[0] + '.wav'
            audio.export(wav_file_path, format='wav')
            # Load WAV file using librosa
            y, sr = librosa.load(wav_file_path, sr=None)
            # Extract features (example: MFCCs, Chroma, Mel, Contrast, Tonnetz)
            # Here we just take the mean of the MFCCs as an example
            mfcc = librosa.feature.mfcc(y=y, sr=sr)
            feature1 = np.mean(mfcc[0])
            feature2 = np.mean(mfcc[1])
            feature3 = np.mean(mfcc[2])
            # Write the features to the CSV file
            csv_writer.writerow([filename, feature1, feature2, feature3])
            # Remove the WAV file to save space
            os.remove(wav_file_path)

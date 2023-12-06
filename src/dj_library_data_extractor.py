import os
import mutagen
from typing import List


class DJLibraryDataExtractor:
    def extract_data(self, library_path: str) -> List[dict]:
        # Implementation for extracting data from a DJ's music library
        track_data = []
        for root, dirs, files in os.walk(library_path):
            for file in files:
                if file.endswith((".mp3", ".flac")):
                    file_path = os.path.join(root, file)
                    audio = mutagen.File(file_path, easy=True)
                    track_data.append(
                        {
                            "id": os.path.splitext(file)[0],
                            "name": audio.get("title", [""])[0],
                            "artist": audio.get("artist", [""])[0],
                            "album": audio.get("album", [""])[0],
                            "genre": audio.get("genre", [""])[0],
                            "length": audio.info.length,
                        }
                    )
        return track_data

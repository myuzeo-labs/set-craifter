```python
import pandas as pd

class DJLibraryDataExtractor:
    def __init__(self, library_path):
        self.library_path = library_path

    def extract_data(self):
        try:
            track_data = pd.read_csv(self.library_path)
            return track_data
        except Exception as e:
            print(f"Error occurred while extracting data: {e}")
            return None
```
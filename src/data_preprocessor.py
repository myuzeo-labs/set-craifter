import pandas as pd
from typing import List, Dict


class DataPreprocessor:
    def process_data(self, raw_data: List[Dict[str, any]]) -> pd.DataFrame:
        # Convert raw data to a pandas DataFrame
        df = pd.DataFrame(raw_data)
        # Handle missing values by filling them with a placeholder
        df.fillna("Unknown", inplace=True)
        # Convert 'length' from seconds to minutes
        df["length"] = df["length"].apply(lambda x: round(x / 60, 2))
        # Normalize the 'length' column to a 0-1 range
        df["length"] = (df["length"] - df["length"].min()) / (
            df["length"].max() - df["length"].min()
        )
        return df

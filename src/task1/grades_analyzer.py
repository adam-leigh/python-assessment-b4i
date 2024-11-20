import pandas as pd

class Loader:
    def load_data(self, filepath: str) -> pd.DataFrame:
        return pd.read_csv(filepath)

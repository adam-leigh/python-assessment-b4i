import pandas as pd

class Loader:

    def __init__(self) -> None:
        self.loaders = {
                ".csv": pd.read_csv,
                ".json": pd.read_json,
                ".xlsx": pd.read_excel,
                }

    def load_data(self, filepath: str) -> pd.DataFrame:
        extension = filepath.split('.')[-1].lower() # splits the string into a list, indexing the last item in the list.
        if f".{extension}" in self.loaders:
            return self.loaders[f".{extension}"](filepath)
        raise ValueError(f"Unsupported file format: {extension}")


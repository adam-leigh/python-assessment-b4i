import pandas as pd

class Loader:
    def __init__(self):
        self.loaders = {
            ".csv": pd.read_csv,
            ".json": self._load_json,
            ".xlsx": pd.read_excel,
        }

    def load_data(self, file_path: str) -> pd.DataFrame:
        extension = file_path.split('.')[-1].lower()
        if f".{extension}" in self.loaders:
            return self.loaders[f".{extension}"](file_path)
        raise ValueError(f"Unsupported file format: {extension}")

    def _load_json(self, file_path: str) -> pd.DataFrame:
        import json

        with open(file_path, "r") as file:
            data = json.load(file)
            return pd.DataFrame(data["grades"])

class Analyzer:
    def __init__(self, data: pd.DataFrame) -> None:
        self.data = data

    def passing_rate(self, pass_mark=60):
        passing_students = self.data[self.data["grade"] >= pass_mark]
        percentage = (len(passing_students) / len(self.data)) * 100
        return round(percentage, 2)

if __name__ == "__main__":
    # df = Loader().load_data("./data/grades.json")
    # df = Loader().load_data("./data/grades.csv")
    # df = Loader().load_data("./data/grades.xlsx")
    # print(df.head())
    pass

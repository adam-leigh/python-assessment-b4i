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

import pandas as pd


class Analyzer:
    def __init__(self, data: pd.DataFrame) -> None:
        """Initialize the Analyzer with student data."""
        self.data = data

    def _validate_data(self):
        """Ensure the DataFrame has the required columns."""
        required_columns = {'student_id', 'subject', 'grade'}
        if not required_columns.issubset(self.data.columns):
            raise ValueError("DataFrame must contain 'student_id', 'subject', and 'grade' columns")

    def _get_passing_students(self, pass_mark=60):
        """Get students with grades >= pass mark."""
        return self.data[self.data["grade"] >= pass_mark]

    def overall_statistics(self, pass_mark=60) -> dict:
        """Calculate overall statistics across all subjects."""
        passing_students = self._get_passing_students(pass_mark)
        return {
            "highest_grade": self.data["grade"].max(),
            "lowest_grade": self.data["grade"].min(),
            "average_grade": round(self.data["grade"].mean(), 2),
            "students_passed": len(passing_students),
            "passing_rate": round((len(passing_students) / len(self.data)) * 100, 2),
        }

    def per_student_statistics(self) -> pd.DataFrame:
        """Calculate average, highest, and lowest grades per student."""
        return self.data.groupby("student_id").agg(
            average_grade=("grade", "mean"),
            highest_grade=("grade", "max"),
            lowest_grade=("grade", "min")
        ).round(2).reset_index()

    def per_subject_statistics(self) -> pd.DataFrame:
        """Calculate average, highest, and lowest grades per subject."""
        return self.data.groupby("subject").agg(
            average_grade=("grade", "mean"),
            highest_grade=("grade", "max"),
            lowest_grade=("grade", "min")
        ).round(2).reset_index()

    def sort_by_column(self, column_name: str, ascending=True):
        """Sort the DataFrame by a specific column."""
        if column_name not in self.data.columns:
            raise ValueError(f"Column {column_name} does not exist.")
        return self.data.sort_values(by=column_name, ascending=ascending)


if __name__ == "__main__":
    df = Loader().load_data("./data/grades.json")
    # df = Loader().load_data("./data/grades.csv")
    # df = Loader().load_data("./data/grades.xlsx")
    analyzer = Analyzer(df)
    stats = analyzer.overall_statistics()
    print("\n📊\n")
    print("Analysis:")
    print(f"- {stats['students_passed']} out of {len(df)} students passed.")
    print(f"- The lowest score was {stats['lowest_grade']}.")
    print(f"- The highest score was {stats['highest_grade']}.")
    print(f"- The average score was {stats['average_grade']}.")
    print(f"- The pass rate of this group of students is {stats['passing_rate']}%")
    # print("DataFrame sorted by grade:")
    # print(analyzer.sort_by_column("grade"))


import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from task1.grades_analyzer import Analyzer, Loader


class Visualizer:
    def __init__(self, data):
        """Initialize the visualizer with any DataFrame."""
        self.data = data

    def plot(self, x_column, y_column, title, xlabel=None, ylabel=None, rotation=45):
        """
        Plot a bar chart from the DataFrame.
        """
        if x_column not in self.data.columns or y_column not in self.data.columns:
            raise ValueError(f"DataFrame must contain '{x_column}' and '{y_column}' columns")

        plt.figure(figsize=(10, 6))
        plt.bar(self.data[x_column], self.data[y_column], color="skyblue")
        plt.title(title)
        plt.xlabel(xlabel if xlabel else x_column)
        plt.ylabel(ylabel if ylabel else y_column)
        plt.xticks(rotation=rotation)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":

    df = Loader().load_data("./data/grades.xlsx")
    analyzer = Analyzer(df)
    student_stats = analyzer.per_student_statistics()

    print(student_stats)

    visualizer = Visualizer(student_stats)

    visualizer.plot(
        x_column="student_id",        
        y_column="average_grade",    
        title="Average Grade Per Student",
        xlabel="Student ID",        
        ylabel="Average Grade"     
    )

    subject_stats = analyzer.per_subject_statistics()
    print(subject_stats)

    visualizer = Visualizer(subject_stats)

    visualizer.plot(
        x_column="subject",
        y_column="average_grade",
        title="Average Grade Per Subject",
        xlabel="Subject",
        ylabel="Average Grade"
)

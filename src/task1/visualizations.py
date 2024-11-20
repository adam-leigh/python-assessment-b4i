import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from task1.grades_analyzer import Loader

class Visualizer:
    def __init__(self, data: pd.DataFrame):
        """Initialize the visualizer with student data."""
        self._validate_data(data)
        self.data = data

    def plot_grades(self):
        """Plot a grouped bar chart for grades by subject."""
        pivot_data = self._pivot_data()
        x_positions = self._calculate_x_positions(pivot_data)
        self._create_grouped_bar_chart(pivot_data, x_positions)
        self._add_labels_and_legend(pivot_data.index, pivot_data.columns)
        self._show_plot()

    def _validate_data(self, data):
        """Check if the data has the right columns."""
        required_columns = {'student_id', 'subject', 'grade'}
        if not required_columns.issubset(data.columns):
            raise ValueError("DataFrame must contain 'student_id', 'subject', and 'grade' columns")

    def _pivot_data(self):
        """Pivot the data so each student ID has grades for all subjects."""
        return self.data.pivot(index="student_id", columns="subject", values="grade")

    def _calculate_x_positions(self, pivot_data):
        """Figure out where to place each bar for students."""
        num_students = len(pivot_data.index)
        return np.arange(num_students)

    def _create_grouped_bar_chart(self, pivot_data, x_positions):
        """Draw the grouped bar chart for all grades."""
        bar_width = 0.2
        subjects = pivot_data.columns
        offsets = np.arange(len(subjects)) * bar_width - (len(subjects) - 1) * bar_width / 2

        for i, subject in enumerate(subjects):
            plt.bar(
                x_positions + offsets[i],
                pivot_data[subject],
                width=bar_width,
                label=subject,
            )

    def _add_labels_and_legend(self, student_ids, subjects):
        """Add labels, ticks, and the legend to the plot."""
        plt.title("Student Grades by Subject")
        plt.xlabel("Student ID")
        plt.ylabel("Grade")
        plt.xticks(ticks=range(len(student_ids)), labels=student_ids, rotation=45)
        plt.legend(title="Subject")

    def _show_plot(self):
        """Render the plot and tighten the layout."""
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":

    df = Loader().load_data("./data/grades.xlsx")
    print(len(df))
    visualizations = Visualizer(df)
    visualizations.plot_grades()

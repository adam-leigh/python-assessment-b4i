import pytest
import pandas as pd
from task1.visualizations import Visualizer

@pytest.fixture
def sample_data():
    """Fixture to provide dummy DataFrame for testing."""
    return pd.DataFrame([
        {"student_id": 1001, "subject": "Math", "grade": 85},
        {"student_id": 1003, "subject": "Biology", "grade": 85},
        {"student_id": 1001, "subject": "Biology", "grade": 88},
        {"student_id": 1002, "subject": "Math", "grade": 92},
        {"student_id": 1004, "subject": "Physics", "grade": 67},
    ])

@pytest.fixture
def student_stats():
    return pd.DataFrame([
        {"student_id": 1001, "average_grade": 85.25, "highest_grade": 90, "lowest_grade": 78},
        {"student_id": 1002, "average_grade": 89.00, "highest_grade": 92, "lowest_grade": 85},
        {"student_id": 1003, "average_grade": 82.75, "highest_grade": 92, "lowest_grade": 76},
    ])
    
def test_visualizer_with_student_statistics(student_stats):
    visualizer = Visualizer(student_stats)
    try:
        visualizer.plot(
            x_column="student_id",
            y_column="average_grade",
            title="Test Student Stats Plot",
            xlabel="Student ID",
            ylabel="Average Grade"
        )
    except Exception as e:
        pytest.fail(f"Plot generation failed with error: {e}")


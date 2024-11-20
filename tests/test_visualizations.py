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
    
def test_visualizer_generates_bar_chart(sample_data):
    visualizer = Visualizer(sample_data)
    try:
        visualizer.plot_grades()
    except Exception as e:
        pytest.fail(e)

import pytest
import pandas as pd

@pytest.fixture
def csv_file():
    return "data/grades.csv"

@pytest.fixture
def json_file():
    return "data/grades.json"

@pytest.fixture
def excel_file():
    return "data/grades.xlsx"


# Grades Loader
from task1.grades_analyzer import Loader

def test_loader_can_load_csv(csv_file):
    loader = Loader()
    data = loader.load_data(csv_file)
    assert isinstance(data, pd.DataFrame)
    assert list(data.columns) == ["student_id", "subject", "grade"]

def test_loader_can_load_json(json_file):
    loader = Loader()
    data = loader.load_data(json_file)
    assert isinstance(data, pd.DataFrame)
    assert list(data.columns) == ["student_id", "subject", "grade"]

def test_loader_can_load_excel(excel_file):
    loader = Loader()
    data = loader.load_data(excel_file)
    assert isinstance(data, pd.DataFrame)
    assert list(data.columns) == ["student_id", "subject", "grade"]

# Grades Analyzer
from task1.grades_analyzer import Analyzer

""" Sample data I extracted from the dataframe:
[{
    'student_id': 1001,
    'subject': 'Math',
    'grade': 85
}, {
    'student_id': 1003,
    'subject': 'Biology',
    'grade': 85
}, {
    'student_id': 1001,
    'subject': 'Biology',
    'grade': 88
}, {
    'student_id': 1002,
    'subject': 'Math',
    'grade': 92
}, {
    'student_id': 1004,
    'subject': 'Physics',
    'grade': 67
}]
"""

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

def test_analyzer_can_sort_dataframe(sample_data):
    analyzer = Analyzer(sample_data)
    sorted_df = analyzer.sort_by_column("grade")
    assert sorted_df.iloc[0]["grade"] == 67 # Lowest grade in our sample data
    assert sorted_df.iloc[-1]["grade"] == 92

def test_analyzer_calculates_statistics(sample_data):
    analyzer = Analyzer(sample_data)
    stats = analyzer.overall_statistics()
    expected_average = sum([85, 85, 88, 92, 67]) / 5 # I manually wrote this out based on our sample data.
    assert stats["highest_grade"] == 92
    assert stats["lowest_grade"] == 67
    assert stats["average_grade"] == round(expected_average, 2)
    assert stats["students_passed"] == 5 # All students passed in our sample
    assert stats["passing_rate"] == 100

import pytest
import pandas as pd
from task1.grades_analyzer import Loader

@pytest.fixture
def csv_file():
    return "data/grades.csv"

def test_loader_can_load_csv(csv_file):
    loader = Loader()
    data = loader.load_data(csv_file)
    assert isinstance(data, pd.DataFrame)
    assert list(data.columns) == ["student_id", "subject", "grade"]

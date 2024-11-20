import pytest
import pandas as pd
from task1.grades_analyzer import Loader

@pytest.fixture
def csv_file():
    return "data/grades.csv"

@pytest.fixture
def json_file():
    return "data/grades.json"

@pytest.fixture
def excel_file():
    return "data/grades.xlsx"

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


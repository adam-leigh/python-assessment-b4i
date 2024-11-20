import pytest
from src.task2.number_game import NumberGuessingGame

@pytest.fixture
def game():
    """Creates an instance of the NumberGuessingGame object for testing."""
    return NumberGuessingGame()

def test_init(game):
    """Verified that game is instantiated and not a Nonetype."""
    assert game is not None

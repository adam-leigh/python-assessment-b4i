import pytest
from src.task2.number_game import NumberGuessingGame
from typing import Any

@pytest.fixture
def game():
    """Creates an instance of the NumberGuessingGame object for testing."""
    return NumberGuessingGame(difficulty="easy")

def test_init(game):
    """Verified that game is instantiated and not a Nonetype."""
    assert game is not None

def test_instantiation_with_difficulty_parameter():
    VALID_OPTIONS: list[str] = ["easy", "medium", "hard"]

    for difficulty in VALID_OPTIONS:
        game = NumberGuessingGame(difficulty=difficulty)
        assert game.difficulty == difficulty

    INVALID_OPTIONS: list[Any] = ["very easy", 123, None, "", [], {}, True]

    for invalid in INVALID_OPTIONS:
        with pytest.raises(ValueError):
            NumberGuessingGame(difficulty=invalid)

def test_make_guess(game):
    game.make_guess(42)
    assert game.user_guess == 42

def test_difficulty_getter_and_setter():
    game = NumberGuessingGame(difficulty="easy")
    assert game.difficulty == "easy"

    game.difficulty = "medium" # Here's where we're testing our setter
    assert game.difficulty == "medium"

    with pytest.raises(ValueError):
        game.difficulty = "sadkljhsfksjh"


def test_guess_getter_and_setter():
    game = NumberGuessingGame(difficulty="easy")
    game.user_guess = 50 # Testing the setter here.
    assert game.user_guess == 50 # Testing the getter.

    with pytest.raises(ValueError):
        game.user_guess = "Not a number."

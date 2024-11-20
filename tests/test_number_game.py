import pytest
from src.task2.number_game import NumberGuessingGame
from typing import Any

@pytest.fixture
def easy_game():
    return NumberGuessingGame(difficulty="easy")

@pytest.fixture
def medium_game():
    return NumberGuessingGame(difficulty="medium")

@pytest.fixture
def hard_game():
    return NumberGuessingGame(difficulty="hard")

# def test_game_configuration_easy(easy_game):
#     assert easy_game.difficulty == "easy"
#     assert easy_game.remaining_tries == 25
#     assert 1 <= easy_game.target_number <= 50
#
# def test_game_configuration_medium(medium_game):
#     assert medium_game.difficulty == "medium"
#     assert medium_game.remaining_tries == 15
#     assert 1 <= medium_game.target_number <= 100
#
# def test_game_configuration_hard(hard_game):
#     assert hard_game.difficulty == "hard"
#     assert hard_game.remaining_tries == 10
#     assert 1 <= hard_game.target_number <= 200

def test_game_rules_based_on_difficulty():
    CONFIG = {
        "easy": {"number_pool": (1, 50), "max_tries": 25},
        "medium": {"number_pool": (1, 100), "max_tries": 15},
        "hard": {"number_pool": (1, 200), "max_tries": 10},
    }

    for difficulty, rules in CONFIG.items():
        game = NumberGuessingGame(difficulty=difficulty)
        assert game.number_pool == rules["number_pool"]

def test_init(easy_game):
    """Verified that game is instantiated and not a Nonetype."""
    assert easy_game is not None

def test_instantiation_with_difficulty_parameter():
    VALID_OPTIONS: list[str] = ["easy", "medium", "hard"]

    for difficulty in VALID_OPTIONS:
        game = NumberGuessingGame(difficulty=difficulty)
        assert game.difficulty == difficulty

    INVALID_OPTIONS: list[Any] = ["extreme", 123, None, "", [], {}, True]

    for invalid in INVALID_OPTIONS:
        with pytest.raises(ValueError):
            NumberGuessingGame(difficulty=invalid)

def test_make_guess(easy_game):
    easy_game.make_guess(42)
    assert easy_game.user_guess == 42

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

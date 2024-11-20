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


# def test_game_rules_based_on_difficulty():
#     CONFIG = {
#         "easy": {"number_pool": (1, 50), "max_tries": 25},
#         "medium": {"number_pool": (1, 100), "max_tries": 15},
#         "hard": {"number_pool": (1, 200), "max_tries": 10},
#     }
#
#     for difficulty, rules in CONFIG.items():
#         game = NumberGuessingGame(difficulty=difficulty)
#         assert game.game_config.number_pool == rules["number_pool"]
#         assert game.game_config.max_tries == rules["max_tries"]

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

def test_difficulty_getter_and_setter():
    game = NumberGuessingGame(difficulty="easy")
    assert game.difficulty == "easy"

    game.difficulty = "medium" # Here's where we're testing our setter
    assert game.difficulty == "medium"

    with pytest.raises(ValueError):
        game.difficulty = "sadkljhsfksjh"


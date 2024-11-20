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

# Make Guess Tests

def test_make_guess_higher(easy_game, monkeypatch):
    """Tests that the make_guess method will return 'Higher' when the guess is less than the target number."""
    monkeypatch.setattr(easy_game.game_config, "target_number", 30) # Here we're saying our random number is 30.
    assert easy_game.make_guess(20) == "Higher"

def test_make_guess_lower(easy_game, monkeypatch):
    """Testing for whether the make_guess method returns 'Lower' if the number is greater than the target number."""
    monkeypatch.setattr(easy_game.game_config, "target_number", 30)
    assert easy_game.make_guess(40) == "Lower"

def test_make_guess_correct(easy_game, monkeypatch):
    """Tests that make_guess returns 'Correct!' if the submitted number matches the target."""
    monkeypatch.setattr(easy_game.game_config, "target_number", 30)
    assert easy_game.make_guess(30) == "Correct!"

def test_decrement_tries(easy_game, monkeypatch):
    """Tests that make_guess successfully decrements the number of attempts."""
    monkeypatch.setattr(easy_game.game_config, "target_number", 30)
    initial_tries = easy_game.game_config.max_tries
    easy_game.make_guess(15)
    assert easy_game.game_config.max_tries == initial_tries - 1
    
def test_game_over_triggered(easy_game, monkeypatch):
    """Tests that game over is triggered when all tries are exhausted."""
    monkeypatch.setattr(easy_game.game_config, "target_number", 30)
    easy_game.game_config.max_tries = 1
    with pytest.raises(RuntimeError, match="Game Over!"):
        easy_game.make_guess(20)

def test_guess_out_of_range(easy_game):
    """Tests that a guess outside the number pool raises a ValueError."""
    # I've configured easy_mode to include numbers between 1 and 50.
    with pytest.raises(ValueError, match="Guess must be between 1 and 50."):
        easy_game.make_guess(60)

    with pytest.raises(ValueError, match="Guess must be between 1 and 50."):
        easy_game.make_guess(0) # Should not include zero.

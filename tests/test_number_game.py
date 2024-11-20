import pytest
from src.task2.number_game import NumberGuessingGame, InvalidGuessError, GameOverError
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
    """Verify that game is instantiated and not a Nonetype."""
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

    game.difficulty = "medium"  # Testing the setter
    assert game.difficulty == "medium"

    with pytest.raises(ValueError):
        game.difficulty = "invalid_difficulty"


# Make Guess Tests

def test_make_guess_higher(easy_game, monkeypatch):
    """Test that make_guess returns 'Higher' when the guess is less than the target number."""
    monkeypatch.setattr(easy_game, "_target_number", 30)
    assert easy_game.make_guess(20) == "Higher"


def test_make_guess_lower(easy_game, monkeypatch):
    """Test that make_guess returns 'Lower' when the guess is greater than the target number."""
    monkeypatch.setattr(easy_game, "_target_number", 30)
    assert easy_game.make_guess(40) == "Lower"


def test_make_guess_correct(easy_game, monkeypatch):
    """Test that make_guess returns 'Correct!' when the guess matches the target number."""
    monkeypatch.setattr(easy_game, "_target_number", 30)
    assert easy_game.make_guess(30) == "Correct!"


def test_decrement_tries(easy_game, monkeypatch):
    """Test that make_guess successfully decrements the number of attempts."""
    monkeypatch.setattr(easy_game, "_target_number", 30)
    initial_tries = easy_game.remaining_tries
    easy_game.make_guess(15)
    assert easy_game.remaining_tries == initial_tries - 1


def test_game_over_triggered(easy_game, monkeypatch):
    """Test that game over is triggered when all tries are exhausted."""
    monkeypatch.setattr(easy_game, "_target_number", 30)
    easy_game._remaining_tries = 1
    with pytest.raises(GameOverError, match="Game Over!"):
        easy_game.make_guess(20)


def test_guess_out_of_range(easy_game):
    """Test that a guess outside the number pool raises an InvalidGuessError."""
    # Easy mode includes numbers between 1 and 50.
    with pytest.raises(InvalidGuessError, match="Guess must be between 1 and 50."):
        easy_game.make_guess(60)

    with pytest.raises(InvalidGuessError, match="Guess must be between 1 and 50."):
        easy_game.make_guess(0)  # Should not include zero.


def test_invalid_guess_type(easy_game):
    """Test that a non-integer guess raises an InvalidGuessError."""
    with pytest.raises(InvalidGuessError, match="Guess must be an integer."):
        easy_game.make_guess("twenty")


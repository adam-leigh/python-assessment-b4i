from dataclasses import dataclass
import random
from typing import Tuple

@dataclass
class GameConfig:
    difficulty: str
    number_pool: Tuple[int, int]
    max_tries: int
    target_number: int = None # initialized once our game class is instantiated.

class NumberGuessingGame:

    _CONFIG = {
            "easy": {
                "number_pool": (1, 50), 
                "max_tries": 25
                },
            "medium": {
                "number_pool": (1, 100), 
                "max_tries": 15
                },
            "hard": {
                "number_pool": (1, 200), 
                "max_tries": 100
                },
            }

    def __init__(self, difficulty: str) -> None:
        self.difficulty = difficulty
        self.game_config = self._setup_game_rules()
        
    @property
    def difficulty(self) -> str:
        return self._difficulty

    @difficulty.setter
    def difficulty(self, value: str):
        if not isinstance(value, str) or value not in ["easy", "medium", "hard"]:
            raise ValueError("Difficulty must be 'easy', 'medium' or 'hard'.")
        self._difficulty = value
    

    def _setup_game_rules(self) -> GameConfig:
        """Configures the game settings / rules based on the difficulty selected."""
        rules = self._CONFIG[self._difficulty]
        return GameConfig(
                difficulty=self.difficulty,
                number_pool=rules["number_pool"],
                max_tries=rules["max_tries"],
                target_number=self._generate_target_number(rules["number_pool"]),
                )

    def _generate_target_number(self, number_pool: Tuple[int, int]) -> int:
        """Generates a random number within the pool range."""
        start, end = number_pool
        return random.randint(start, end)

    def make_guess(self, number: int) -> str:
        """
        Receives a number from the user, compares it with the target number,
        decrements the number of tries, and provides hints or triggers game-over.
        """
        if not isinstance(number, int):
            raise ValueError("Guess must be an integer.")

        if number < self.game_config.number_pool[0] or number > self.game_config.number_pool[1]:
            raise ValueError(
                f"Guess must be between {self.game_config.number_pool[0]} and {self.game_config.number_pool[1]}."
            )

        if self.game_config.max_tries <= 0:
            raise RuntimeError("Game Over!")

        self.game_config.max_tries -= 1

        if self.game_config.max_tries == 0 and number != self.game_config.target_number:
            raise RuntimeError("Game Over!")

        if number == self.game_config.target_number:
            return "Correct!"
        elif number < self.game_config.target_number:
            return "Higher"
        else:
            return "Lower"


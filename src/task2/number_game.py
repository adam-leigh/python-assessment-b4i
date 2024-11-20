import random

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
        self._difficulty = str()
        self._user_guess = int()
        self._number_pool = None
        self._max_tries = None
        self.difficulty = difficulty
        self._setup_game_rules()
        
    @property
    def difficulty(self) -> str:
        return self._difficulty

    @difficulty.setter
    def difficulty(self, value: str):
        if not isinstance(value, str) or value not in ["easy", "medium", "hard"]:
            raise ValueError("Difficulty must be 'easy', 'medium' or 'hard'.")
        self._difficulty = value
    
    @property
    def user_guess(self) -> int:
        return self._user_guess

    @user_guess.setter
    def user_guess(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("Guess must be an integer.")
        self._user_guess = value

    @property
    def number_pool(self) -> tuple:
        return self._number_pool

    def max_tries(self) -> int:
        return self._max_tries

    def _setup_game_rules(self):
        """Configures the game settings / rules based on the difficulty selected."""
        rules = self._CONFIG[self._difficulty]
        self._number_pool = rules["number_pool"]
        self._max_tries = rules["max_tries"]

    def make_guess(self, number: int):
        """
        Receives a number from the user and stores it in the user_guess attribute.
        """
        self.user_guess = number

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
        self.difficulty = difficulty
        
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

    def make_guess(self, number: int):
        """
        Receives a number from the user and stores it in the user_guess attribute.
        """
        self.user_guess = number

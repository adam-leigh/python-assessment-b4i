
class NumberGuessingGame:

    def __init__(self, difficulty: str) -> None:
        if not isinstance(difficulty, str) or difficulty not in ["easy", "medium", "hard"]:
            raise ValueError("Difficulty must be 'easy', 'medium' or 'hard'.")
        self.difficulty = difficulty
        self.user_guess = None
    
    def make_guess(self, number: int) -> None:
        if not isinstance(number, int):
            raise ValueError("Guess must be an integer.")
        self.user_guess = number

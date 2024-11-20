
class NumberGuessingGame:

    def __init__(self, difficulty: str) -> None:
        if not isinstance(difficulty, str) or difficulty not in ["easy", "medium", "hard"]:
            raise ValueError("Difficulty must be 'easy', 'medium' or 'hard'.")
        self.difficulty = difficulty

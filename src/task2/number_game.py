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
                "max_tries": 10
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

def get_valid_difficulty() -> str:
    while True:
        difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
        if difficulty in ["easy", "medium", "hard"]:
            return difficulty
        else:
            print("Invalid difficulty. Please choose 'easy', 'medium', or 'hard'.")

if __name__ == "__main__":

    def play_game():
        difficulty: str = get_valid_difficulty()
        game = NumberGuessingGame(difficulty=difficulty)
        print(f"Game started! Guess a number between {game.game_config.number_pool[0]} and {game.game_config.number_pool[1]}.")
        print(f"You have {game.game_config.max_tries} attempts.")

        while True:
            try:
                guess_input = input("Enter your guess: ")
                guess = int(guess_input)
                hint = game.make_guess(guess)
                print(hint)
                print(f"Remaining attempts: {game.game_config.max_tries}")  # Display remaining tries

                if hint.startswith("Correct"):
                    print(f"Congratulations! You won the game with {game.game_config.max_tries} attempts remaining.")
                    break

            except ValueError as ve:
                print(f"Invalid input: {ve}")
            except RuntimeError as re:
                print(re)
                print(f"The correct number was {game.game_config.target_number}.")
                break

    while True:
        play_game()
        replay = input("Do you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thank you for playing! Goodbye.")
            break


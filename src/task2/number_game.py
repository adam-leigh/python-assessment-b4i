from dataclasses import dataclass
import random
from typing import Tuple

class InvalidGuessError(Exception):
    """Exception raised for invalid guesses."""
    pass

class GameOverError(Exception):
    """Exception raised when the game is over."""
    pass

@dataclass(frozen=True)
class GameConfig:
    difficulty: str
    number_pool: Tuple[int, int]
    max_tries: int

class GameConfigFactory:
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

    @classmethod
    def create_config(cls, difficulty: str) -> GameConfig:
        if difficulty not in cls._CONFIG:
            raise ValueError("Difficulty must be 'easy', 'medium' or 'hard'.")
        config = cls._CONFIG[difficulty]
        return GameConfig(
                difficulty=difficulty,
                number_pool=config["number_pool"],
                max_tries=config["max_tries"]
                )


class NumberGuessingGame:
    def __init__(
            self, 
            difficulty: str, 
            config_factory: GameConfigFactory = GameConfigFactory
            ) -> None:
        self._difficulty = None
        self.difficulty = difficulty
        self._config_factory = config_factory
        self.game_config = self._setup_game_rules()
        self._target_number = self._generate_target_number()
        self._remaining_tries = self.game_config.max_tries
        
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
        return self._config_factory.create_config(self._difficulty)

    def _generate_target_number(self) -> int:
        """Generates a random number within the pool range."""
        start, end = self.game_config.number_pool
        return random.randint(start, end)

    def make_guess(self, number: int) -> str:
        """
        Receives a number from the user, compares it with the target number,
        decrements the number of tries, and provides hints or triggers game-over.
        """
        if not isinstance(number, int):
            raise InvalidGuessError("Guess must be an integer.")

        if number < self.game_config.number_pool[0] or number > self.game_config.number_pool[1]:
            raise InvalidGuessError(
                f"Guess must be between {self.game_config.number_pool[0]} and {self.game_config.number_pool[1]}."
            )

        if self.game_config.max_tries <= 0:
            raise GameOverError("Game Over!")

        self._remaining_tries -= 1

        if self._remaining_tries == 0 and number != self._target_number:
            raise GameOverError("Game Over!")

        if number == self._target_number:
            return "Correct!"
        elif number < self._target_number:
            return "Higher"
        else:
            return "Lower"

    @property
    def remaining_tries(self) -> int:
        return self._remaining_tries

    @property
    def target_number(self) -> int | None:
        """Expose the target_number for testing purposes."""
        return self._target_number


def get_valid_difficulty() -> str:
    while True:
        difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
        if difficulty in ["easy", "medium", "hard"]:
            return difficulty
        else:
            print("Invalid difficulty. Please choose 'easy', 'medium', or 'hard'.")


def play_game():
    difficulty = get_valid_difficulty()
    game = NumberGuessingGame(difficulty=difficulty)
    print(f"Game started! Guess a number between {game.game_config.number_pool[0]} and {game.game_config.number_pool[1]}.")
    print(f"You have {game.remaining_tries} attempts.")

    while True:
        try:
            guess_input = input("Enter your guess: ")
            guess = int(guess_input)
            hint = game.make_guess(guess)
            print(hint)
            print(f"Remaining attempts: {game.remaining_tries}")

            if hint.startswith("Correct"):
                print(f"Congratulations! 🎉 You won the game with {game.game_config.max_tries} attempts remaining.")
                break

        except InvalidGuessError as e:
            print(f"Invalid input: {e}")
        except GameOverError as e:
            print(e)
            print(f"The correct number was {game.target_number}.")
            break


if __name__ == "__main__":
    while True:
        play_game()
        replay = input("Do you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thank you for playing 👾 Goodbye.")
            break


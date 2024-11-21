# The Python Assessment for B4i

## Overview

This project serves as a test of my abilities with the Python programming language. The assessment consists of two tasks:

1. **Data Analysis Project**
    
    This task involves analyzing a sample CSV file containing a list of grades for five students across separate subjects. The specifics of this task include:
    
    - Loading the CSV file (and optionally other file types containing the same data).
    - Calculating the average grade per student.
    - Identifying the highest and lowest grade per student.
    - Determining the number of passing students per subject.

2. **Number Guessing Game**
    
    This second task involves creating a number guessing game with different difficulty levels. The game requirements include:
    
    - Allowing guesses from a predefined pool of numbers based on the selected difficulty.
    - Displaying hints after each guess, indicating whether the next guess should be higher or lower.

## Setup Instructions

This project uses Poetry for dependency management, but a `requirements.txt` is also provided for convenience.

## Quick Start with Poetry (Recommended)

1. Install Poetry:

```bash
# Windows (PowerShell)
(Invoke-WebRequest -Uri <https://install.python-poetry.org> -UseBasicParsing).Content | python -

# macOS/Linux
curl -sSL <https://install.python-poetry.org> | python3
```

1. Clone and set up:

```bash
git clone <https://github.com/yourusername/yourrepository.git>
cd yourrepository
poetry install
poetry shell
```

## Alternative Setup with pip

If you prefer using traditional virtual environments:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
```

Note: The `requirements.txt` was generated using:

```bash
poetry export -f requirements.txt --without-hashes > requirements.txt

```

## Usage Examples
### File Structure

The project is organized as follows:

```
.

├── README.md

├── data

│   ├── grades.csv

│   ├── grades.json

│   └── grades.xlsx

├── poetry.lock

├── pyproject.toml

├── requirements.txt

├── src

│   ├── task1

│   │   ├── __init__.py

│   │   ├── grades_analyzer.py

│   │   └── visualizations.py

│   ├── task2

│   │   ├── __init__.py

│   │   └── number_game.py

│   └── task3

│       ├── __init__.py

│       └── palindrome.py

└── tests

├── test_grades_analyzer.py

├── test_number_game.py

├── test_palindrome.py

└── test_visualizations.py
```

### Running the Project

Each task can be executed directly using the `if __name__ == "__main__"` block in their respective files.

#### Task 1: Grades Analysis

Run the `grades_analyzer.py` or `visualizations.py` scripts to analyze grades or visualize the data:

```bash

python3 src/task1/grades_analyzer.py

python3 src/task1/visualizations.py

python3 src/task2/number_game.py

python3 src/task3/palindrome.py "Racecar"

```


## Design Decisions

### Task 1: Data Analysis Project

For Task 1, I decided to break the project into three Python classes:

1. **Loader Class**
    
    This class dynamically loads the grades data from the directory, whether it's in CSV, JSON, or Excel format. It returns a Pandas DataFrame in all cases. I chose Pandas because, in my opinion, it’s the best library for handling large datasets and performing statistical analysis quickly and easily.
    
2. **Analyzer Class**
    
    This class requires a Pandas DataFrame when you create an instance. You can either pass it a DataFrame directly or use the output from the Loader class. This design makes it flexible and lets the Analyzer immediately provide the statistical analysis we want based on the data.
    
3. **Visualizer Class**
    
    The Visualizer class also takes a Pandas DataFrame when it’s instantiated. Since many of the Analyzer methods return DataFrames, it’s easy to pass those directly into the Visualizer. As long as the DataFrame has the expected columns, the Visualizer works seamlessly, and we can add more functionality to it over time.
    

This setup keeps the project modular:

- The Loader handles loading the data.
- The Analyzer handles the calculations.
- The Visualizer handles how the data is presented.

This structure makes the code more flexible and easier to extend in the future.

### Task 2: Number Guessing Game

For the number guessing game, I did my best to structure the code in a way that allows for future development and makes the project easier to build upon. This was especially important during the final stages when I refactored the code.

Because the game depends on the selected difficulty level, and because you might want to modify what “easy,” “medium,” or “hard” means in terms of game settings, I created an immutable dataclass for `GameConfig`. This ensures that once the game rules are set, they can’t be changed during runtime.

To handle the setup for `GameConfig`, I nested everything required into `GameConfigFactory`. This was my best attempt at implementing the factory design pattern. My aim was to prioritize the separation of concerns principle by untangling the game settings from the `NumberGuessingGame` itself.

Additionally, the `play_game` function is a standalone function and not part of the game class. This was intentional, as I wanted to keep the logic for running the game separate from the game settings and configuration.

To improve the readability of the code and make errors more specific to the game, I also created two custom exceptions:

- `InvalidGuessError` for handling invalid guesses.
- `GameOverError` for when the player runs out of attempts.

Overall, the design ensures that the game is modular, flexible, and easy to maintain or expand in the future.

## Known Limitations
### Task 1: Data Analysis Project

1. **Loader Object**
    
    The loader is currently limited to working only if the file contains the following columns: `student ID`, `subject`, and `grade`. If these columns are missing, the loader will fail.
    
2. **Analyzer Object**
    
    The analyzer could be improved by separating the individual statistics calculations (e.g., highest grade, lowest grade, average grade, passing students, and passing rate) into their own methods. This would enhance the separation of concerns and make the code easier to maintain and extend.
    
3. **Visualizer Object**
    
    The visualizer is designed to work almost exclusively with the output of two specific methods from the analyzer. This restricts its usability and flexibility, making it less dynamic and less adaptable for broader use cases.
    

### Task 2: Number Guessing Game

1. **Leaderboard Feature**
    
    The leaderboard feature was planned but never implemented due to time constraints.
    
2. **Terminal-Based Design**
    
    The game currently runs in the terminal, and its design is not future-proof. Significant refactoring would be required to adapt it for a front-end interface, such as a web-based application.
    

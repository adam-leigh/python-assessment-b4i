# README.md - B4i Python Assessment

## **Background**
This project serves as a test of my abilities with the Python programming language. The assessment, provided by the team at the B4I Project, consists of two tasks designed to evaluate my technical skills and coding abilities.

## **Requirements**

### **Task 1: Grades Data Analysis**

**Must-Haves**:

•	A Python script must load a CSV file named grades.csv containing three columns: student ID, subject, and grade.

•	The script must calculate the following:

•	Average grade per student.

•	Highest and lowest grade per subject.

•	Number of passing students per subject.

•	Results must be sortable by criteria such as average grade or subject.

•	Exception handling must cover:

•	Missing or nonexistent files.

•	Invalid file formats.

**Nice-to-Haves**:

•	Support for additional input formats, such as JSON and Excel.

•	Data visualization using Matplotlib or a similar library.

•	Unit tests for key functions.

•	Handling variations in schemas for JSON or Excel files.

### **Task 2: Number Guessing Game**

**Must-Haves**:

•	A class-based implementation of a number guessing game.

•	The game must support three difficulty levels:

•	**Easy**: Numbers range from 1 to 50.

•	**Medium**: Numbers range from 1 to 100.

•	**Hard**: Numbers range from 1 to 200.

•	A randomly generated target number must be created for the chosen difficulty.

•	The range of numbers is determined dynamically based on the selected difficulty.

•	The game must run in a loop, allowing the user to make guesses, and provide feedback to the console after each guess:

•	“Higher” if the guess is too low.

•	“Lower” if the guess is too high.

•	A variable to track the number of attempts used.

•	A maximum number of attempts per difficulty level.

•	As difficulty increases, the maximum number of guesses decreases.

•	The game must end when the user either guesses correctly or runs out of attempts.

•	A scoring system that evaluates performance based on the number of guesses used, and prints the score to the console upon successful completion.

**Nice-to-Haves**:

•	A leaderboard feature that persists between game sessions to store and display high scores.

•	Additional game modes (specific modes not yet defined).

•	Comprehensive error handling using try-except blocks or unit tests.

## **Method**

### **Task 1: Grades Data Analysis**

**Overview**:
The implementation for Task 1 will focus on loading and processing grades data using a class-based approach where appropriate, while leveraging standalone functions for specific calculations or visualizations. The architecture aligns with the single responsibility principle, ensuring clear separation of data loading, processing, and visualization.

**Key Components**:

1.	**Tests**:

•	The development process will start with writing unit tests in a file named testGradeAnalyzer.py, located in the tests folder.

•	The tests will validate the functionality of the DataLoader and DataVisualizer classes and the standalone functions responsible for calculations.

2.	**Classes**:

•	**DataLoader Class**:

•	Responsible for loading data from files located in the data folder.

•	Accepts the file path as input to its constructor.

•	Validates the file format using the endswith method to ensure only CSV, JSON, or Excel files are processed.

•	Rejects improper file types with an appropriate error message.

•	Loads the valid file into a Pandas DataFrame for further processing.

•	Handles missing or invalid files through exception handling.

•	**DataVisualizer Class**:

•	Accepts a Pandas DataFrame as input to its constructor.

•	Provides methods to visualize the statistics calculated by other components (e.g., average grades, highest and lowest grades per subject).

•	Leverages Matplotlib for creating graphs or charts if visualization is required.

3.	**Functions**:

•	**calculate_statistics(data: pd.DataFrame)**:

•	Computes the required metrics:

•	Average grade per student.

•	Highest and lowest grade for each subject.

•	Number of passing students per subject.

•	Returns these metrics as a dictionary or a DataFrame for further use.

•	**sort_results(data: pd.DataFrame, criteria: str)**:

•	Sorts the processed data based on user-specified criteria (e.g., average grade or subject).

•	Additional utility functions may include format validation or data cleaning.

**Libraries Used**:

•	**Pandas** for loading and manipulating tabular data.

•	**Matplotlib** for optional data visualization.

•	**Pytest** for unit testing.

**Flow**:

1.	DataLoader reads and validates the file, outputting a Pandas DataFrame.

2.	The DataFrame is passed to standalone functions like calculate_statistics for analysis.

3.	Results are optionally passed to DataVisualizer for graphical representation.

### **Task 2: Number Guessing Game**

**Overview**:

I’m less sure of how exactly I’m going to tackle task 2, so I’ll begin with writing tests for the core NumberGuessingGame class and build upon it from there. If I get a chance to refactor the project, I may design NumberGuessingGame as a dataclass and incorporate pydantic into the project. The class will encapsulate the core game logic, as well as the validating and rejecting invalid user input. I will start with tests that reject invalid input when initializing our class, accepting only the strings “easy”, “medium” or “hard”.

The game will be implemented as a CLI program, allowing players to input guesses through the terminal.

class PalindromeChecker:
    """Class to check if a given string is a palindrome."""

    def palindrome_checker(self, input_string: str) -> bool:
        """Expects a string as input, then evaluates whether or not that string is a palindrome."""
        if not (isinstance(input_string, str) and input_string.isalpha()):
            raise ValueError("Input must be a string containing only alphabetic characters")
        uniform_string: str = input_string.lower()
        return uniform_string == uniform_string[::-1]

if __name__ == "__main__":
    pass

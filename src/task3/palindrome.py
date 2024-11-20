def palindrome_checker(string: str) -> bool:
    """Expects a string as input, then evaluates whether or not that string is a palindrome."""
    uniform_string: str = string.lower()
    return uniform_string == uniform_string[::-1]

if __name__ == "__main__":
    pass

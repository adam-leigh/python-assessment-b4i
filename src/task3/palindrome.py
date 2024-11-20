import argparse

def palindrome_checker(input_string: str) -> bool:
    """Expects a string as input, then evaluates whether or not that string is a palindrome."""
    if not (isinstance(input_string, str) and input_string.isalpha()):
        raise ValueError("Input must be a string containing only alphabetic characters")
    uniform_string: str = input_string.lower()
    return uniform_string == uniform_string[::-1]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check if a given string is a palindrome.")
    parser.add_argument("input_string", type=str, help="The string to check for palindrome property.")
    args = parser.parse_args()
    
    try:
        is_palindrome = palindrome_checker(args.input_string)
        print(f"'{args.input_string}' is a palindrome: {is_palindrome}")
    except ValueError as e:
        print(f"Error: {e}")

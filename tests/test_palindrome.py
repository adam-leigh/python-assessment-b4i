import pytest
from task3 import palindrome
from task3.palindrome import PalindromeChecker


@pytest.fixture
def palindrome_checker():
    """Fixture to instantiate PalindromeChecker."""
    return PalindromeChecker()


def test_palindrome_checker_with_palindrome(palindrome_checker):
    """Test that palindrome_checker returns True for palindrome strings."""
    PALINDROMES = ["radar", "civic", "racecar", "dad", "madam", "stats", "Civic"]
    for word in PALINDROMES:
        assert palindrome_checker.is_palindrome(word)


def test_palindrome_checker_returns_false_for_non_palindromes(palindrome_checker):
    """Test that palindrome_checker returns True for palindrome strings."""
    NON_PALINDROMES = ["Sarah", "Homecell", "Adam", "Thembani"]
    for word in NON_PALINDROMES:
        assert not palindrome_checker.is_palindrome(word) # Essentially saying 'assert that these all return False'


def test_palindrome_checker_with_uppercase_palindrome(palindrome_checker):
    """Test that PalindromeChecker.is_palindrome accounts for uppercase strings."""
    assert palindrome_checker.is_palindrome("Racecar")
    assert palindrome_checker.is_palindrome("Civic")


def test_palindrome_checker_invalid_input_types(palindrome_checker):
    """Test that palindrome_checker raises ValueError for invalid input types."""
    invalid_inputs = [626, 123.321, None, "626"]
    for val in invalid_inputs:
        with pytest.raises(ValueError, match="Input must be a string containing only alphabetic characters"):
            palindrome_checker.is_palindrome(val)


def test_palindrome_checker_empty_string(palindrome_checker):
    """Test that palindrome_checker raises ValueError for empty strings."""
    with pytest.raises(ValueError, match="Input must contain only alphabetic characters"):
        palindrome_checker.is_palindrome("")

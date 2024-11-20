import pytest
from task3.palindrome import palindrome_checker

def test_palindrome_checker_returns_true_for_radar():
    """Test that the function returns True for a palindrome string."""
    result: bool = palindrome_checker("radar")
    assert result

def test_palindrome_checker_returns_true_for_valid_palindromes():
    """Test that the function returns True for a palindrome string."""
    result: bool = palindrome_checker("civic")
    assert result

    result: bool = palindrome_checker("racecar")
    assert result

    result: bool = palindrome_checker("dad")
    assert result

    result: bool = palindrome_checker("madam")
    assert result

    result: bool = palindrome_checker("stats")
    assert result

def test_palindrome_checker_accounts_for_uppercase_palindromes():
    """Test that the function returns True for uppercase palindrome strings."""
    result: bool = palindrome_checker("Civic")
    assert result

def test_palindrome_checker_raises_exception_if_argument_is_not_string():
    """Test that an exception is raised if the input is not a string."""
    with pytest.raises(TypeError, match="Input must be a string"):
            palindrome_checker(626)

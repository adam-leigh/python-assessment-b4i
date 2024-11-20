from task3.palindrome import palindrome_checker

def test_palindrome_returns_true_for_radar():
    """ We're expecting the output of this function to return true if a string such as radar is passed into it. """
    result: bool = palindrome_checker("radar")
    assert result == True

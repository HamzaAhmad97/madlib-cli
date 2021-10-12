from madlib_cli import __version__
import pytest
from madlib import read_template, parse_template, merge, wrtie_response


def test_version():
    assert __version__ == "0.1.0"


def test_read_template_returns_stripped_string():
    """
    This is a testing function to test if the read_template function returns a file content given its path 

    Parameters
    ---------
    This function does not have any parameters

    Exceptions
    ----------
    AssertionError
        If the content retreived from the read_template function does not match the expected value

    Returns
    -------
    This function does not return anything
    """
    actual = read_template("assets/dark_and_stormy_night_template.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected


# @pytest.mark.skip("pending")
def test_parse_template():
    """
    This is a testing function to test if the parse_template function a tuple of strings and a string contining empty curly brackets

    Parameters
    ---------
    This function does not have any parameters

    Exceptions
    ----------
    AssertionError
        If the returned tuple of strings does not match the expected one
        If the returned string does not match the expected one
        
    Returns
    -------
    This function does not return anything
    """
    actual_stripped, actual_parts = parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


# @pytest.mark.skip("pending")
def test_merge():
    """
    This is a testing function to test if the merge function returns the correct string, where the passed strings in the tuple should replace all the empty curly brackets in the passed string

    Parameters
    ---------
    This function does not have any parameters

    Exceptions
    ----------
    AssertionError
        If the returned value form merge does not match the expected string
        
    Returns
    -------
    This function does not return anything
    """
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected


#@pytest.mark.skip("pending")
def test_read_template_raises_exception_with_bad_path():
    """
    This is a testing function to test if the read_template function raises an exception given an invalid file path

    Parameters
    ---------
    This function does not have any parameters
 
    Returns
    -------
    This function does not return anything
    """

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)


def test_write_response_writes_result_to_response_file():
    """
    This is a testing function to test if the write_resonse function writes the content to a file given its path

    Parameters
    ---------
    This function does not have any parameters
        
    Returns
    -------
    This function does not return anything
    """
    wrtie_response("It was a dark and stormy night.","assets/dummy_story.txt" )
    with open("assets/dummy_story.txt") as f:
        actual = f.read()
    expected = "It was a dark and stormy night."
    print(actual)
    assert actual == expected

def test_parse_template_returns_None_if_no_curly_brackets():
    """
    This is a testing function to test if the parse_template function returns None instead of a tuple if there are no wrapping curly brackets in the string

    Parameters
    ---------
    This function does not have any parameters

    Exceptions
    ----------
    AssertionError
        If the returned parts is not equal to None
        
    Returns
    -------
    This function does not return anything
    """
    actual_stripped, actual_parts = parse_template(
        "It was a and."
    )
    expected_stripped = "It was a and."
    expected_parts = None

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts

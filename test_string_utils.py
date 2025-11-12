import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("12 ноября 2025", "12 ноября 2025"),
    ("123", "123"),


])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),


])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.fixture
def utils():
    return StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_string, symbol, expected_output", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("hello world", "o", "hell wrld"),
    ("12345", "3", "1245"),
    ("pineapple cake", "p", "ineale cake"),
    ("11 ноября 2025", "я", "11 нобр 2025"),
    ("hello world", "!", "hello world"),
    (" Skypro", " ", "Skypro")


])
def test_delete_symbol_positive(utils, input_string, symbol, expected_output):
    result = utils.delete_symbol(input_string, symbol)
    assert result == expected_output


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   Skypro", "Skypro"),
    ("  hello world", "hello world"),
    ("  123", "123")



])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("Skypro", "Skypro"),
    ("hello world", "hello world"),
    ("123", "123")



])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_string, symbol, expected_output", [
    ("SkyPro", "k", True),
    ("hello world", "o", True),
    ("12345", "3", True),
    ("pineapple cake", "p", True),
    ("11 ноября 2025", "я", True),
    ("", "", True)



])
def test_contains_positive(utils, input_string, symbol, expected_output):
    result = utils.contains(input_string, symbol)
    assert result == expected_output


@pytest.mark.negative
@pytest.mark.parametrize("input_string, symbol, expected_output", [
    ("SkyPro", "f", False),
    ("hello world", "t", False),
    ("12345", "7", False),
    ("pineapple cake", "z", False),
    ("11 ноября 2025", "!", False),
    ("", "x", False)



])
def test_contains_negativ(utils, input_string, symbol, expected_output):
    result = utils.contains(input_string, symbol)
    assert result == expected_output

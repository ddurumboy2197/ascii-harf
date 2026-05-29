# test_ascii.py
import pytest
from ascii import ascii_to_char

def test_ascii_to_char():
    assert ascii_to_char(65) == 'A'
    assert ascii_to_char(97) == 'a'
    assert ascii_to_char(48) == '0'
    assert ascii_to_char(32) == ' '

def test_ascii_to_char_invalid():
    with pytest.raises(ValueError):
        ascii_to_char(100)

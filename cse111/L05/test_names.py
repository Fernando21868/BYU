import pytest
from names import make_full_name, extract_family_name, extract_given_name


def test_make_full_name():
    """Verify that the make_full_name function works correctly.
    Parameters: none
    Return: nothing
    """

    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("Fernando", "Arias") == "Arias; Fernando"


def test_extract_family_name():
    """Verify that the extract_family_name function works correctly.
    Parameters: none
    Return: nothing
    """

    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Arias; Fernando") == "Arias"


def test_extract_given_name():
    """Verify that the extract_given_name function works correctly.
    Parameters: none
    Return: nothing
    """

    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Arias; Fernando") == "Fernando"


pytest.main(["-v", "--tb=line", "-rN", __file__])

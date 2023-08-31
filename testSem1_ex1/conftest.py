import pytest

@pytest.fixture()
def correct_word():
    return 'молоко'

@pytest.fixture()
def incorrect_word():
    return 'малако'
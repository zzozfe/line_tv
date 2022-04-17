import pytest
from line_test import is_valid
from utils import get_test_data


filename = "test_data.json"
test_data = get_test_data(filename)

@pytest.mark.parametrize("data, expected", test_data)
def test_is_valid(data, expected):
    assert is_valid(data) == expected
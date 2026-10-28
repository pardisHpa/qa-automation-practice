import pytest

from src.rfm import CASES, segment


@pytest.mark.parametrize("recency, frequency, expected", CASES)
def test_segment(recency, frequency, expected):
    assert segment(recency, frequency) == expected


@pytest.mark.parametrize("recency, frequency", [(-1, 3), (10, -2)])
def test_negative_values_raise_error(recency, frequency):
    with pytest.raises(ValueError):
        segment(recency, frequency)

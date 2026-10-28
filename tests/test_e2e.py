import pytest

from src.rfm import CASES


@pytest.mark.parametrize("recency, frequency, expected", CASES)
def test_page_shows_segment(segment_page, recency, frequency, expected):
    segment_page.check(recency, frequency)
    assert segment_page.result_text() == f"Segment: {expected}"


@pytest.mark.parametrize("recency, frequency", [("abc", "3"), ("10", ""), ("-5", "2"), ("1.5", "2")])
def test_invalid_input_shows_error(segment_page, recency, frequency):
    segment_page.check(recency, frequency)
    assert "whole numbers" in segment_page.error_text()
    assert segment_page.result_text() == ""


def test_error_is_cleared_after_valid_input(segment_page):
    segment_page.check("abc", "3")
    segment_page.check(10, 8)
    assert segment_page.error_text() == ""
    assert segment_page.result_text() == "Segment: Champion"

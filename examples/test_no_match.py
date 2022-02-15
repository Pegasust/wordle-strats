import pytest
from wordle_env import no_match, _match_color


def green_test_set():
    return {}

def test_match_color():
    assert _match_color("blush", "blush") == [2]*5
    assert _match_color("beily", "belly") == [2, 2, 0, 2, 2]
    assert _match_color("beliy", "belly") == [2, 2, 2, 0, 2]
    assert _match_color("belly", "beily") == [2, 2, 0, 2, 2]
    assert _match_color("belly", "beliy") == [2, 2, 2, 0, 2]
    assert _match_color("belly", "beiiy") == [2, 2, 0, 0, 2]
    assert _match_color("blely", "belly") == [2, 1, 1, 2, 2]
    assert _match_color("blyle", "belly") == [2, 1, 1, 2, 1]
    assert _match_color("blyel", "belly") == [2, 1, 1, 1, 1]
    assert _match_color("ylleb", "belly") == [1, 1, 2, 1, 1]


def green_test():
    pass

if __name__ == "__main__":
    print("hello world")
    test_match_color()
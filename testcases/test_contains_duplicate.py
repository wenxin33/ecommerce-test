
import pytest


def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ([], False),
    ([0], False),
    ([0, 0], True),
    ([-1, -2, -3, -1], True),
    ([1, 2, 3, 4, 5], False),
])

def test_contains_duplicate(nums, expected):
    assert contains_duplicate(nums) == expected


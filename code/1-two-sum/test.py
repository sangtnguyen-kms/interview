from main import two_sum


def test_two_sum():
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3, 4, 5], 9, [3, 4]),
        ([1, 2, 3, 4, 5], 7, [1, 3]),
        ([1, 2, 3, 4, 5], 10, [4, 0]),
        ([1, 2, 3, 4, 5], 11, [4, 2]),
        ([1, 2, 3, 4, 5], 6, [1, 2]),
        ([1, 2, 3, 4, 5], 1, None),
        ([], 5, None),
    ]

    for i, (nums, target, expected) in enumerate(test_cases):
        result = two_sum(nums, target)
        assert (
            result == expected
        ), f"Test case {i+1} failed: Expected\
            {expected}, got {result}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_two_sum()

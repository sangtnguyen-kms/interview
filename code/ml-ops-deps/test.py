from main import findTaskOrder


def test_findTaskOrder():
    test_cases = [
        (3, [[1, 0], [2, 1]], [0, 1, 2]),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 1, 2, 3]),
        (3, [], [0, 1, 2]),
        (3, [[0, 1], [1, 2], [2, 0]], []),
        (
            6,
            [[1, 0], [2, 1], [3, 2], [4, 1], [5, 3], [5, 4]],
            [0, 1, 2, 4, 3, 5],
        ),
    ]

    for i, (numTasks, prerequisites, expected) in enumerate(test_cases):
        result = findTaskOrder(numTasks, prerequisites)
        assert (
            result == expected
        ), f"Test case {i+1} failed: Expected {expected}, got {result}"

    print("All test cases passed!")


# Run the test function
test_findTaskOrder()

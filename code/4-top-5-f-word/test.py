from main import topKFrequent


def test_topKFrequent():
    test_cases = [
        (["i", "love", "kms", "i", "love", "coding"], 2, ["i", "love"]),
        (
            [
                "the",
                "day",
                "is",
                "sunny",
                "the",
                "the",
                "the",
                "sunny",
                "is",
                "is",
            ],
            4,
            ["the", "is", "sunny", "day"],
        ),
    ]

    for i, (words, k, expected) in enumerate(test_cases):
        result = topKFrequent(words, k)
        assert (
            result == expected
        ), f"Test case {i+1} failed:\
            Expected {expected}, got {result}"

    print("All test cases passed!")


# Run the test function
test_topKFrequent()

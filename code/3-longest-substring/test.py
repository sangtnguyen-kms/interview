from main import lengthOfLongestSubstring


def test_lengthOfLongestSubstring():
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("aab", 2),
        ("dvdf", 3),
        (" ", 1),
        ("abba", 2),
        ("a", 1),
        ("", 0),
        ("abcdefghijklmnopqrstuvwxyz", 26),
    ]

    for i, (s, expected) in enumerate(test_cases):
        result = lengthOfLongestSubstring(s)
        assert (
            result == expected
        ), f"Test case {i+1} failed: \
            Expected {expected}, got {result}"

    print("All test cases passed!")


# Run the test function
test_lengthOfLongestSubstring()

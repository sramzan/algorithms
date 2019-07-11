# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcbabcbb"
        #   012345678
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#   Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


def get_longest_substring(someStr: str) -> int:
    longest = 0
    currentSubstrLength = 0
    currentStart = 0
    charDict = {}

    for index, char in enumerate(someStr):
        for currentIndex in range(currentStart, len(someStr)):
            if charDict.get(someStr[currentIndex]) == 1:
                longest = max(longest, currentSubstrLength)
                currentSubstrLength = 0
                currentStart = (index - currentStart) - 1
                charDict = {}
                print('new start', someStr[currentStart])

            charDict[someStr[currentIndex]] = 1
            currentSubstrLength += 1

    return max(longest, currentSubstrLength)


# print(get_longest_substring("abcabcbb"))
# print(get_longest_substring("bbbbb"))
# print(get_longest_substring(" "))
print(get_longest_substring("xzaxog"))
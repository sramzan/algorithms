'''
Problem:
    Given an array of integers, return indices of the two numbers such that
        they add up to a specific target.
    You may assume that each input would have exactly one solution, and you
        may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

Source: https://leetcode.com/problems/two-sum/
'''


def two_sum(nums, target):
    """
    :type nums: List[int`]
    :type target: int
    :rtype: List[int]
    """
    if not isinstance(nums, list) or len(nums) < 2:
        return -1

    val_index_map = {}

    for index, num in enumerate(nums):
        diff = target - num
        if diff in val_index_map:
            # Match found
            return [val_index_map.get(diff), index]

        val_index_map[num] = index

    # No match found
    return []

# Runtime: Worst: O(n) Avg: O(n/2) => O(n), Space: O(n)

# Call to enumerate does not duplicate the list, it returns an object
# which you use to iterate over. O(1) initialization, 0(1) return next el
# O(n) returning all elements
# To make this more efficient, you could keep the current index of the arr
# in mind. But, I felt the readability using enumerate is better


print('Test Cases: ')
print('1', two_sum([-1, 2], 1))
print('2:', two_sum([-2, 7], 5))
print('3:', two_sum([], 5))
print('4:', two_sum([2, 3, 6, -1, -9, 100], 99))
print('5:', two_sum([2, 3, 6, -1, -9, 100], -10))

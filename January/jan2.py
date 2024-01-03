"""2610. Convert an Array Into a 2D Array With Conditions"""
from typing import List

"""
You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

    The 2D array should contain only the elements of the array nums.
    Each row in the 2D array contains distinct integers.
    The number of rows in the 2D array should be minimal.

Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.
"""


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count_nums = {}
        ans = []

        for num in nums:
            if num not in count_nums:
                count_nums[num] = 0

            idx = count_nums[num]

            if idx == len(ans):
                ans.append([])

            ans[idx].append(num)

            count_nums[num] += 1

        return ans

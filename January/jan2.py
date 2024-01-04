"""2610. Convert an Array Into a 2D Array With Conditions"""
from typing import List

"""
You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

    The 2D array should contain only the elements of the array nums.
    Each row in the 2D array contains distinct integers.
    The number of rows in the 2D array should be minimal.

Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.

Example 1:

Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]
Explanation: We can create a 2D array that contains the following rows:
- 1,3,4,2
- 1,3
- 1
All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
It can be shown that we cannot have less than 3 rows in a valid array.


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

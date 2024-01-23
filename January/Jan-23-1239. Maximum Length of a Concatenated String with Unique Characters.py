"""
1239. Maximum Length of a Concatenated String with Unique Characters

You are given an array of strings arr. A string s is formed by the concatenation of a
 subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by
deleting some or no elements without changing the order of the remaining elements.



Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.


"""


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)

        def backtrack(i, curr, ans):
            if i == n:
                return ans
            nxt = set(curr)
            for c in arr[i]:
                if c in nxt:
                    return backtrack(i + 1, curr, ans)
                else:
                    nxt.add(c)

            return max(backtrack(i + 1, curr, ans), backtrack(i + 1, nxt, ans + len(arr[i])))

        return backtrack(0, set(), 0)
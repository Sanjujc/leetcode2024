
"""
1026. Maximum Difference Between Node and Ancestor
Given the root of a binary tree, find the maximum value v for which there exist different
 nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        return self.diff_val(root, root.val, root.val)

    def diff_val(self, root, max_val, min_val):
        print(max_val)
        if not root:
            return max_val - min_val
        min_val = min(min_val, root.val)
        max_val = max(max_val, root.val)
        left_node = self.diff_val(root.left, max_val, min_val)
        right_node = self.diff_val(root.right, max_val, min_val)
        return max(left_node, right_node)
"""
2385. Amount of Time for Binary Tree to Be Infected

You are given the root of a binary tree with unique values, and an integer start.
 At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

    The node is currently uninfected.
    The node is adjacent to an infected node.

Return the number of minutes needed for the entire tree to be infected.
Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        res = 0

        def dfs(node, res=None):
            if not node:
                return (0, False)

            l_res, l_found = dfs(node.left)
            r_res, r_found = dfs(node.right)

            if node.val == start:
                nonlocal res
                res = max(res, l_res, r_res)
                return (1, True)

            if l_res == 0 and r_res == 0:
                return (1, False)

            if l_found or r_found:
                res = max(res, l_res + r_res)

            if l_found:
                return (l_res + 1, True)

            if r_found:
                return (r_res + 1, True)

            return (max(l_res, r_res) + 1, False)

        dfs(root)

        return res
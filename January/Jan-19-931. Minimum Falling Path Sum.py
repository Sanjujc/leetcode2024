"""
931. Minimum Falling Path Sum

Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element
 in the next row that is either directly below or diagonally left/right.
  Specifically, the next element from position
(row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
"""

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        for r in range(n):
            for c in range(m):
                if r>0 and 0<=c-1 and c+1<m:
                    matrix[r][c]=min(matrix[r][c]+matrix[r-1][c],matrix[r][c]+matrix[r-1][c+1],matrix[r][c]+matrix[r-1][c-1])
                elif r>0 and c-1==-1:
                    matrix[r][c]=min(matrix[r][c]+matrix[r-1][c],matrix[r][c]+matrix[r-1][c+1])
                elif r>0 and c+1==m:
                    matrix[r][c]=min(matrix[r][c]+matrix[r-1][c],matrix[r][c]+matrix[r-1][c-1])

        return min(matrix[n-1])
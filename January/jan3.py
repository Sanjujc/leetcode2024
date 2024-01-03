from typing import List

"""2125. Number of Laser Beams in a Bank"""

"""Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, while'1' means the cell has a security device.

There is one laser beam between any two security devices if both conditions are met:

    The two devices are located on two different rows: r1 and r2, where r1 < r2.
    For each row i where r1 < i < r2, there are no security devices in the ith row.

Laser beams are independent, i.e., one beam does not interfere nor join with another.

Return the total number of laser beams in the bank."""


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        row, col = len(bank), len(bank[0])
        current, previous = 0, 0
        final_ans = 0
        for r in range(row):
            current = 0
            for c in range(col):
                if bank[r][c] == '1':
                    print('inside current')
                    current += 1
            if current != 0:
                final_ans += current * previous
                print(final_ans)
                previous = current
        return final_ans
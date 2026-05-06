from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])

        # Step 1: simulate gravity (stones fall right)
        for i in range(m):
            empty = n - 1
            for j in range(n - 1, -1, -1):
                if box[i][j] == '*':
                    empty = j - 1
                elif box[i][j] == '#':
                    box[i][j] = '.'
                    box[i][empty] = '#'
                    empty -= 1

        # Step 2: rotate 90° clockwise
        res = [[None] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][m - 1 - i] = box[i][j]

        return res
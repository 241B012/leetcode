from typing import List
from functools import lru_cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return piles[i]

            take_left = piles[i] - dp(i + 1, j)
            take_right = piles[j] - dp(i, j - 1)

            return max(take_left, take_right)

        return dp(0, len(piles) - 1) > 0
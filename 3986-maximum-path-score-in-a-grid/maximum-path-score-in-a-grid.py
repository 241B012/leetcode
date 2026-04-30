from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[i][j] = dict {cost: max_score}
        dp = [[{} for _ in range(n)] for _ in range(m)]
        
        # helper to get score & cost
        def get(val):
            if val == 0:
                return 0, 0
            elif val == 1:
                return 1, 1
            else:
                return 2, 1
        
        # initialize start
        s, c = get(grid[0][0])
        if c <= k:
            dp[0][0][c] = s
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                s, cost = get(grid[i][j])
                curr = {}
                
                # from top
                if i > 0:
                    for pc, ps in dp[i-1][j].items():
                        nc = pc + cost
                        if nc <= k:
                            curr[nc] = max(curr.get(nc, -1), ps + s)
                
                # from left
                if j > 0:
                    for pc, ps in dp[i][j-1].items():
                        nc = pc + cost
                        if nc <= k:
                            curr[nc] = max(curr.get(nc, -1), ps + s)
                
                dp[i][j] = curr
        
        if not dp[m-1][n-1]:
            return -1
        
        return max(dp[m-1][n-1].values())
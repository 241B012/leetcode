from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                # stay at i (not i+1) because reuse allowed
                backtrack(i, path, remaining - candidates[i])
                path.pop()

        backtrack(0, [], target)
        return res
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def backtrack(start, target, path):
            if target == 0:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                # skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # pruning
                if candidates[i] > target:
                    break
                
                # choose
                path.append(candidates[i])
                
                # move forward (i+1 because each element used once)
                backtrack(i+1, target - candidates[i], path)
                
                # backtrack
                path.pop()
        
        backtrack(0, target, [])
        return res
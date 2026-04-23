from collections import defaultdict

class Solution:
    def distance(self, nums):
        pos = defaultdict(list)
        
        # Step 1: store indices for each value
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        res = [0] * len(nums)
        
        # Step 2: process each group
        for indices in pos.values():
            n = len(indices)
            
            # prefix sum of indices
            prefix = [0] * (n + 1)
            for i in range(n):
                prefix[i + 1] = prefix[i] + indices[i]
            
            # Step 3: compute answer
            for i in range(n):
                left = indices[i] * i - prefix[i]
                right = (prefix[n] - prefix[i + 1]) - indices[i] * (n - i - 1)
                res[indices[i]] = left + right
        
        return res
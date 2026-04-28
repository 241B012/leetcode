from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        
        # Flatten grid
        for row in grid:
            arr.extend(row)
        
        # Check feasibility
        mod = arr[0] % x
        for num in arr:
            if num % x != mod:
                return -1
        
        # Sort and find median
        arr.sort()
        median = arr[len(arr) // 2]
        
        # Compute operations
        ops = 0
        for num in arr:
            ops += abs(num - median) // x
        
        return ops
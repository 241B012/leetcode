from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        
        # Calculate the sum of the entire array (prefix sum for picking all stones)
        current_prefix_sum = sum(stones)
        
        # Base case: if a player must pick the last possible index (n-1)
        # the game ends, and they get the total sum. Next player gets 0.
        dp = current_prefix_sum
        
        # Iterate backwards from the second-to-last index down to index 1
        # (Index 0 is invalid because a player must take x > 1 stones)
        for i in range(n - 1, 1, -1):
            # Subtract the stone we are leaving behind to get the previous prefix sum
            current_prefix_sum -= stones[i]
            
            # The player can either take the current prefix sum and give the remaining
            # optimal play to the opponent, OR skip this and take the optimal play of the next state
            dp = max(dp, current_prefix_sum - dp)
            
        return dp
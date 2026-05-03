class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] will store the number of unique BSTs that can be formed with i nodes
        dp = [0] * (n + 1)
        
        # Base cases:
        # 0 nodes (empty tree) = 1 way
        # 1 node = 1 way
        dp[0], dp[1] = 1, 1
        
        # Fill the dp table for nodes from 2 to n
        for nodes in range(2, n + 1):
            # For each number of nodes, we can pick any node 'i' to be the root
            for root in range(1, nodes + 1):
                # left subtree has (root - 1) nodes
                # right subtree has (nodes - root) nodes
                left = dp[root - 1]
                right = dp[nodes - root]
                
                # Total ways with 'root' as the root is the product of left and right ways
                dp[nodes] += left * right
                
        return dp[n]
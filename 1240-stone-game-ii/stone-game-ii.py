class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = total stones from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        # dp(i, M) = maximum stones current player can get
        # starting from index i with current M
        memo = {}

        def dp(i, M):
            # No piles left
            if i >= n:
                return 0

            # If we can take all remaining piles
            if 2 * M >= n - i:
                return suffix[i]

            if (i, M) in memo:
                return memo[(i, M)]

            best = 0

            # Try taking x piles
            for x in range(1, 2 * M + 1):
                # Current player gets x piles.
                # Opponent then gets dp(i+x, max(M,x))
                opponent = dp(i + x, max(M, x))

                current = suffix[i] - opponent

                best = max(best, current)

            memo[(i, M)] = best
            return best

        return dp(0, 1)
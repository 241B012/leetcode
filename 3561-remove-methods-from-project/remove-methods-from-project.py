from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)

        # Find all suspicious methods (reachable from k)
        suspicious = [False] * n

        def dfs(node):
            suspicious[node] = True
            for nei in graph[node]:
                if not suspicious[nei]:
                    dfs(nei)

        dfs(k)

        # Check if any non-suspicious method calls a suspicious one
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        # Remove all suspicious methods
        ans = []
        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans
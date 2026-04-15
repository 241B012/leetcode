class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = float('inf')
        
        for i in range(n):
            if words[i] == target:
                clockwise = (i - startIndex + n) % n
                counter = (startIndex - i + n) % n
                ans = min(ans, min(clockwise, counter))
        
        return ans if ans != float('inf') else -1
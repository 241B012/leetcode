class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        
        prefixes = set()
        
        # Store all prefixes from arr1
        for num in arr1:
            while num > 0:
                prefixes.add(num)
                num //= 10
        
        ans = 0
        
        # Check prefixes from arr2
        for num in arr2:
            while num > 0:
                if num in prefixes:
                    ans = max(ans, len(str(num)))
                    break
                num //= 10
        
        return ans
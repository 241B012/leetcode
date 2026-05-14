class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = max(nums)

        # base[n] should have length n + 1
        if len(nums) != n + 1:
            return False

        # sort and compare with [1,2,...,n,n]
        nums.sort()

        return nums == list(range(1, n + 1)) + [n]
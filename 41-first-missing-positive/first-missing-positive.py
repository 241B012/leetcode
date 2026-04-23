class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        # Step 1: place elements at correct positions
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        # Step 2: find first missing
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix
        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # Store all numbers for quick lookup
        nums_set = set(nums)

        # Find the smallest missing integer >= total
        while total in nums_set:
            total += 1

        return total
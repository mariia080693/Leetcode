class Solution(object):
    def thirdMax(self, nums):
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        if len(nums) < 3 :
            return max(nums)
        return nums[-3]     
        
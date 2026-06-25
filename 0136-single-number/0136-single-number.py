class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique_num = nums[0]
        for i in range(1, len(nums)):
            unique_num = unique_num ^ nums[i]
        return unique_num
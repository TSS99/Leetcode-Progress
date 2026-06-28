class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        ranges = []
        start = 0 
        
        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i] + 1 != nums[i + 1]:
                if start == i:
                    ranges.append(str(nums[start]))
                else:
                    ranges.append(f"{nums[start]}->{nums[i]}")
                start = i + 1
                
        return ranges
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half_len = (m + n + 1) // 2
        
        while left <= right:
            i = (left + right) // 2
            j = half_len - i
            
            # Get the elements around the partition, handling edge cases
            nums1_left_max = nums1[i - 1] if i > 0 else float('-inf')
            nums1_right_min = nums1[i] if i < m else float('inf')
            
            nums2_left_max = nums2[j - 1] if j > 0 else float('-inf')
            nums2_right_min = nums2[j] if j < n else float('inf')
            
            # Check if we found the correct partition
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # If the total number of elements is odd
                if (m + n) % 2 == 1:
                    return float(max(nums1_left_max, nums2_left_max))
                # If the total number of elements is even
                else:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0
            
            # Adjust the binary search range
            elif nums1_left_max > nums2_right_min:
                right = i - 1
            else:
                left = i + 1
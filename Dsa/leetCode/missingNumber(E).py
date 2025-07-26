class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i  /// It reachers time complxity O(n^2)
# Use brain use math
        lengthOfNums=len(nums)
        return int((lengthOfNums*(lengthOfNums+1)/2)-sum(nums))
    
'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''
'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # hashMap={}
        # for elements in nums:
        #     if elements in hashMap:
        #         return True
        #     hashMap[elements]=1
        # return False
        
        
        if len(set(nums))!=len(nums):
            return True
        else: 
            return False
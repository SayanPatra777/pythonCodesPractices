# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
# nums=[1,-1,0,2,3,-4,1,2]
nums = [-1,0,1,2,-1,-4]
listLen=len(nums)
numslist= (list([nums[i],nums[j],nums[k]] 
           for i in range(listLen) 
           for j in range(i+1, listLen) 
           for k in range(j+1, listLen) 
           if nums[i] + nums[j] + nums[k] == 0 and i != j
           and i != k and j != k
        ))
print(numslist)

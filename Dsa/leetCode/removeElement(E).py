# nums=[3,2,2,3]
# val=3
# count=nums.count(val)
# print(count)
# for i in range(count):
#     nums.remove(val)
# print(nums)

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # nums=[0,1,2,2,3,0,4,2]
        count=nums.count(val)
        for i in range (count):
            nums.remove(val)
        return len(nums)
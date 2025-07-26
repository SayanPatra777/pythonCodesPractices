class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        lenNums=len(nums)
        nums=set(nums)
        l=[]
        for i in range(1,lenNums+1):
            if i not in nums:
                l.append(i)
        return l
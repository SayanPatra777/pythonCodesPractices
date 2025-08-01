'''
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

'''
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums2Length=len(nums2)
        for j,element in enumerate(nums1):
            indexOfEle,flag,i=0,0,0
            nums1[j]=-1
            while i<len(nums2):
                if nums2[i]==element:
                    flag=1
                if flag ==1 and i<len(nums2)-1:
                    if element<nums2[i+1]:
                        nums1[j]=nums2[i+1]
                        break
                i+=1
        return nums1
    
    # According to LeetCode, the time complexity is O(n*m) where n is the length of nums1 and m is the length of nums2. So, it should be optimised. I'll write that benith 
class SolutionOptimized:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        # Step 1: Build next_greater map using monotonic stack
        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)

        # Step 2: Map results for nums1 using precomputed dictionary
        # You're looping through nums1 and trying to find the "next greater" element for each x. The .get() function on a Python dict is like asking:
# “Hey dictionary, do you have a value for this key x? If yes, give it to me. If not, give me -1

        return [next_greater.get(num, -1) for num in nums1]


s=SolutionOptimized()
print(s.nextGreaterElement([4,1,2,0],[3,4,2,0,1])) #[-1,-1,-1,1]

'''
🧩 Problem Recap (In Your Words)
You're given:
nums1 — a subset of nums2
For each element in nums1, find the next greater element in nums2.
If there's no greater element to its right — return -1
💡 Core Insight
Instead of looping through nums2 again and again for each nums1[i], we can preprocess nums2 once to record the next greater number for every element

'''
    
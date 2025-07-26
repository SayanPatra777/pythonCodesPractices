class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=-1
        while i>=(-len(digits)):
            if (digits[i]+1)//10<1:
                digits[i]+=1
                return digits
            else:
                if i==-len(digits):
                    digits[i]=1
                    digits.append(0)
                    return digits
                else:
                    digits[i]=0
                    i-=1
'''               
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0]. 
'''                
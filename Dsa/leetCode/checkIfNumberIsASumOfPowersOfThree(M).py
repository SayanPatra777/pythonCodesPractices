class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            rem=n%3
            if rem==2:
                return False
            n=n//3
        return True
s=Solution()
print(s.checkPowersOfThree(91))

'''    
So here in this problem it is given that " The number can not be represented as a sum of powers of 3 if it's ternary presentation has a 2 in it "
so here I just find turnary representation ..
What Is Base 3 (Ternary)?
In base 3, each digit represents a power of 3, and the digits can only be:
5=1 × 3^1+ 2×3^0 = (12) base 3   

'''
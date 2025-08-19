import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # return n>0 and math.log(n,4).is_integer()   #here is_integer() check the floats values after decimal if there is nothing after the . it return True
        

        if n<0:
            return False
        i=0
        while True:
            temp = 4**i
            if temp==n:
                return True
            elif temp>n:
                return False
            i+=1
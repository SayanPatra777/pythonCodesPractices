class Solution:
    def hammingWeight(self, n: int) -> int:
        n=bin(n)
        sumOfBits=0
        n=n[-1:-len(n)+1:-1]
        for nums in n:
            sumOfBits+=int(nums)
        return sumOfBits

# Leetcode optimal (efficient) version
'''
# code

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

# Explaination

🔁 while n:
Loop runs until all bits in n are processed (i.e., until n == 0).

Each iteration shifts the binary number one bit to the right, so you examine one bit per loop.

⚙️ count += n & 1
The key bitwise trick:

n & 1 checks the last (least significant) bit of n.

It results in either 1 or 0.

You add the result to count.

n >>= 1
Right shift: drops the last bit of n and moves to the next one.

It's like dividing n by 2 (but for bits!).

'''
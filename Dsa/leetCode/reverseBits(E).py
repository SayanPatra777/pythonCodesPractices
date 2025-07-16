class Solution:
    def reverseBits(self, n: int) -> int:
        n=f'{n:032b}'
        num=0
        # print(n)
        # n1=str(n)
        for i ,digit in enumerate (n):
            num+=int(digit)*(2**i)
        return num
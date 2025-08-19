class Solution:
    def maximum69Number (self, num: int) -> int:
        num=list(str(num))
        count=0
        for digit in num:
            if digit=="6":
                num[count]="9"
                break
            count+=1
        return int("".join(num))
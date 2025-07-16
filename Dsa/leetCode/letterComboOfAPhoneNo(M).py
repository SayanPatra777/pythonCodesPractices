from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        listStr=[]
        i=1
        tableId={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        if not len(digits):
            return listStr
        if len(digits)>1:
            while i<len(digits):
                listStr+=("".join(items)for items in product(tableId[digits[0]],tableId[digits[i]]))
                i+=1
            return listStr
        else:
            return sorted(tableId[digits])
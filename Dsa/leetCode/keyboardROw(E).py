class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        lenList=len(words)
        # k=0
        firstRow=set("qwertyuiop")
        secondRow=set("asdfghjkl")
        thirdRow=set("zxcvbnm")
        for i in range(lenList):
            if set(words[i].lower()) <=firstRow or set(words[i].lower()) <=(secondRow) or set(words[i].lower()) <=(thirdRow):
                words.append(words[i])
        return words[lenList:]

        # or
        #         words[k] = words[i]
        #         k += 1
                
        # return words[:k]
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        newS=s[::-1]
        for i in range(len(s)):
            if newS[i]==" ":
                return i
        return len(s)
s=Solution()
print(s.lengthOfLastWord("Hello World"))
print(s.lengthOfLastWord("   fly me   to   the moon  "))
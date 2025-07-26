class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j,maxlen=0,0,1
        tempSet=set()
        if not s:
            return 0
        while i<len(s) and j<len(s):
            if i==j:
                j+=1
                tempSet.add(s[i])
                # maxlen=max(maxlen,j-i+1)
            elif s[i]!=s[j] and s[j] not in tempSet:
                tempSet.add(s[j])
                maxlen=max(maxlen,j-i+1)
                j+=1
            else:
                tempSet.remove(s[i])
                i+=1
        return maxlen
s=Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(s.lengthOfLongestSubstring("bbbbb"))  # Output: 1
print(s.lengthOfLongestSubstring("pwwkew"))  # Output: 3
print(s.lengthOfLongestSubstring("a"))  # Output: 1
print(s.lengthOfLongestSubstring("dvdf"))
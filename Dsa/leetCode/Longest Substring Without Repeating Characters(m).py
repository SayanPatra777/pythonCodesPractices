class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # chars=[]
        # maxlen=0
        # temp=0
        # for i in range (len(s)):
        #     if s[i] not in chars:
        #         chars.append(s[i])
        #     else:
        #         temp=len(chars)
        #         if s[i]!=s[i+1]:
        #             chars=chars[-1:]
        #             chars.append(s[i])
        #         else:
        #             chars=[]
        #         if maxlen<temp:
        #             maxlen=temp
        # temp=len(chars)
        # chars=chars[-1:]
        # if maxlen<temp:
        #     maxlen=temp
        # return maxlen
        
        # s is input
        # taking two pointers l and m
        m=1
        tempval=0
        maxlen=0
        for l in range (s):
            while s[l]!=s[m]:
                tempval=m-l
                m+=1
            maxlen=max(maxlen,tempval)
        return maxlen
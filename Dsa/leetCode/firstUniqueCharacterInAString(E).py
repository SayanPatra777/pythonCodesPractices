'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''

#  My way 
class Solution1:
    def firstUniqChar(self, s: str) -> int:
        hashmap={}
        for char in s:
            if char not in hashmap:
                hashmap[char]=1
            else: 
                hashmap[char]+=1
        min_key = min(hashmap, key=hashmap.get)
        return s.index(min_key) if hashmap[min_key]==1 else -1



#  Ai way 
class Solution2:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for idx, char in enumerate(s):
            if freq[char] == 1:
                return idx
        return -1
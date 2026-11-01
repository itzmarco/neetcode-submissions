from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hashmap = [0]*26
        OFFSET = ord('a')
        get_idx = lambda x: ord(x) - OFFSET
        
        for ch in s:
            idx = get_idx(ch)
            hashmap[idx] += 1
        
        for ch in t:
            idx = get_idx(ch)
            if hashmap[idx]:
                hashmap[idx] -= 1
            else:
                return False
        
        return True
        

            
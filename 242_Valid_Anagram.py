class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freq_s = {}
        for c in s:
            freq_s[c] = freq_s.get(c, 0) + 1
        freq_t = {}
        for c in t:
            freq_t[c] =  freq_t.get(c, 0) + 1
        
        for k in freq_s:
            if freq_s[k] != freq_t.get(k, 0):
                return False
        for k in freq_t:
            if freq_t[k] != freq_s.get(k, 0):
                return False
        return True
        
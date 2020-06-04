class Solution:
    def romanToInt(self, s: str) -> int:
        MAP = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        ans = MAP[s[0]]
        for i in range(1, len(s)):
            if MAP[s[i]] <= MAP[s[i-1]]:
                ans += MAP[s[i]]
            else:
                ans = ans + MAP[s[i]] - 2*MAP[s[i-1]]
        return ans
        
class Solution:
    def hammingWeight(self, n: int) -> int:
        x = n
        ans = 0
        while x:
            x = x&(x-1)
            ans += 1
        return ans
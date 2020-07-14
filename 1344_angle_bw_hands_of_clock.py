class Solution:
    def angleClock(self, h: int, m: int) -> float:
        ans = abs(30*(h%12) - 5.5*m)
        return min(360-ans, ans)
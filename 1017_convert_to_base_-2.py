class Solution:
    def quo_rem(self, num):
        return (num/-2, 0) if num % 2 == 0 else ((num-1)/-2, 1 )
        
    def baseNeg2(self, N: int) -> str:
        
        ans = []
        while True:
            quo, rem = self.quo_rem(N)
            ans.append(rem)
            N = quo
            if N == 0:
                break
        return ''.join(map(str,reversed(ans)))
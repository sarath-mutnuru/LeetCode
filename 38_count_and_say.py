class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        for _ in range(1,n):
            i = 0
            c = ''
            while i < len(ans):
                j = i
                while j < len(ans) and ans[j] == ans[i]:
                    j += 1
                num_times = j - i
                c = c + str(num_times) + ans[i]
                i = j
            ans = c
        return ans
        
        
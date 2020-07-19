class Solution:
    def addBinary(self, s1: str, s2: str) -> str:
        ans = ''
        n1, n2 = len(s1), len(s2)
        c = 0
        for i in range(max(n1,n2)):
            
            tot = c + (int(s1[n1-i-1]) if n1-i-1 >=0 else 0 ) + (int(s2[n2-i-1]) if n2-i-1 >=0 else 0 )
            dig, c = tot%2, tot//2
            ans = str(dig)+ans
        if c:
            ans = '1'+ans
        #print(ans)
        return ans
            
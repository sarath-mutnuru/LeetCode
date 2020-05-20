class Solution:
    def isInt(self, c):
        return c in map(str,list(range(10)))
    def f(self,a):
        if a > 2**31 - 1:
            return 2**31 - 1
        if a < -2**31:
            return -2**31
        return a
    def myAtoi(self, str: str) -> int:
        idx = 0
        while True:
            if idx >= len(str) or str[idx] != ' ':
                break
            idx += 1
        if idx >= len(str):
            return 0
        #print(idx)
        if not ( self.isInt(str[idx]) or str[idx] in ['+','-'] ):
            return 0
        sgn = 1
        if str[idx] == '+':
            idx += 1
        elif str[idx] == '-':
            sgn = -1 
            idx += 1
                
        ans = 0
        
        for i in range(idx,len(str)):
            if not self.isInt(str[i]):
                return self.f(sgn*ans)
            ans = ans*10 + int(str[i])
        
        return self.f(ans*sgn)
                
        
                                   
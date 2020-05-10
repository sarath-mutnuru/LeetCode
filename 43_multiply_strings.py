class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1[0] == '0' or num2[0] == '0':
            return "0"
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        v = []
        c = []
        for i in range(len(num1)):
            for j in range(len(num2)):
                
                res = int(num1[i]) * int(num2[j])
                idx = i + j
                
                if idx < len(c) :
                    res += c[idx]
                    c[idx] = 0
                else:
                    c.append(0)
                
                if idx < len(v):
                    res += v[idx]
                    
                val = res % 10
                car = res // 10
                
                if idx < len(v):
                    v[idx] = val
                else:
                    v.append(val)
                
                if idx + 1 < len(c):
                    c[idx + 1] += car
                else:
                    c.append(car)
        
        if i + j + 1 < len(c) and c[i + j + 1] != 0:
            v.append(c[i + j + 1])
        
        ans = ''.join(map(str,v[::-1]))
        return ans
                    
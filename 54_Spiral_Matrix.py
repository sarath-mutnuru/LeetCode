class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n_r = len(matrix)
        n_c = len(matrix[0]) if matrix else 0
        t = 0
        b = n_r - 1
        
        l = 0
        r = n_c - 1
        ans = []
        while t <=b and l <= r:
            for i in range(l, r+1):
                ans.append(matrix[t][i])
            t += 1
            
            for i in range(t, b + 1):
                ans.append(matrix[i][r])
            r -= 1
            
            if t <= b:
                for i in range(r, l - 1, -1):
                    ans.append(matrix[b][i])
                b -= 1
                
            if l <= r :
                for i in range(b, t - 1, -1):
                    ans.append(matrix[i][l])
                l += 1
                
        return ans

            
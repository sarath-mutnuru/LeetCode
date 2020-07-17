class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        ans=[]
        for j in range(cols):
            for i in range(rows):
                if mat[i][j] == 0 and i not in ans:
                    ans.append(i)
                    k -= 1
                    if k == 0:
                        return ans
        for i in range(rows):
            if i not in ans:
                ans.append(i)
                k -= 1
                if k == 0:
                    return ans
        
                    
        
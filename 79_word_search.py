class Solution:
    def exist(self, mat: List[List[str]], word: str) -> bool:
        def e_util(i,j,word,used):
            if len(word) == 0:
                return True
            if mat[i][j] != word[0]:
                return False
            if mat[i][j] == word[0] and len(word) == 1:
                used[i][j] = True
                return True
            used[i][j] = True
            top = e_util(i-1,j,word[1:],used) if i-1 >= 0 and not used[i-1][j] else False
            bottom = e_util(i+1,j,word[1:],used) if i+1 < len(mat) and not used[i+1][j] else False
            right = e_util(i,j+1,word[1:],used) if j+1 < len(mat[0]) and not used[i][j+1] else False
            left = e_util(i,j-1,word[1:],used) if j-1 >=0 and not used[i][j-1] else False
            if top or bottom or left or right:
                return True
            used[i][j] = False
            return False
        
        used = [[False for _ in range(len(mat[0]))] for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if e_util(i,j,word,used):
                    return True
    
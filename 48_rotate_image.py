class Solution:
    def rotate(self, M: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(M)
        left, right = 0, n-1
        top, bottom = 0, n-1
        iter = 0
        while left < right and top < bottom:
            iter += 1
            tl, tr, bl, br = M[top][left], M[top][right], M[bottom][left], M[bottom][right]
            k = [M[i][right] for i in range(top+1, bottom)]
            print(k)
            for i in range(top+1,bottom):
                M[i][right] = M[top][i]
            for i in range(left+1, bottom):
                M[top][i] = M[bottom-(i-left)][left]
            for i in range(left+1, right):
                M[i][left] = M[bottom][i]
            for i in range(top+1, bottom):
                M[bottom][i] = k[len(k)-(i-top)]           
            M[top][left], M[top][right], M[bottom][left], M[bottom][right] = bl, tl, br, tr
            print(M)
            print(iter)
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        
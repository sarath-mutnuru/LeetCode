class Solution:
    def setZeroes(self, arr: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col  = False, False
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] == 0:
                    if i == 0:
                        row = True
                    if j == 0:
                        col = True
                    arr[0][j], arr[i][0] = 0,0
        print(arr)
        for i in range(1,len(arr[0])):
            if arr[0][i] == 0:
                for j in range(len(arr)):
                    arr[j][i] = 0
        print(arr)
        for i in range(1,len(arr)):
            if arr[i][0] == 0:
                for j in range(len(arr[0])):
                    arr[i][j] = 0
        if row:
            for j in range(len(arr[0])):
                arr[0][j] =0
        if col:
            for i in range(len(arr)):
                arr[i][0] = 0
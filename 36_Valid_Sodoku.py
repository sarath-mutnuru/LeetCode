class Solution:
    def has_duplicate(self,reg):
        v = [ 0 for _ in range(9)]
        for e in reg:
            if e != '.':
                if v[int(e) - 1] == 1:
                    return True
                v[int(e) - 1 ] += 1
        return False
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        vals = []
        for i in range(9):
            rowDupl = self.has_duplicate(board[i])
            if rowDupl:
                return False
            colDupl = self.has_duplicate([row[i] for row in board])
            if colDupl:
                return False
            vals.append(rowDupl)
            vals.append(colDupl)
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                reg = [board[I][J] for I in range(i,i+3) for J in range(j,j+3)]
                regDupl = self.has_duplicate(reg)
                if regDupl:
                    return False
                vals.append(self.has_duplicate(reg))
                
        return not any(vals)
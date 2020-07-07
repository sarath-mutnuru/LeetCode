class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        f = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    f = 1
                    break
            if f:
                break
                    
        source = (i, j)
        s = [source]
        visited = set()
        num_nodes, num_edges = 0, 0
        
        while s:
            n = s.pop()
            if n not in visited:
                num_nodes += 1
                visited.add(n)
                if n[0]+1 < r:
                    if grid[n[0]+1][n[1]] and (n[0]+1,n[1]) not in visited:
                        s.append((n[0]+1,n[1]))
                        num_edges += 1
                if n[0]-1 >= 0:
                    if grid[n[0]-1][n[1]] and (n[0]-1,n[1]) not in visited:
                        s.append((n[0]-1,n[1]))
                        num_edges += 1
                        
                if n[1]+1 < c:
                    if grid[n[0]][n[1] + 1] and (n[0],n[1]+1) not in visited:
                        s.append((n[0],n[1]+1))
                        num_edges += 1
                if n[1]-1 >= 0:
                    if grid[n[0]][n[1] - 1] and (n[0],n[1]-1) not in visited:
                        s.append((n[0],n[1]-1))
                        num_edges += 1
        return num_nodes*4  - num_edges*2
                    
def numIslands(grid):
        

    def isIsland(grid,x,y,n,m):
        if x < 0 or x >= n or y < 0 or y >= m  or grid[x][y] != "1" : 
            return 
        
        grid[x][y] = 0

        isIsland(grid,x,y+1,n,m)
        isIsland(grid,x,y-1,n,m)
        isIsland(grid,x+1,y,n,m)
        isIsland(grid,x-1,y,n,m)

    count = 0
    n = len(grid)
    m = len(grid[0])

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1":
                count += 1
                isIsland(grid,i,j,n,m)
    return count

print(numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
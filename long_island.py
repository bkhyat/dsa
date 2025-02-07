def long_island(grid):
    if not grid:
        return 0
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                count += 1
                recursive(grid, i, j)
    return count

def recursive(grid, i, j):
    if i<0 or i>len(grid)-1 or j<0 or j>len(grid[0])-1 or grid[i][j] == 0: return

    grid[i][j] = 0
    recursive(grid, i - 1, j)
    recursive(grid, i + 1, j)
    recursive(grid, i, j - 1)
    recursive(grid, i, j + 1)
    # if i>0:
    #     if grid[i-1][j] == 1:
    #         grid[i - 1][j] = 0
    #         recursive(grid, i-1, j)
    # if i<len(grid)-1:
    #     if grid[i+1][j] == 1:
    #         grid[i+1][j] = 0
    #         recursive(grid, i+1, j)
    #
    # if j>0:
    #     if grid[i][j-1] == 1:
    #         grid[i][j-1] = 0
    #         recursive(grid, i, j-1)
    #
    # if j<len(grid[0])-1:
    #     if grid[i][j+1] == 1:
    #         grid[i][j+1] = 0
    #         recursive(grid, i, j+1)

if __name__ == '__main__':
    grid = [[int(i) for i in row.strip()] for row in """
    11000
    11000
    00100
    00011
    00011
    """.strip().split("\n")]
    print(long_island(grid))
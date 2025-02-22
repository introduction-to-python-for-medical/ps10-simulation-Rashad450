import copy
def spread_fire(grid):
    
    grid_size = len(grid) 
    new_grid = copy.deepcopy(grid)
    
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1:
               if((i > 0 and grid[i-1][j] == 2) or 
                  (i < grid_size - 1 and grid[i+1][j] == 2) or 
                  (j > 0 and grid[i][j-1] == 2) or 
                  (j < grid_size - 1 and grid[i][j+1] == 2)):
                  new_grid[i][j] = 2
                 

    return new_grid


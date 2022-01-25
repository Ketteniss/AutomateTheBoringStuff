# Conway's Game of Life
import random, time, copy
WIDTH = 60
HEIGHT = 20 
black = [(1,3), (1,4), (2,3), (2,4), (3,3), (3,4)]
# Create a list of list for the cells:
grid = []
for x in range(WIDTH):
    column = [] # Create a new column.
    for y in range(HEIGHT):
        if (x,y) in black:
            column.append('#') # Add a living cell.
        else:
            column.append(' ') # Add a dead cell.
    grid.append(column) # nextCells is a list of column lists.

    # Print currentCells on the screen:
for y in range(HEIGHT):
    for x in range(WIDTH):
        print(grid[x][y], end='') # Print the # or space.
    print() # Print a newline at the end of the row.

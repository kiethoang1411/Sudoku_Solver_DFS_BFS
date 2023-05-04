from BFS_Sudoku import BFS_solve
from DFS_Sudoku import DFS_solve

print ("\n\nTesting on easy 6x6 grid...")
grid = [[6,0,0,0,0,0],
      [0,0,1,3,0,6],
      [0,0,4,0,0,0],
      [1,2,0,0,0,0],
      [0,0,0,0,0,4],
      [3,0,5,0,0,0]]

print ("Problem:")
for row in grid:
      print (row)

BFS_solve(grid)
DFS_solve(grid)

print ("\n\nTesting on hard 6x6 grid...")
grid = [[0,0,0,3,0,0],
      [0,0,0,0,5,0],
      [0,0,3,0,0,0],
      [0,5,0,0,0,0],
      [6,0,0,5,4,0],
      [0,0,2,0,6,0]]

print ("Problem:")
for row in grid:
      print (row)

BFS_solve(grid)
DFS_solve(grid)

print ("\n\nTesting on invalid 9x9 grid...")
grid = [[0,0,9,0,7,0,0,0,5],
      [0,0,2,1,0,0,9,0,0],
      [1,0,0,0,2,8,0,0,0],
      [0,7,0,0,0,5,0,0,1],
      [0,0,8,5,1,0,0,0,0],
      [0,5,0,0,0,0,3,0,0],
      [0,0,0,0,0,3,0,0,6],
      [8,0,0,0,0,0,0,0,0],
      [2,1,0,0,0,0,0,8,7]]

print ("Problem:")
for row in grid:
      print (row)

BFS_solve(grid)
DFS_solve(grid)

print ("\n\nTesting on easy 9x9 grid...")
grid = [[0,0,7,2,8,0,0,0,0], 
      [0,0,0,0,0,0,5,0,6],
      [4,1,3,0,0,6,0,8,0],
      [7,2,0,3,9,0,0,0,0],
      [3,4,0,0,0,0,8,1,0],
      [6,8,0,1,0,7,0,0,2],
      [0,0,0,6,7,4,0,2,3],
      [0,0,0,0,0,5,7,0,0],
      [1,0,6,0,2,3,0,4,0]]

print ("Problem:")
for row in grid:
      print (row)
      
BFS_solve(grid)
DFS_solve(grid)


print ("\n\nTesting on medium 9x9 grid...")
grid = [[0,0,2,0,3,0,0,0,8],
      [0,0,0,0,0,8,0,0,0],
      [0,3,1,0,2,0,0,0,0],
      [0,6,0,0,5,0,2,7,0],
      [0,1,0,0,0,0,0,5,0],
      [2,0,4,0,6,0,0,3,1],
      [0,0,0,0,8,0,6,0,5],
      [0,0,0,0,0,0,0,1,3],
      [0,0,5,3,1,0,4,0,0]]

print ("Problem:")
for row in grid:
      print (row)

BFS_solve(grid)
DFS_solve(grid)


print ("\n\nTesting on very hard 9x9 grid...")
grid = [[0,3,0,0,0,1,5,0,0],
      [0,0,0,5,0,0,0,8,4],
      [0,0,5,0,0,7,0,6,0],
      [0,0,0,0,0,0,0,0,0],
      [0,8,0,2,0,0,0,7,0],
      [0,0,0,8,5,0,0,0,9],
      [0,0,3,0,9,4,0,0,7],
      [0,0,4,0,0,0,0,0,8],
      [5,0,6,0,1,0,0,0,0]]
 
print ("Problem:")
for row in grid:
      print (row)

BFS_solve(grid)
DFS_solve(grid)

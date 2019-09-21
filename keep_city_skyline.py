from typing import List, Tuple, Dict, TextIO

def maxIncreaseKeepingSkyline(grid:List[List[int]])->int:
	row_maxes=[max(row) for row in grid]
	col_maxes=[max(col) for col in zip(grid)]
	
	return sum(min(row_maxes[r], col_maxes[c])-val
			for r, row in enumerate(grid)
			for c, val in enumerate(row))
#zip example
	#i,j,k,l=zip(*grid)
	#print (i,j,k,l)
	return 1
	
grid=[[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
maxIncreaseKeepingSkyline(grid)
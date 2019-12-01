import pandas as pd
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

class MultiModal_Planner:

	def load_Map(self,data_path):
		self.map = list(pd.read_csv(data_path, sep=',',header=None).values)
		self.noRows = len(self.map)
		self.noCols = len(self.map[0])

	def cellToRC(self,cellnum):
		row = int( cellnum / self.noRows)
		rowstart = row * self.noCols
		col = cellnum - rowstart
		return (row,col)

	def rcToCell(self,row,col):
		return row*self.noRows + col

	def plan_path(self, startCell, endCell):
		route = []

		grid = Grid(matrix=self.map)

		start_RC = self.cellToRC(startCell)
		end_RC = self.cellToRC(endCell)

		start_node = grid.node( start_RC[0] , start_RC[1] )
		end_node = grid.node( end_RC[0] , end_RC[1] )

		finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
		path, runs = finder.find_path(start_node, end_node, grid)

		transformed_path = []
		for tplnum in range( len(path) ):
			inv_cellNum = self.rcToCell(   path[tplnum][1] , path[tplnum][0]   )
			transformed_path.append(  inv_cellNum  )
			#transformed_path.append(  (path[tplnum][1],path[tplnum][0])  )

		return transformed_path,runs

"""
plnr = MultiModal_Planner()
plnr.load_Map('Map.csv')
path,runs = plnr.plan_path(0, 24)
print(path)
"""
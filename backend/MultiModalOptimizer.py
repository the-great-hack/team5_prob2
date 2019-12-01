import numpy as np
import pandas as pd
import mlrose
import time


class MultiModal_Optimizer:

	def __init__(self,user_preferences,route,modes,max_switches=2):
		self.user_preferences = user_preferences
		self.route = route
		self.max_switches = max_switches
		self.modes = modes
		self.no_modes = len(modes)

	def load_location_stats(self,data_path):
		self.loc_df = pd.read_csv(data_path)
		print(self.loc_df.head())

	def generate_combinations(self):
		pass

	def generate_personalizedScores(self):

		for curMode in self.modes:

			self.loc_df[ curMode+'_Score'] = self.loc_df[curMode+'TimePerkm'] * self.user_preferences['time'] + \
												self.loc_df[curMode+'CostPerkm'] * self.user_preferences['cost']
		print( self.loc_df.head(5)  )

	def fitnessFunction_subroute(self,modeNum,cellNums):
		score = 0

		return score

	def evaluateSolution(self,solution):
		score = 0

		return score

	def getSolutions_GraphSearch(self,multiple_sols=True):
		sols = {}
		return sols

	def getSolutions_Combinatorial(self,multiple_sols=True):
		sols = {}
		return sols

	def getSolutions_Metaheuristic(self,multiple_sols=True):
		sols = {}
		return sols






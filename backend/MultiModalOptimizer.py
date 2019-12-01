import numpy as np
import pandas as pd
import itertools
#import mlrose
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

	def generate_ModeCombinations(self):
		self.modeCombos = list(  itertools.product( list( range(self.no_modes)   ) , repeat = self.max_switches+1  ))
		print("No Mode Combinations : ",  len(self.modeCombos) )

	def generate_SwitchCombinations(self,subroute):

		self.switchCombos = list(itertools.permutations( subroute[1:-1] , self.max_switches ))
		print( "No Switch Combinations : ", len(self.switchCombos) )

	def generate_personalizedScores(self):
		encodeDict = {1:1.2,2:1}
		self.user_preferences['time'] = encodeDict[self.user_preferences['time']]
		self.user_preferences['cost'] = encodeDict[self.user_preferences['cost']]

		for curMode in self.modes:

			self.loc_df[ curMode+'_Score'] = self.loc_df[curMode+'TimePerkm'] * self.user_preferences['time'] + \
												self.loc_df[curMode+'CostPerkm'] * self.user_preferences['cost']


		print("Personalized Scores : ",self.loc_df.head(5))

	def fitnessFunction_subroute(self,modeNum,cellNums):
		score = 0
		modeName = self.modes[modeNum]

		for cellnum in cellNums:
			modecellScore = self.loc_df[ modeName+'_Score'].values[cellnum]
			score += modecellScore

		return score

	def evaluateSolution(self,solution):
		score = 0

		return score

	def sol_Describe(self,sol_list):
		sol_desc = []
		noCombs = len(self.modeCombos[0])
		for i in range( noCombs ):
			sol_desc.append(   ( self.modes[sol_list[i]]  , sol_list[ i + noCombs ])       )
		return sol_desc


	def getSolutions_Combinatorial(self,multiple_sols=True):
		sols = {}

		self.generate_ModeCombinations()
		self.generate_SwitchCombinations(self.route)

		for modeComb in self.modeCombos:
			for switchComb in self.switchCombos:
				potential_solution = list(modeComb) + list(switchComb) + [self.route[-1]]
				#print(potential_solution)
				print(   self.sol_Describe( potential_solution ) )



		"""

		for modeComb in self.modeCombos:
			print(modeComb)
			switchComb = []
			temp_route = [rtv for rtv in self.route]
			for i in range(  len(switchComb)   ):
				print("")

		"""

		return sols

	def getSolutions_Metaheuristic(self,multiple_sols=True):
		sols = {}
		return sols






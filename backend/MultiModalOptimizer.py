import numpy as np
import pandas as pd
import itertools
#import mlrose
import math
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

	def fitnessFunction_subroute(self,modeName,cellNums):
		score = 0

		for cellnum in cellNums:
			modecellScore = self.loc_df[ modeName+'_Score'].values[cellnum]
			score += modecellScore

		return score

	def sol_Describe(self,sol_list):
		sol_desc = []
		noCombs = len(self.modeCombos[0])
		for i in range( noCombs ):
			sol_desc.append(   ( self.modes[sol_list[i]]  , sol_list[ i + noCombs ])   )
		return sol_desc

	def sameSwitch_isValid(self,sol_desc):
		for i in range( len(sol_desc)-1):
			if sol_desc[i][0] == sol_desc[i+1][0]:
				return False
		return True

	def family_isValid(self,sol_desc):
		for i in range( len(sol_desc) ):

			if sol_desc[i][0] == 'Bike' and self.user_preferences['family'] == 1 :
				return False

		return True


	def evaluateSolution(self,solution):
		total_score = 0

		
		for i in range( len(solution) -1):

			startIndx = self.route.index( solution[i][1] )
			endIndx = self.route.index( solution[i+1][1] )
			cellNums = self.route[ startIndx : endIndx+1 ]
			cur_mode = solution[i][0]
			cur_score = self.fitnessFunction_subroute( cur_mode , cellNums )
			total_score += cur_score


		return total_score


	def getSolutions_Combinatorial(self,multiple_sols=True):

		self.generate_ModeCombinations()
		self.generate_SwitchCombinations(self.route)

		bestSol = self.sol_Describe( list(self.modeCombos[0]) + list(self.switchCombos[0]) + [self.route[-1]] )
		bestScore = math.inf

		for modeComb in self.modeCombos:
			for switchComb in self.switchCombos:
				potential_solution = list(modeComb) + list(switchComb) + [self.route[-1]]
				#print(potential_solution)
				desc_sol = self.sol_Describe( potential_solution )
				if self.sameSwitch_isValid(desc_sol) and self.family_isValid(desc_sol) :
					curScore = self.evaluateSolution( desc_sol )
					if curScore < bestScore:
						bestScore = curScore
						bestSol = desc_sol

		return bestSol

	def getSolutions_Metaheuristic(self,multiple_sols=True):
		sols = {}
		return sols






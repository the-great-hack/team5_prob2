import numpy as np
import mlrose
import time


class MultiModal_Optimizer:

	def __init__(self,max_switches=2,no_modes=3):
		self.max_switches = max_switches
		self.no_modes = no_modes
		self.alogs = ['SA','GA','MM','BR']

	def load_map_scores(self,data_path):
		pass

	def get_user_preferences(self,data_path):
		pass

	def fitnessFunction(self,solution):
		score = 0

		return score

	def get_optimal_solutions(self,multiple_sols=False,algo='SA'):
		sols = {}
		return sols

	def post_solution(self,sols):
		pass






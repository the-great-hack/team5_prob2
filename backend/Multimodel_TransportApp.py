import numpy as np
import pandas as pd
import json
import MultimodalPlanner
import MultimodalOptimizer

def get_user_preferences_json(filePath):
	with open(filePath) as json_file:
		data = json.load(json_file)
	return data['user_data']

def get_user_preferences_API():
	return {}

def main():

	user_preferences = get_user_preferences_json("user_prefs.json")
	print("User Preferences : ",user_preferences)

	planner = MultimodalPlanner.MultiModal_Planner()
	planner.load_Map('Map.csv')
	path,runs = planner.plan_path( user_preferences['pickup'] , user_preferences['dropoff'])
	print("Planned Path : ",path)

	modes = ["Bike","Go","GoMini","Rikshaw","Bus"]
	optimizer = MultimodalOptimizer.MultiModal_Optimizer(user_preferences,path,modes,max_switches=2)
	optimizer.load_location_stats('location_stats.csv')
	optimizer.generate_personalizedScores()
	solution = optimizer.getSolutions_Combinatorial()
	print("Solution : ", solution)

	print("________________")
  
if __name__== "__main__":
	main()
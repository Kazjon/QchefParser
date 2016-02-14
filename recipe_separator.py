import pymongo

def separate(recipe_source, collection):

	recipes = []
	
	for line in recipe_source:
		# Determine which format it's in
		if line.startswith("MMMMM----") and "Meal-Master" in line:
			# Create new recipe instance
			recipe = {"raw_text": [], "format": "mmf"}
		# Store the line
		recipe["raw_text"].append(line)
		# End recipe instance
		if "MMMMM" in line.strip("\n") and "----" not in line.strip("\n"):
			recipes.append(recipe)
			#print recipe["raw_text"]
			#print "$$$$$$$$$$$$"

	print "Number of recipes:", len(recipes)
	#print recipes
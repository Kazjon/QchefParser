with open('recipe-text-sample.txt') as myFile:
	recipe_source = myFile.readlines()

recipes = []

for line in recipe_source:
	# Determine which format it's in
	if line.startswith("MMMMM----") and "Meal-Master" in line:
		# Create new recipe instance
		recipe = {"raw_text": [], "format": "mmf", "metadata": []}
	# Store the line
	recipe["raw_text"].append(line)
	# End recipe instance
	if "MMMMM" in line.strip("\n") and "----" not in line.strip("\n"):
		recipes.append(recipe)
		#print recipe["raw_text"]
		#print "$$$$$$$$$$$$"

print "Number of recipes:", len(recipes), "\n"

#print individual recipes
# i = 0
# for i in recipes:
# 	print "\n"
# 	print "- - - - - - - recipe - - - - - - - - - "
# 	print i
# 	print "\n"

# Separate recipe into parts: (A) metadata (B) ingredients list (C) steps
raw_text = recipes[0]["raw_text"]

for line in raw_text:
	# print line
	if "Title: " in line.strip("\n"):
		recipes[0]["metadata"].append(line)
	if "Categories: " in line.strip("\n"):
		recipes[0]["metadata"].append(line)
	if "Yield: " in line.strip("\n"):
		recipes[0]["metadata"].append(line)
print recipes[0]["metadata"], "\n"
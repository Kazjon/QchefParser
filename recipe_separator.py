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


# Separate recipe into parts:
# (1) title
# (2) metadata
# (3) ingredients list
# (4) steps

raw_text = recipes[0]["raw_text"]

section_start = 0

title = ""
categories = ""
servings = ""
ingredients_list_lines = []
steps = []


def store_title (raw_string):
	title = raw_string.split(": ")[1]
	print title

def store_categories (raw_string):
	categories = raw_string.split(": ")[1]
	print categories

def store_servings (raw_string):
	servings = raw_string.split(": ")[1]
	servings = servings.split(" ")[0]
	print servings

def store_ingredients (raw_string):
	ingredients_list_lines.append(raw_string)
	print raw_string

def store_steps (raw_string):
	steps.append(raw_string)
	print raw_string

for i, line in enumerate(raw_text):
	stripped = line.strip(" \t\n\r")
	if stripped.startswith("Title:"):
		store_title(stripped)
	if stripped.startswith("Categories:"):
		store_categories(stripped)
	if stripped.startswith("Yield:"):
		store_servings(stripped)

	if len(stripped) < 1:
		section_start += 1
		if section_start == 1:
			print "--- Metadata ---"
		if section_start == 2:
			print "--- Ingredients ---"
		if section_start == 3:
			print "--- Steps ---"

	if section_start == 2:
		store_ingredients(stripped)

	if section_start == 3:
		store_steps(stripped)


print ""
print ingredients_list_lines




# for line in raw_text:
# 	# print line
# 	if "Title: " in line.strip("\n"):
# 		recipes[0]["metadata"].append(line)
# 	if "Categories: " in line.strip("\n"):
# 		recipes[0]["metadata"].append(line)
# 	if "Yield: " in line.strip("\n"):
# 		recipes[0]["metadata"].append(line)
# print recipes[0]["metadata"], "\n"
import pymongo, argparse, recipe_separator, sys


if __name__ == "__main__":
	print "Running the Q-chef Recipe Parser."
	parser = argparse.ArgumentParser(description='Use this to import recipes into mongodb for use with Q-chef')
	parser.add_argument('-f','--file',help="The text file from which to load recipes",required=False, default=None)
	parser.add_argument('-w','--website',help="The web URL from which to scrape (not implemented yet)",required=False, default=None)
	parser.add_argument('-d','--db',help="The mongodb database to which to save",required=True)
	parser.add_argument('-c','--collection',help="The mongodb collection to which to save",required=True)

	args = parser.parse_args()

	client = pymongo.MongoClient()
	db = args.db
	collection = db[args.collection]

	if args.website is not None:
		print "Website-scraping is not implemented.  Sorry!"
		sys.exit()
	try:
		with open(args.file, "rb") as recipe_source:
			recipe_separator.separate(recipe_source, collection)
	except:
		"No file provided, or provided file not found.  Sorry!"
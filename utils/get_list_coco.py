## Function to return list of categories from COCO format annotation files
import os
import json


# Function to return list of categories from dataset
def classes(anno_dir):
	anno_files = os.listdir(anno_dir)
	classes = []

	for f in anno_files:
		if '.json' not in f:
			print('Warning: annotation file not recognized')
			continue

		anno_file = open(anno_dir + f)
		data = json.load(anno_file)

		categories = data["categories"]

		for category in categories:
			name = category["name"]
			if name not in classes:
				classes.append(name)

	classes.sort()
	return classes
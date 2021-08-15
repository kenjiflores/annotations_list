## Function to return list of categories in 
## a group of Pascal VOC-formatted annotation files

import os
import xml.etree.ElementTree as ET

# Function to return list of categories from dataset
def classes(anno_dir):
	anno_files = os.listdir(anno_dir)
	categories = []

	for f in anno_files:
		if '.xml' not in f:
			print('Warning: annotation file not recognized')
			continue

		anno_file = anno_dir + f
		tree = ET.parse(anno_file)
		root = tree.getroot()

		for obj in root.findall('object'):
			name = obj.find('name').text
			if name not in categories:
				categories.append(name)

	categories.sort()
	return categories
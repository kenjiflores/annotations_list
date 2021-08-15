## Function to extract annotations from images
import os
import shutil
import xml.etree.ElementTree as ET
import cv2


# Function to extract annotations from every image
def extract(images_dir, annotations_dir, instances_dir, classes):
	categories = classes
	img_dir = images_dir
	anno_dir = annotations_dir
	save_dir = instances_dir

	for category in categories: 
		os.mkdir(save_dir + category)

	anno_files = os.listdir(anno_dir)

	for f in anno_files:
		if '.xml' not in f:
			print('Warning: annotation file not recognized')
			continue

		anno_file = anno_dir + f
		tree = ET.parse(anno_file)
		root = tree.getroot()
		img = root.find('filename').text

		image = cv2.imread(img_dir + img)

		count = 0
		for obj in root.findall('object'):
			name = obj.find('name').text
			x1 = int(float(obj.find('./bndbox/xmin').text))
			y1 = int(float(obj.find('./bndbox/ymin').text))
			x2 = int(float(obj.find('./bndbox/xmax').text))
			y2 = int(float(obj.find('./bndbox/ymax').text))

			new_save_dir = save_dir + name + '/'
			ROI = image[y1:y2,x1:x2]
			unit_name = img.split('.')[0] + '__' + str(count) + '.png'
			cv2.imwrite(new_save_dir + unit_name, ROI)

			count = count + 1
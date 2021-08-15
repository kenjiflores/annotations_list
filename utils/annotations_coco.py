## Function to extract annotations from images
import os
import shutil
import cv2
import json


class instance():

	def __init__(self, coco_data, image_id, category_id, bbox):
		self.coco_data = coco_data
		self.image_id = image_id
		self.category_id = category_id
		self.bbox = bbox

	def img_id(self):
		data = self.coco_data
		images = data["images"]
		for image in images:
			if self.image_id == image["id"]:
				filename = image["file_name"]
		return filename

	def class_id(self):
		data = self.coco_data
		categories = data["categories"]
		for cat in categories:
			if self.category_id == cat["id"]:
				category = cat["name"]
		return category

	def coordinates(self):
		return self.bbox

	def save_object(self, count, filename, category, bbox):
		img_dir = './data/images/'
		save_dir = './data/instances/'

		image = cv2.imread(img_dir + filename)

		x1 = bbox[0]
		y1 = bbox[1]
		x2 = x1 + bbox[2]
		y2 = y1 + bbox[3]

		name = category
		new_save_dir = save_dir + name + '/'
		ROI = image[y1:y2,x1:x2]
		unit_name = filename.split('.')[0] + '__' + str(count) + '.png'
		cv2.imwrite(new_save_dir + unit_name, ROI)



# Function to extract annotations from every image
def extract(images_dir, annotations_dir, instances_dir, classes):
	categories = classes
	img_dir = images_dir
	anno_dir = annotations_dir
	save_dir = instances_dir

	objects = dict()

	for category in categories: 
		os.mkdir(save_dir + category)

	anno_files = os.listdir(anno_dir)

	for f in anno_files:
		if '.json' not in f:
			print('Warning: annotation file not recognized')
			continue

		anno_file = open(anno_dir + f)
		data = json.load(anno_file)

		annotations = data["annotations"]
		count = 0
		for anno in annotations:
			image_id = anno["image_id"]
			category_id = anno["category_id"]
			bbox = anno["bbox"]
			anno_id = anno["id"]	

			inst = instance(data, image_id, category_id, bbox)
			objects[anno_id] = inst

			category = inst.class_id()
			filename = inst.img_id()
			try:
				inst.save_object(count, filename, category, bbox)
			except:
				print('Warning: object from ' + filename + ' not saved')
			count = count + 1
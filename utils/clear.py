# Function to clear data in instances folder before new run
import os
import shutil

def clear_instances(directory):
	instances_folder = directory
	folders = os.listdir(instances_folder)
	for folder in folders:
			shutil.rmtree(instances_folder + folder)

	print('\nInstances folder cleared\n')


def clear_all():

	img_dir  = './data/images/'
	anno_dir = './data/annotations/'
	save_dir = './data/instances/'

	imgs = os.listdir(img_dir)
	annos = os.listdir(anno_dir)
	object_folders = os.listdir(save_dir)

	for img in imgs:
		os.remove(img_dir + img)

	for anno in annos:
		os.remove(anno_dir + anno)

	for folder in object_folders:
		shutil.rmtree(save_dir + folder)
import os
import xml.etree.ElementTree as ET
import cv2

from utils import get_list_voc, annotations_voc, clear, create
from utils import get_list_coco, annotations_coco

## Specify directories
img_dir  = './data/images/'
anno_dir = './data/annotations/'
save_dir = './data/instances/'

## Clear instances directory
clear.clear_instances(directory = save_dir)

## Return list of annotation files
anno_files = os.listdir(anno_dir)


## Run program for COCO format annotations
if any('.json' in s for s in anno_files):

	print('Extracting COCO-format annotations\n')
	# Return list of all categories occurring in the dataset
	categories = get_list_coco.classes(anno_dir)

	# Extract annotations of all categories occurring in the dataset
	annotations_coco.extract(images_dir = img_dir, annotations_dir = anno_dir, 
						instances_dir = save_dir, classes = categories)


## Run program for Pascal VOC format annotations
else:

	print('Extracting Pascal VOC-format annotations\n')
	# Return list of all categories occurring in the dataset
	categories = get_list_voc.classes(anno_dir)

	# Extract annotations of all categories occurring in the dataset
	annotations_voc.extract(images_dir = img_dir, annotations_dir = anno_dir, 
						instances_dir = save_dir, classes = categories)



## Create HTML file containing table of annotations
create.table(instances_dir = save_dir, categories = categories)
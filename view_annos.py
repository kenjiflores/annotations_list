import os
import xml.etree.ElementTree as ET
import cv2

from utils import get_list, create, annotations

## Specify directories
img_dir  = './data/images/'
anno_dir = './data/annotations/'
save_dir = './data/instances/'

## Return list of all categories occurring in the dataset
categories = get_list.classes(anno_dir)

## Extract annotations of all categories occurring in the dataset
annotations.clear_folder(directory = save_dir)
annotations.extract(images_dir = img_dir, annotations_dir = anno_dir, 
					instances_dir = save_dir, classes = categories)

## Create HTML file containing table of annotations
create.table(instances_dir = save_dir, categories = categories)
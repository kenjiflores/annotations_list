## Functions to create table and save table as HTML file

import pandas as pd
import numpy as np
from IPython.core.display import HTML
import os


# Converting image paths to html tags
def write_html(path):
	html_tag = ''
	if isinstance(path, str):
		html_tag = '<img src="'+ path + '" style="max-height:250px;max-width:250px;min-height:30px;min-width:30px;height:auto;width:auto;" >'
	else:
		for image in path:
			string = '<img src="'+ image + '" style="max-height:250px;max-width:250px;min-height:30px;min-width:30px;height:auto;width:auto;" >\n'
			html_tag = html_tag + string
	return html_tag


# Function to create HTML table file from annotations in pandas dataframe
def table(instances_dir, categories):
	print('Creating HTML table')
	classes = categories
	save_dir = instances_dir

	imgs_lists = []
	for category in classes:
		img_list = []
		category_path = save_dir + category + '/'
		instances = os.listdir(category_path)
		for img in instances:
			img_path = category_path + img
			img_list.append(img_path)
		imgs_lists.append(img_list)

	df = pd.DataFrame(categories, columns = ['Category'])
	df['Instances'] = imgs_lists
	pd.set_option('colheader_justify', 'center')

	# Saving dataframe in html file
	df.to_html('annotations_list.html',escape=False, formatters=dict(Instances=write_html))
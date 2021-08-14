## Annotations List

Simple tool to create a table with all annotation instances in an object detection dataset.
(Currently only works with Pascal VOC format annotations)

### Usage

1. Create annotated dataset with Pascal VOC format XML files (using [LabelImg](https://github.com/tzutalin/labelImg) or similar tool).

2. Move image dataset to `data/images/` folder in the project directory.

3. Move the respective annotation files to `data/annotations/` folder.

	* All data in the `data/instances/` folder will be deleted automatically in every run.

4. Run the `view_annos.py` file in the command line:

```sh
> python view_annos.py
```
5. An HTML file (named `annotations_list.html`) with the table of annotations will be generated and saved in the main project folder.


Required packages: [OpenCV](https://pypi.org/project/opencv-python/) 


Any comments and issues are very welcome!

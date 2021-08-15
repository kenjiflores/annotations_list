## Annotations List

Simple tool to create a table with all annotation instances in an object detection dataset.

(Works with COCO and Pascal VOC annotation formats)

### Usage

1. Create annotated dataset with COCO `.json` or Pascal VOC format `.xml` files (using [LabelImg](https://github.com/tzutalin/labelImg) or similar tool).

2. Move image dataset to `data/images/` folder in the project directory.

3. Move the respective annotation file(s) to `data/annotations/` folder.

	* All data in the `data/instances/` folder will be deleted automatically in every run.

4. Run the `main.py` file in the command line:

```sh
> python main.py
```
5. An HTML file (named `annotations_list.html`) with the table of annotations will be generated and saved in the main project folder.


**Required packages**: [OpenCV](https://pypi.org/project/opencv-python/) 


Example result:

![example](example/example2.png) 


Any comments and issues are very welcome!
# object_detection_YOLOV5

first clone YOLOV5

pre code,  git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
.md:not(.use-csslab) pre code
 {
  white-space: pre-wrap;
}

then edit coco.ymal:

train_path: /path/to/train/
val_path: /path/to/val/
test_path: /path/to/test/

#number_of_classes
nc: 1

#classes
class_names: ['your_class']


last, train your model, you can use hyp.scratch which contains augmentations:

'''python train.py --img 640 --epochs 200 --data coco.yaml --weights yolov5l.pt  --batch-size 16 --nosave --cache --patience 10 --hyp hyp.scratch-low.yaml'''

you can ten validate your model's performance:

'''python val.py --weights /path/to/model.pt --data coco.yaml --img 640'''

check your model on new image:

'''python detect.py --weights /path/to/model.pt --source /path/to/img --img 640 --save-txt --save-conf'''

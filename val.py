import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('FeatherYOLO.pt')
    model.val(data='feather.v9i.yolov11/data.yaml',
              split='test',
              imgsz=640,
              batch=16,
              # iou=1,
              # rect=False,
              # save_json=True, # if you need to cal coco metrice
              project='runs/val',
              name='exp',
              )
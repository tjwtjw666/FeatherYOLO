import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('FeatherYOLO.yaml')
    # model.load('yolo11n.pt') # loading pretrain weights
    model.train(data='feather.v9i.yolov11/data.yaml',
                cache=False,
                imgsz=640,
                epochs=300,
                batch=32,
                close_mosaic=0,
                workers=4,
                # device='0',
                optimizer='SGD', # using SGD
                # patience=0, # set 0 to close earlystop.
                # resume=True, # 断点续训,YOLO初始化时选择last.pt
                # amp=False, # close amp
                # fraction=0.2,
                project='runs/train',
                name='exp',
                )
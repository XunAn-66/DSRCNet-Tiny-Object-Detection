import warnings
import matplotlib

matplotlib.use('Agg')
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/v8/yolov8s-dsrc.yaml')
    model.train(data='../dataset/data.yaml',
                cache=False,
                imgsz=640,
                epochs=300,
                batch=4,
                close_mosaic=40,
                workers=0,
                optimizer='SGD',
                patience=20,
                project='runs/train',
                name='exp',
                )

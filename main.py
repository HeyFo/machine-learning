from ultralytics import YOLO

model = YOLO("yolov8x.pt")  

results = model.train(data="C:/Users/nazira/Downloads/heyfo.v3i.yolov8/data.yaml", epochs=25, imgsz=64)
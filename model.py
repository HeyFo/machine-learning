from ultralytics import YOLO
model = YOLO("")  
names = model.names
objects = []
results = model('')
for result in results:
    boxes = result.boxes  
    for c in boxes.cls:
            label = names[int(c)]
            if label not in objects:
                objects.append(label)

print(objects)